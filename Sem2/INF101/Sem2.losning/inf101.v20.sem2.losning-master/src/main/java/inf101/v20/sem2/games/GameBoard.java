package inf101.v20.sem2.games;

import inf101.v20.sem2.grid.Grid;
import inf101.v20.sem2.grid.GridDirection;
import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.tools.Range;

/**
 * Keeps track of a grid and where on this grid different Players have placed.
 * It is only allowed to place if the position is empty
 * @author mva021
 *
 */
public class GameBoard extends Grid<Player>{

	/**
	 * Constructs a new GameBoard as a grid
	 * @param rows - number of rows on the board
	 * @param cols - number of columns on the board
	 */
	public GameBoard(int rows, int cols){
		super(rows, cols,null); //we fill with null and let null indicate empty
	}

	@Override
	public void set(Location loc, Player p) {
		if(isEmpty(loc))
			super.set(loc, p);
		else
			throw new IllegalArgumentException("Can not place there, field is occupied.");
	}
	
	/**
	 * Checks if a Player has placed on a given position or if it is free.
	 * @param currentRow - row of position to check
	 * @param currentCol - column of position to check
	 * @return true if the position contains the empty Piece, false otherwise
	 */
	public boolean isEmpty(Location loc) {
		return get(loc)==null;
	}

	/**
	 * Prints a board to the screen
	 */
	public void printBoard() {
		System.out.println(toString());
	}
	
	/**
	 * Counts how many in a row a given Piece has.
	 * @param player - The Piece type we are looking for.
	 * @return
	 */
	public int countNumInRow(Player player) {
		int maxCount = 0;
		for(Location loc : locations()) {
			maxCount = Math.max(maxCount, count(loc, player));
		}
		return maxCount;
	}
	
	/**
	 * Counts to check how many in a row a given Piece has from a given start location.
	 * 
	 * @param loc - start location
	 * @param player - the Piece we are counting
	 * @return
	 */
	public int count(Location loc, Player player) {
		int maxCount = 0;
		for(GridDirection dir : GridDirection.EIGHT_DIRECTIONS) {
			maxCount = Math.max(maxCount, count(loc,dir,player));
		}
		return maxCount;
	}
	
	/**
	 * Counts to check how many in a row a given Player has 
	 * from a given start location and in a given direction.
	 * 
	 * @param loc - start location
	 * @param dir - describes the direction to count in
	 * @param player - the Player we are counting for
	 * @return
	 */
	public int count(Location loc, GridDirection dir, Player player) {
		int count = 0;
		while(validLocation(loc) && get(loc) == player) {
			count ++;
			loc = loc.move(dir);
		}
		return count;
	}
	
	@Override
	public String toString() {
		String s = "";
		for(int row = 0; row<numRows()*2-1; row++) {
			for(int col = 0; col<numCols()*2-1; col++) {
				if(row%2==0) { // row with pieces
					if(col%2==0) {
						//add the char symbol of the piece
						s += getSymbol(get(new Location(row/2, col/2)));
					}else {
						s+='|';
					}
				}else { //row with only boarders
					if(col%2==0)
						s+='-';
					else
						s+='+';					
				}
			}
			s+="\n";
		}
		return s;
	}

	private String getSymbol(Player player) {
		if(player == null)
			return " ";
		else
			return player.getSymbol();
	}

	/**
	 * Checks if there are positions with no piece on yet
	 * @return
	 */
	public boolean isFull() {
		for(Player p : this) {
			if(p==null)
				return false;
		}
		return true;
	}
	
	public Iterable<Integer> rowIndices(){
		return Range.range(numRows());
	}

	public Iterable<Integer> colIndices(){
		return Range.range(numCols());
	}
	
	@Override
	public GameBoard copy() {
		GameBoard newBoard = new GameBoard(numRows(), numCols());
		copy(newBoard);
		return newBoard;
	}
}
