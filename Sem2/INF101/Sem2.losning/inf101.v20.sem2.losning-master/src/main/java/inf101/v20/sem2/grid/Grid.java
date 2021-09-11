package inf101.v20.sem2.grid;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 
 * A Grid contains a set of elements 
 *
 */
public class Grid<T> implements IGrid<T> {
	private List<T> cells;
	private int rows;
	private int cols;

	/**
	 * 
	 * Construct a grid with the given dimensions.
	 * 
	 * @param cols
	 * @param rows
	 * @param initElement
	 *            What the cells should initially hold (possibly null)
	 */
	public Grid(int rows, int cols, T initElement) {
		if(cols <= 0 || rows <= 0)
			throw new IllegalArgumentException("number of rows and columns must be positive");

		this.rows = rows;
		this.cols = cols;
		cells = new ArrayList<>(rows * cols);
		for(int i = 0; i<rows*cols; i++) {
			cells.add(initElement);
		}
	}

	
	@Override
	public int numRows() {
		return rows;
	}


	@Override
	public int numCols() {
		return cols;
	}


	@Override
	public void set(Location loc, T elem) {
		check(loc);

		cells.set(indexOf(loc), elem);
	}

	/**
	 * Computes the right index in the list from a location in the grid 
	 * @param loc - the location in the grid
	 * @return the index in the list cells
	 */
	private int indexOf(Location loc) {
		return loc.getCol() + loc.getRow()*cols;
	}

	/**
	 * Computes the location corresponding to an index in the list
	 * @param index
	 * @return
	 */
	private Location locationFromIndex(int index) {
		if(index<0 || index > cells.size())
			throw new IndexOutOfBoundsException("index is not a valid index of the board");
		return new Location(index/cols,index%cols);
	}

	@Override
	public T get(Location loc) {
		check(loc);

		return cells.get(indexOf(loc));
	}

	@Override
	public IGrid<T> copy() {
		Grid<T> newGrid = new Grid<>(numRows(), numCols(), null);
		copy(newGrid);
		return newGrid;

	}
	
	protected void copy(IGrid<T> newGrid) {
		for(Location loc : locations())
			newGrid.set(loc,  get(loc));
	}
	
	/**
	 * Checks that a given xy coordinate is within the bounds of the Grid
	 * @param x
	 * @param y
	 * @return
	 */
	public boolean validCoordinate(int x, int y) {
		if(x < 0 || x >= cols || y < 0 || y >= rows)
			return false;
		return true;
	}

	/**
	 * Checks if a given location is within the limits of the grid
	 * @param loc
	 * @return
	 */
	public boolean validLocation(Location loc) {
		return validCoordinate(loc.getCol(), loc.getRow());
	}

	/**
	 * Checks if a given xy coordinate is within the bounds of the Grid.
	 * If not an exception is thrown
	 * @param row
	 * @param col
	 */
	public void check(Location loc) {
		if(!validLocation(loc)) 
			throw new IndexOutOfBoundsException();
	}
	
	@Override
	public boolean contains(Object obj) {
		return this.cells.contains(obj);
	}

	@Override
	public Location locationOf(Object target) {
		int index = this.cells.indexOf(target);
		if(index<0)
			return null;
		else
			return locationFromIndex(index);
	}

	@Override
	public Iterator<T> iterator() {
		return cells.iterator();
	}

	@Override
	public GridLocationIterator locations() {
		return new GridLocationIterator(this);
	}


}
