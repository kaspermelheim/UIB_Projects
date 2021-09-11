package inf101.v20.rogue101.game;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

import inf101.v20.gfx.Screen;
import inf101.v20.gfx.gfxmode.IBrush;
import inf101.v20.gfx.textmode.Printer;
import inf101.v20.grid.GridDirection;
import inf101.v20.grid.IGrid;
import inf101.v20.grid.ILocation;
import inf101.v20.rogue101.map.GameMap;
import inf101.v20.rogue101.map.IGameMap;
import inf101.v20.rogue101.map.IMapView;
import inf101.v20.rogue101.map.MapReader;
import inf101.v20.rogue101.objects.Amulet;
import inf101.v20.rogue101.objects.IActor;
import inf101.v20.rogue101.objects.IItem;
import inf101.v20.rogue101.objects.IPlayer;
import inf101.v20.rogue101.objects.Portal;
import javafx.scene.input.KeyCode;

/**
 * A game implementation for Rogue 101
 * 
 * @author anya
 * @author Anna Eilertsen - anna.eilertsen@uib.no
 *
 */
public class Game implements IGame {
	/**
	 * All the IActors that have things left to do this turn
	 */
	private List<IActor> actors = Collections.synchronizedList(new ArrayList<>());

	/**
	 * This game's random generator
	 */
	private Random random = new Random();
	/**
	 * The game map. {@link IGameMap} gives us a few more details than
	 * {@link IMapView} (write access to item lists); the game needs this but
	 * individual items don't.
	 */
	private IGameMap map;
	/**
	 * The actor who gets to perform an action this turn
	 */
	private IActor currentActor;
	/**
	 * The current location of the current actor
	 */
	private ILocation currentLocation;
	private int movePoints = 0;
	private int numPlayers = 0;
	GameGraphics graphics;

	public Game(Screen screen, IBrush painter, Printer printer) {

		// NOTE: in a more realistic situation, we will have multiple levels (one map
		// per level), and (at least for a Roguelike game) the levels should be
		// generated
		//
		// inputGrid will be filled with single-character strings indicating what (if
		// anything)
		// should be placed at that map square
		IGrid<String> inputGrid = MapReader.readFile("maps/level1.txt");
		if (inputGrid == null) {
			System.err.println("Map not found – falling back to builtin map");
			inputGrid = MapReader.readString(MapReader.BUILTIN_MAP);
		}
		this.map = new GameMap(inputGrid.getArea());
		for (ILocation loc : inputGrid.locations()) {
			char c = inputGrid.get(loc).charAt(0);
			try {
				IItem item = createItem(c);
				if(item != null)
					map.add(loc, item);
			} catch (IllegalArgumentException e) {
				e.printStackTrace();
			}
		}
		graphics = new GameGraphics(painter, printer, map);
	}

	public Game(String mapString) {
		IGrid<String> inputGrid = MapReader.readString(mapString);
		this.map = new GameMap(inputGrid.getArea());
		for (ILocation loc : inputGrid.locations()) {
			char c = inputGrid.get(loc).charAt(0);
			IItem item = createItem(c);
			if (item != null) {
				map.add(loc, item);
			}
		}

		graphics = new GameGraphics(map);
	}

	@Override
	public void addItem(IItem item) {
		map.add(currentLocation, item);
	}

	@Override
	public void addItem(char symbol) {
		IItem item = ItemFactory.createItem(symbol);
		if (item != null)
			map.add(currentLocation, item);
	}

	public boolean attack(GridDirection dir) {
		ILocation loc = map.getNeighbour(getLocation(), dir);
		List<IActor> actorsOnTargetLoc = map.getActors(loc);
		if (actorsOnTargetLoc.isEmpty())
			return true;
		actorsOnTargetLoc.sort(null);
		IActor target = actorsOnTargetLoc.get(0);
		if (attack(dir, target).equals(currentLocation))
			return false;
		return true;
	}

	@Override
	public ILocation attack(GridDirection dir, IItem target) {
		ILocation loc = map.getNeighbour(getLocation(), dir);
		if (!map.has(loc, target))
			throw new IllegalMoveException("Target isn't there!");

		if (Game.attackSucceeds(currentActor, target))
			target.handleDamage(currentActor.getDamage());

		map.clean(loc);
		if (target.isDestroyed()) {
			return move(dir);
		} else {
			movePoints--;
			return currentLocation;
		}
	}

	/**
	 * Begin a new game turn, or continue to the previous turn
	 *
	 * @return True if the game should wait for more user input
	 */
	public boolean doTurn() {
		do {
			if (actors.isEmpty()) {
				// System.err.println("new turn: " + turnCount++);

				// no one in the queue, we're starting a new turn!
				// first collect all the actors:
				beginTurn();
			}

			// process actors one by one; for the IPlayer, we return and wait for keypresses
			while (!actors.isEmpty()) {
				// get the next player or non-player in the queue
				currentActor = actors.remove(0);
				if (currentActor.isDestroyed()) { // skip if it's dead
					continue;
				}
				currentLocation = map.getLocation(currentActor);
				if (currentLocation == null) {
					displayDebug("doTurn(): Whoops! Actor has disappeared from the map: " + currentActor);
				}
				movePoints = 1; // everyone gets to do one thing

				if (currentActor instanceof IPlayer) {
					if (currentActor.getCurrentHealth() <= 0) {
						// a dead human player gets removed from the game
						// TODO: you might want to be more clever here
						displayStatus(currentActor.getShortName() + " died.");
						// map.remove(currentLocation, currentActor);
						// currentActor = null;
						// currentLocation = null;
					} else {
						currentActor.doTurn(this);
					}
					// For the human player, we need to wait for input, so we just return.
					// Further keypresses will cause keyPressed() to be called, and once the human
					// makes a move, it'll lose its movement point and doTurn() will be called again
					//
					// NOTE: currentActor and currentLocation are set to the IPlayer (above),
					// so the game remembers who the player is whenever new keypresses occur. This
					// is also how e.g., getLocalItems() work – the game always keeps track of
					// whose turn it is.
					return true;
				} else if (currentActor instanceof IActor) {
					ILocation oldLocation = map.getLocation(currentActor);
					try {
						// computer-controlled players do their stuff right away
						currentActor.doTurn(this);
						// remove any dead items from current location
					} catch (Exception e) {
						// actor did something wrong
						// do nothing, leave this IActor
					}
					map.clean(currentLocation);
					map.clean(oldLocation);
				} else {
					displayDebug("doTurn(): Hmm, this is a very strange actor: " + currentActor);
				}
			}

		} while (numPlayers > 0); // we can safely repeat if we have players, since we'll return (and break out of
		// the loop) once we hit the player

		return true;
	}

	/**
	 * Go through the map and collect all the actors.
	 */
	private void beginTurn() {
		numPlayers = 0;
		// this extra fancy iteration over each map location runs *in parallel* on
		// multicore systems!
		// that makes some things more tricky, hence the "synchronized" block and
		// "Collections.synchronizedList()" in the initialization of "actors".
		// NOTE: If you want to modify this yourself, it might be a good idea to replace
		// "parallelStream()" by "stream()", because weird things can happen when many
		// things happen
		// at the same time! (or do INF214 or DAT103 to learn about locks and threading)
		map.getArea().parallelStream().forEach((loc) -> { // will do this for each location in map
			List<IItem> list = map.getAllModifiable(loc); // all items at loc
			Iterator<IItem> li = list.iterator(); // manual iterator lets us remove() items
			List<IItem> toRemove = new ArrayList<IItem>();
			while (li.hasNext()) { // this is what "for(IItem item : list)" looks like on the inside
				IItem item = li.next();
				if (item.getCurrentHealth() < 0) {
					// normally, we expect these things to be removed when they are destroyed, so
					// this shouldn't happen
					synchronized (this) {
						formatDebug("beginTurn(): found and removed leftover destroyed item %s '%s' at %s%n",
								item.getLongName(), item.getGraphicTextSymbol(), loc);
					}
					toRemove.add(item);
				} else if (item instanceof IPlayer) {
					actors.add(0, (IActor) item); // we let the human player go first
					synchronized (this) {
						numPlayers++;
					}
				} else if (item instanceof IActor) {
					actors.add((IActor) item); // add other actors to the end of the list
				}
			}
			for (IItem item : toRemove)
				map.remove(loc, item); // need to do this too, to update item map

		});
	}

	@Override
	public boolean canGo(GridDirection dir) {
		ILocation location = getLocation(dir);
		if (containsActor(location, Portal.class) && currentActor instanceof IPlayer) {
			IPlayer currentPlayer = (IPlayer) currentActor;
			Portal portal = (Portal) map.getActors(location).get(0);
			if (currentPlayer.hasItem(Amulet.getInstance())) {
				displayStatus("Congratulations, you reached the portal with the " + Amulet.getInstance().getShortName()
						+ " and won the game!");
				portal.open();
				map.remove(location, portal);
				return true;
			}
		}
		return map.canGo(currentLocation, dir);
	}

	@Override
	public IItem createItem(char sym) {
		return ItemFactory.createItem(sym);
	}

	@Override
	public void displayDebug(String s) {
		graphics.displayDebug(s);
	}

	@Override
	public void displayMessage(String s) {
		graphics.displayMessage(s);
	}

	@Override
	public void displayStatus(String s) {
		graphics.displayStatus(s);
	}

	public void draw() {
		graphics.draw();
	}

	@Override
	public boolean drop(IItem item) {
		if (item != null) {
			map.add(currentLocation, item);
			return true;
		} else
			return false;
	}

	@Override
	public void formatDebug(String s, Object... args) {
		graphics.formatDebug(s, args);
	}

	@Override
	public void formatMessage(String s, Object... args) {
		graphics.formatMessage(s, args);
	}

	@Override
	public void formatStatus(String s, Object... args) {
		graphics.formatStatus(s, args);
	}

	@Override
	public int getHeight() {
		return map.getHeight();
	}

	@Override
	public List<IItem> getLocalNonActorItems() {
		return map.getItems(currentLocation);
	}

	@Override
	public ILocation getLocation() {
		return currentLocation;
	}

	@Override
	public ILocation getLocation(GridDirection dir) {
		if (currentLocation.canGo(dir))
			return currentLocation.go(dir);
		else
			return null;
	}

	/**
	 * Return the game map. {@link IGameMap} gives us a few more details than
	 * {@link IMapView} (write access to item lists); the game needs this but
	 * individual items don't.
	 */
	@Override
	public IMapView getMap() {
		return map;
	}

	@Override
	public List<GridDirection> getPossibleMoves() {
		return map.getPossibleMoves(currentLocation);
	}

	@Override
	public List<ILocation> getReachable() {
		return map.getReachable(currentLocation, 5);
	}

	@Override
	public int getWidth() {
		return map.getWidth();
	}

	public void keyPressed(KeyCode code) {
		// only an IPlayer/human can handle keypresses, and only if it's the human's
		// turn
		// NB: all codes are for the large letter, even if a small one was pushed
		if (currentActor instanceof IPlayer) {
			if (currentActor.getCurrentHealth() <= 0) {
				graphics.displayMessage("Sorry, you're dead!");
			} else {
				((IPlayer) currentActor).keyPressed(this, code); // do your thing
			}
		}
	}

	@Override
	public ILocation move(GridDirection dir) {
		if (movePoints < 1)
			throw new IllegalMoveException("You're out of moves!");
		if (!canGo(dir))
			throw new IllegalMoveException("You cannot go there!");
		ILocation newLoc = map.go(currentLocation, dir);
		map.remove(currentLocation, currentActor);
		map.add(newLoc, currentActor);
		currentLocation = newLoc;
		movePoints--;
		return currentLocation;
	}

	@Override
	public IItem pickUp(IItem item) {
		if (item == null || !map.has(currentLocation, item))
			return null;
		if (!Game.pickUpSucceeds(currentActor, item))
			return null;
		map.remove(currentLocation, item);
		return item;
	}

	@Override
	public ILocation rangedAttack(GridDirection dir, IItem target) {
		return currentLocation;
	}

	@Override
	public IActor getActor() {
		return currentActor;
	}

	public ILocation setCurrent(IActor actor) {
		currentLocation = map.getLocation(actor);
		if (currentLocation != null) {
			currentActor = actor;
			movePoints = 1;
		}
		return currentLocation;
	}

	public IActor setCurrent(ILocation loc) {
		List<IActor> list = map.getActors(loc);
		if (!list.isEmpty()) {
			currentActor = list.get(0);
			currentLocation = loc;
			movePoints = 1;
		}
		return currentActor;
	}

	public IActor setCurrent(int x, int y) {
		return setCurrent(map.getLocation(x, y));
	}

	@Override
	public Random getRandom() {
		return random;
	}

	@Override
	public <T extends IActor> boolean containsActor(ILocation loc, Class<T> c) {
		for (IActor actor : map.getActors(loc)) {
			if (c.isInstance(actor))
				return true;
		}
		return false;
	}

	public <T extends IItem> boolean containsItem(Class<T> c) {
		List<IItem> items = getLocalNonActorItems();
		for (IItem item : items) {
			if (c.isInstance(item))
				return true;
		}
		return false;
	}

	@Override
	public <T extends IItem> boolean containsItem(ILocation loc, Class<T> c) {
		for (IItem item : map.getItems(loc)) {
			if (c.isInstance(item))
				return true;
		}
		return false;
	}

	/**
	 * An {@link IActor} succeeds at picking up a target item if the actors attack score 
	 * is strictly larger than the target's size
	 * 
	 * @param actor the {@link IActor} trying to pick up the item 
	 * @param item   the {@link IItem} to be picked up
	 * @return true if picking up succeeds, false otherwise
	 */
	public static boolean pickUpSucceeds(IActor actor, IItem item) {
		return actor.getAttack() > item.getSize();
	}

	/**
	 * An attack succeeds if the attacker's attack score is strictly larger than,
	 * the target's defense score.
	 * 
	 * @param attacker the attacking {@link IActor}
	 * @param target   the target {@link IItem}
	 * @return true if the attack succeeds, false otherwise
	 */
	public static boolean attackSucceeds(IActor attacker, IItem target) {
		return attacker.getAttack() > target.getDefence();
	}
}
