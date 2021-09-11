package inf101.v20.sem2.grid;

import java.util.Arrays;
import java.util.List;

/**
 * This class represents the 8 different directions 
 * (plus the direction of no movement) in in a grid 
 * which one can move by changing either x or y coordinate by at most 1
 */
public enum GridDirection {
	EAST(1, 0), 
	NORTH(0, -1), 
	WEST(-1, 0), 
	SOUTH(0, 1), //
	NORTHEAST(1, -1), 
	NORTHWEST(-1, -1), 
	SOUTHWEST(-1, 1), 
	SOUTHEAST(1, 1), //
	CENTER(0, 0);

	/**
	 * The four cardinal directions: {@link #NORTH}, {@link #SOUTH}, {@link #EAST},
	 * {@link #WEST}.
	 */
	public static final List<GridDirection> FOUR_DIRECTIONS = Arrays.asList(EAST, NORTH, WEST, SOUTH);
	/**
	 * The eight cardinal and intercardinal directions: {@link #NORTH},
	 * {@link #SOUTH}, {@link #EAST}, {@link #WEST}, {@link #NORTHWEST},
	 * {@link #NORTHEAST}, {@link #SOUTHWEST}, {@link #SOUTHEAST}.
	 */
	public static final List<GridDirection> EIGHT_DIRECTIONS = Arrays.asList(EAST, NORTHEAST, NORTH, NORTHWEST, WEST,
			SOUTHWEST, SOUTH, SOUTHEAST);
	/**
	 * The eight cardinal and intercardinal directions ({@link #EIGHT_DIRECTIONS}),
	 * plus {@link #CENTER}.
	 */
	public static final List<GridDirection> NINE_DIRECTIONS = Arrays.asList(EAST, NORTHEAST, NORTH, NORTHWEST, WEST,
			SOUTHWEST, SOUTH, SOUTHEAST, CENTER);

	private final int dx;
	private final int dy;

	private GridDirection(int dx, int dy) {
		this.dx = dx;
		this.dy = dy;
	}

	/**
	 * @return The change to your X-coordinate if you were to move one step in this
	 *         direction
	 */
	public int getDx() {
		return dx;
	}

	/**
	 * @return The change to your Y-coordinate if you were to move one step in this
	 *         direction
	 */
	public int getDy() {
		return dy;
	}
}
