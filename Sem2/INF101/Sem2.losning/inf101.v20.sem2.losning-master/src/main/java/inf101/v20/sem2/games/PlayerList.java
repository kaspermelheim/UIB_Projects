package inf101.v20.sem2.games;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * This class keep track of players and who's turn it is.
 * In this project that might be overkill since there are only 2 players.
 * But I think the code becomes more readable when we have a PlayerList class
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 */
public class PlayerList implements Iterable<Player>{

	private ArrayList<Player> players;
	private int currentIndex;

	/**
	 * Constructs a new empty PlayerList
	 */
	public PlayerList() {
		players = new ArrayList<Player>();
		currentIndex = 0;
	}
	
	/**
	 * @return the player who has turn now
	 */
	public Player currentPlayer() {
		return players.get(currentIndex);
	}
	
	/**
	 * Advances the current player.
	 * @return the next player;
	 */
	public Player nextPlayer() {
		next();
		return currentPlayer();
	}

	/**
	 * advances the PlayerList to the next player
	 */
	private void next() {
		currentIndex++;
		updateIndex();
	}

	/**
	 * Advances the index to the next in the list, if the end is reached
	 * the index restarts on the beginning.
	 */
	private void updateIndex() {
		if(currentIndex>=players.size() || currentIndex<0)
			currentIndex = 0;
	}
	
	/**
	 * This method removes a player from the list.
	 * In this project there is no need to remove a Player.
	 * But in general one might think of games with more players
	 * where those who loose the game is removed
	 * 
	 * @param index The index to remove
	 * @return The Player removed from the PlayerList
	 */
	public Player remove(int index) {
		Player p = players.remove(index);
		if(index < currentIndex)
			currentIndex--;
		updateIndex();
		return p;
	}
	
	/**
	 * Removes a player from this list
	 * @param p
	 * @return
	 */
	public boolean remove(Player p) {
		int index = players.indexOf(p);
		if(index<0)
			return false;
		else {
			remove(index);
			updateIndex();
			return true;
		}
	}

	/** 
	 * @return The number of players in this list
	 */
	public int size() {
		return players.size();
	}

	/**
	 * Adds a player to the playing list. currentPlayer() will return the same before and after a player is added. 
	 * @param player
	 */
	public void add(Player player) {
		for(Player p : players) {
			if(p.usesSameSymbol(player))
				throw new IllegalArgumentException("Two players can not have same piece");
		}
		players.add(player);
	}

	@Override
	public Iterator<Player> iterator() {
		return players.iterator();
	}

}
