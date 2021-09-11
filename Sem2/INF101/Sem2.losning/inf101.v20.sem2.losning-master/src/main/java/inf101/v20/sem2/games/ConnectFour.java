package inf101.v20.sem2.games;

import inf101.v20.sem2.grid.GridDirection;
import inf101.v20.sem2.grid.Location;

/**
 * This game is played on a 6 x 7 board.
 * The players select a column and the placement will be on the lowest
 * available row of that column.
 *  
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class ConnectFour extends AbstractGame {

	public ConnectFour() {
		super(new GameBoard(6, 7));
	}

	public ConnectFour(Iterable<Player> players) {
		super(new GameBoard(6, 7),players);
	}

	public ConnectFour(GameBoard board, Iterable<Player> players) {
		super(board,players);
	}

	@Override
	public String getName() {
		return "Connect Four";
	}

	@Override
	public boolean isWinner(Player player) {
		return board.countNumInRow(player)>=4;
	}
	
	@Override
	public boolean canPlace(Location loc, Player p) {
		if(!super.canPlace(loc, p))
			return false;
		if(super.canPlace(loc.move(GridDirection.SOUTH), p)) {
			return false;
		}
		return true;
	}

	@Override
	protected void makeMove(Location loc, Player p) {
		super.makeMove(drop(loc),p);
	}

	/**
	 * This method disregards the row number of the input location and finds
	 * The lowest row number such that it is possible to place on that position.
	 * If no location in that column is possible to place on the highest
	 * row number on the board is used.
	 * 
	 * @param loc
	 * @return
	 */
	public Location drop(Location loc) {
		return drop(loc.getCol());
	}
	
	/**
	 * Finds the valid location in a column (there is at most 1 valid position in each column)
	 * @param column the column to place a piece in.
	 * @return the location to place at, if there is a valid location that one will be returned, otherwise the top location will be returned.
	 */
	public Location drop(int column) {
		return dropFrom(new Location(0, column));
	}

	/**
	 * This method starts from a location and moves down 
	 * until it can not move further.
	 * 
	 * @param loc
	 * @return
	 */
	Location dropFrom(Location loc) {
		Location below = loc.move(GridDirection.SOUTH); 
		while(board.validLocation(below) && board.isEmpty(below)){
			loc = below;
			below = loc.move(GridDirection.SOUTH);
		}
		return loc;
	}
	
	@Override
	public AbstractGame copy() {
		AbstractGame newGame = new ConnectFour(board.copy(),players);
		newGame.setPlayer(getCurrentPlayer());
		return newGame;
	}

}
