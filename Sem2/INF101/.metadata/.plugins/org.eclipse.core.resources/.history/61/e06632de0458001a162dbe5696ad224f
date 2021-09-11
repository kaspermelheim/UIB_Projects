package inf101.v20.rogue101.objects;

import inf101.v20.gfx.gfxmode.DrawHelper;
import inf101.v20.gfx.gfxmode.IBrush;
import inf101.v20.gfx.textmode.Printer;
import inf101.v20.rogue101.RogueApplication;
import javafx.scene.paint.Color;

/**
 * En gulrot i Rogue 101-spillet.  
 * 
 * Gulrøtter dør hvis de blir spist. 
 * 
 * @author Anna Eilertsen - anna.eilertsen@uib.no
 *
 */
public class Carrot implements IItem {
	/**
	 * char representation of this type 
	 */
	public static final char SYMBOL = 'C';
	private int hp = getMaxHealth();

	@Override
	public boolean draw(IBrush painter, double w, double h) {
		if (!RogueApplication.USE_EMOJI) {
			DrawHelper.drawCarrot(painter, h, w, getHealthStatus());
			return true;
		} else {
			return false;
		}
	}

	@Override
	public int getCurrentHealth() {
		return hp;
	}

	@Override
	public int getDefence() {
		return 0;
	}

	@Override
	public int getMaxHealth() {
		return 5;
	}

	@Override
	public String getShortName() {
		return "carrot";
	}

	@Override
	public String getLongName() {
		return "juicy carrot";
	}

	@Override
	public int getSize() {
		return 2;
	}

	@Override
	public String getGraphicTextSymbol() {
		if (useEmoji()) {
			return Printer.coloured("🥕", Color.ORANGE);
		} else {
			return "" + SYMBOL;
		}

	}

	private boolean useEmoji() {
		return RogueApplication.USE_EMOJI;
	}

	@Override
	public int handleDamage(int amount) {
		return amount;
	}
	
	@Override
	public char getSymbol() {
		return SYMBOL;
	}
}
