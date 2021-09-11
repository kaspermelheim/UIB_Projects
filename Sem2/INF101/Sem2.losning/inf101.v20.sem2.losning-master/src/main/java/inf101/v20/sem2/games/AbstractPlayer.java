package inf101.v20.sem2.games;

/**
 * This class takes care of the name and symbol handling in Player classes.
 * Using an abstract class here means we avoid duplicating this code in each
 * class of Players.
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public abstract class AbstractPlayer implements Player {

	protected String symbol;
	protected String name;
	
	/**
	 * This Constructor can not be called directly, but classes extending (inheriting from)
	 * AbstractPlayer will be able to call this constructor
	 * @param piece
	 * @param name
	 */
	public AbstractPlayer(String piece, String name) {
		if(piece == null)
			throw new IllegalArgumentException("Each player need to have a Symbol to play");
		this.symbol = piece;
		this.name = name;
	}

	@Override
	public String toString() {
		return getName()+" with symbol "+getSymbol();
	}
	
	@Override
	public String getName() {
		return name;
	}

	@Override
	public boolean usesSameSymbol(Player player) {
		return getSymbol().contentEquals(player.getSymbol());
	}

	@Override
	public String getSymbol() {
		return symbol;
	}
	
}
