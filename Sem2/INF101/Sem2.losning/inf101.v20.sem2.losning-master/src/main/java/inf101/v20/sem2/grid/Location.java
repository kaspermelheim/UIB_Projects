package inf101.v20.sem2.grid;

/**
 * represents an row, column index of a grid.
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 */
public class Location {
	private int row;
	private int col;
	
	/**
	 * Constructor for location, note that a Location is independent of the Grid implementation,
	 * hence can have values not corresponding to a cell in the grid.
	 * 
	 * @param row
	 * @param col
	 */
	public Location(int row, int col){
		this.row = row;
		this.col = col;
	}
	
	/**
	 * Makes a new Location representing the location adjacent in the given direction
	 * @param dir
	 * @return
	 */
	public Location move(GridDirection dir) {
		return new Location(row+dir.getDy(), col+dir.getDx());
	}

	/**
	 * @return the index of the row containing this Location.
	 */
	public int getRow() {
		return row;
	}

	/**
	 * @return the index of the column containing this Location.
	 */
	public int getCol() {
		return col;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj ==null || !(obj instanceof Location)) {
				return false;
		}
		Location loc = (Location) obj;
		return this.getRow()==loc.getRow() && this.getCol()==loc.getCol();
	}
	
	@Override
	public String toString() {
		return "Location: "+getRow()+","+getCol();
	}
}
