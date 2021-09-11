package inf101.v20.sem2.grid;

/**
 * IGrid is a generic grid 
 * 
 * @author Anna Eilertsen - anna.eilertsen@uib.no 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public interface IGrid<T> extends Iterable<T> {

	/**
	 * @return The height of the grid.
	 */
	int numRows();

	/**
	 * @return The width of the grid.
	 */
	int numCols();

	/**
	 * 
	 * Set the contents of the cell in the given Location. 
	 * 
	 * @param loc - The location we want to change.
	 * @param element - The contents the cell is to have.
	 */
	void set(Location loc, T element);

	/**
	 * Get the contents of the cell in the given location.
	 * The location must be within the grid, otherwise an IndecOutOfBoundsException is thrown. 
	 * 
	 * @param loc - The Location we want to get.
	 * @return The element stored in that location.
	 */
	T get(Location loc);

	/**
	 * Make a copy
	 *
	 * @return A shallow copy of the grid, with the same elements
	 */
	IGrid<T> copy();
	
	/**
	 * Searches the grid for an element
	 * @param target - element to find
	 * @return the location at which that element is stored, if no such element is found null is returned.
	 */
	Location locationOf(T target);
	
	/**
	 * Returns an Iterable over all valid locations in this grid
	 * @return
	 */
	public Iterable<Location> locations();
	
	/**
	 * Searches the grid for an element
	 * @param obj - the element to search for
	 * @return true if the element was found, false otherwise
	 */
	public boolean contains(Object obj);

}