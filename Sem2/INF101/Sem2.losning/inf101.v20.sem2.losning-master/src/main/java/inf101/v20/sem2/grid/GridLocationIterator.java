package inf101.v20.sem2.grid;

import java.util.Iterator;

/**
 * This class is able to iterate over all locations in a grid.
 *  
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class GridLocationIterator implements Iterator<Location>, Iterable<Location> {
	
	int numRows;
	int numCols;
	int currentRow;
	int currentCol;
	
	/**
	 * Constructs a GridLocationIterator
	 * @param grid - the grid which we want to iterate through
	 */
	public GridLocationIterator(Grid<?> grid) {
		this(grid.numRows(),grid.numCols());
	}

	/**
	 * Constructs a GridLocationIterator
	 * @param numRows - number of rows in the grid
	 * @param numCols - number of columns in the grid
	 */
	public GridLocationIterator(int numRows,int numCols) {
		this.numRows = numRows;
		this.numCols = numCols;
	}
	
	@Override
	public boolean hasNext() {
		return currentRow<numRows && currentCol<numCols;
	}

	@Override
	public Location next() {
		Location elem = new Location(currentRow, currentCol);
		currentCol++;
		if(currentCol>=numCols) {
			currentCol=0;
			currentRow++;
		}
		return elem;
	}

	@Override
	public Iterator<Location> iterator() {
		return new GridLocationIterator(numRows,numCols);
	}

}
