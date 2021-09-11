package inf101.v20.rogue101.objects;

import inf101.v20.rogue101.RogueApplication;

/**
 * Amulet that lets you enter the portal and win the game.
 * 
 * There is only ONE amulet in the game so this class implements the singleton pattern. 
 * @see <a href="https://www.tutorialspoint.com/design_pattern/singleton_pattern.htm">Singleton Pattern</a>
 * 
 * @author anna
 *
 */
public class Amulet implements IItem {
	/**
	 * char representation of this type 
	 */
	public static final char SYMBOL = 'A';
	private int hp = getMaxHealth();
	private static Amulet amuletten = new Amulet();
	
	private Amulet() {
		
	}

	@Override
	public int getCurrentHealth() {
		return hp;
	}

	@Override
	public int getDefence() {
		return 10000;
	}

	@Override
	public int getMaxHealth() {
		return 10000;
	}
	
	@Override
	public String getShortName() {
		return "amulet";
	}

	@Override
	public String getLongName() {
		return "magical amulet";
	}

	@Override
	public int getSize() {
		return 1;
	}

	@Override
	public String getGraphicTextSymbol() {
		if (RogueApplication.USE_EMOJI) {
			return "💳"; 
		} else {
			return "" + SYMBOL;
		}	}

	@Override
	public int handleDamage(int amount) {
		return 0;
	}

	public static IItem getInstance() {
		return amuletten;
	}
	
	@Override
	public char getSymbol() {
		return SYMBOL;
	}
}
