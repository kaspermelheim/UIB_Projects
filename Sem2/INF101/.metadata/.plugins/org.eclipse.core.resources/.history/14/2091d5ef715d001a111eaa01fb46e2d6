package inf101.v20.rogue101.game;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import inf101.v20.gfx.gfxmode.BrushPainter;
import inf101.v20.gfx.gfxmode.IBrush;
import inf101.v20.gfx.textmode.Printer;
import inf101.v20.grid.ILocation;
import inf101.v20.rogue101.RogueApplication;
import inf101.v20.rogue101.map.IGameMap;
import inf101.v20.rogue101.map.IMapView;
import inf101.v20.rogue101.objects.IItem;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

/**
 * @author Martin Vatshelle
 *
 */
public class GameGraphics implements IGameGraphics {

	// graphics application to draw graphics on
	private final IBrush painter;
	private final Printer printer;
	private final List<String> buffer = new ArrayList<>();
	/**
	 * The game map. {@link IGameMap} gives us a few more details than
	 * {@link IMapView} (write access to item lists); the game needs this but
	 * individual items don't.
	 */
	private IGameMap map;

	public GameGraphics(IBrush painter, Printer printer, IGameMap map2) {
		this.painter = painter;
		this.printer = printer;
		this.map = map2;
	}

	public GameGraphics(IGameMap map) {
		printer = new Printer(1280, 720);
		painter = new BrushPainter(1280, 720);
		this.map = map;
	}

	@Override
	public void displayDebug(String s) {
		printer.clearLine(RogueApplication.LINE_DEBUG);
		printer.printAt(1, RogueApplication.LINE_DEBUG, s, Color.DARKRED);
		System.err.println(s);
	}

	@Override
	public void displayMessage(String s) {
		// it should be safe to print to lines RogueApplication.LINE_MSG1,
		// RogueApplication.LINE_MSG2,
		// RogueApplication.LINE_MSG3
		// TODO: you can save the last three lines, and display/scroll them
		buffer.add(s);
		if (printer.hasScreen()) {
			Color col = Color.BLACK;
			for (int i = 0; i < Math.min(3, buffer.size()); i++) {
				printer.clearLine(RogueApplication.LINE_MSG1 + i);
				printer.printAt(1, RogueApplication.LINE_MSG1 + i, buffer.get(buffer.size() - i - 1), col);
				col = col.deriveColor(0.0, 1.0, 1.0, .5);
			}
			System.out.printf("Message %d: «%s»%n", buffer.size(), s);
		}
	}

	@Override
	public void displayStatus(String s) {
		printer.clearLine(RogueApplication.LINE_STATUS);
		printer.printAt(1, RogueApplication.LINE_STATUS, s);
		System.out.println("Status: «" + s + "»");
	}

	public void draw() {
		draw(map.getDirtyLocs());
	}

	public void draw(Set<ILocation> dirtyLocs) {
		if (dirtyLocs.isEmpty())
			return;
		GraphicsContext ctx = painter.as(GraphicsContext.class);
		double h = printer.getCharHeight();
		double w = printer.getCharWidth();
		if (RogueApplication.MAP_AUTO_SCALE_ITEM_DRAW) {
			ctx.save();
			ctx.scale(w / h, 1.0);
			w = h;
		}
		try {
			for (ILocation loc : map.getArea()) {
				ctx.clearRect(loc.getX() * w, loc.getY() * h, w, h);
				List<IItem> list = map.getAll(loc);
				String sym = " ";
				if (!list.isEmpty()) {
					if (RogueApplication.MAP_DRAW_ONLY_DIRTY_CELLS) {
						ctx.clearRect(loc.getX() * w, loc.getY() * h, w, h);
						// ctx.fillRect(loc.getX() * w, loc.getY() * h, w, h);
					}
					painter.save();
					painter.jumpTo((loc.getX() + 0.5) * w, (loc.getY() + 0.5) * h);
					boolean dontPrint = list.get(0).draw(painter, w, h);
					painter.restore();
					if (!dontPrint) {
						sym = list.get(0).getGraphicTextSymbol();
					}
				}
				printer.printAt(loc.getX() + 1, loc.getY() + 1, sym);
			}
		} finally {
			if (RogueApplication.MAP_AUTO_SCALE_ITEM_DRAW) {
				ctx.restore();
			}
		}
		dirtyLocs.clear();
	}

	@Override
	public void formatDebug(String s, Object... args) {
		displayDebug(String.format(s, args));
	}

	@Override
	public void formatMessage(String s, Object... args) {
		displayMessage(String.format(s, args));
	}

	@Override
	public void formatStatus(String s, Object... args) {
		displayStatus(String.format(s, args));
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
	public IBrush getPainter() {
		return painter;
	}

	@Override
	public Printer getPrinter() {
		return printer;
	}

	@Override
	public int[] getFreeTextAreaBounds() {
		int[] area = new int[4];
		area[0] = map.getWidth() + 1;
		area[1] = 1;
		area[2] = printer.getLineWidth();
		area[3] = printer.getPageHeight() - 5;
		return area;
	}

	@Override
	public void clearFreeTextArea() {
		printer.clearRegion(map.getWidth() + 1, 1, printer.getLineWidth() - map.getWidth(),
				printer.getPageHeight() - 5);
	}

	@Override
	public void clearFreeGraphicsArea() {
		painter.as(GraphicsContext.class).clearRect(map.getWidth() * printer.getCharWidth(), 0,
				painter.getWidth() - map.getWidth() * printer.getCharWidth(),
				(printer.getPageHeight() - 5) * printer.getCharHeight());
	}

	@Override
	public double[] getFreeGraphicsAreaBounds() {
		double[] area = new double[4];
		area[0] = map.getWidth() * printer.getCharWidth();
		area[1] = 0;
		area[2] = painter.getWidth();
		area[3] = map.getHeight() * printer.getCharHeight();
		return area;
	}
}
