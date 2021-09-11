package inf101.v20.sem2.grid;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Random;
import org.junit.jupiter.api.Test;

import inf101.v20.sem2.grid.Grid;
import inf101.v20.sem2.grid.IGrid;
import inf101.v20.sem2.grid.Location;


public class GridTest {
	Random random = new Random();

	@Test
	public void constructTest1() {
		IGrid<String> grid = new Grid<String>(11, 17, "S");
		
		// TODO: sjekk at bredde og høyde faktisk er 11 og 17
		assertEquals(11, grid.numRows());
		assertEquals(17, grid.numCols());
	}
	
	@Test
	public void constructTest2() {
	    assertThrows(IllegalArgumentException.class,()->{new Grid<String>(0, 17, "S");} );
	    assertThrows(IllegalArgumentException.class,()->{new Grid<String>(3, -1, "S");} );
	}

    
	/**
	 * Tests that trying to access outside of the dimensions of the grid throws
	 * an IndexOutOfBoundsException.
	 */
	@Test
	public void outOfBoundsTest() {
		IGrid<String> grid = new Grid<>(10, 10, "S");

		try {
			grid.set(new Location(11, 0), "S");
			fail("Should throw exception");
		} catch (IndexOutOfBoundsException e) {
			;
		}
		try {
			grid.set(new Location(0, 11), "S");
			fail("Should throw exception");
		} catch (IndexOutOfBoundsException e) {
			;
		}
	}

	@Test
	public void setGetTest1() {
		IGrid<String> grid = new Grid<>(100, 100, "S");

		for(Location loc : grid.locations()) {
			String cs = ""+random.nextDouble();
			grid.set(loc, cs);
			assertEquals(cs, grid.get(loc));
		}
	}

	@Test
	public void setGetTest2() {
		IGrid<String> grid = new Grid<>(100, 100, "S");

		for(Location loc : grid.locations()) {
			grid.set(loc, ""+random.nextDouble());
		}

		for(Location loc : grid.locations()) {
			String cs = ""+random.nextDouble();
			grid.set(loc, cs);
			assertEquals(cs, grid.get(loc));
		}
	}

	@Test
	public void copyTest() {
		IGrid<String> grid = new Grid<>(100, 100, "S");

		for(Location loc : grid.locations()) {
			String cs = ""+random.nextDouble();
			grid.set(loc, cs);
		}

		IGrid<String> newGrid = grid.copy();
		for(Location loc : grid.locations()) {
			assertEquals(grid.get(loc), newGrid.get(loc));
		}
	}
	
	@Test
	public void containsTest() {
		IGrid<String> grid = new Grid<>(23, 67, "EMPTY");
		
		String elem = "Element";
		assertFalse(grid.contains(elem));
		Location loc = new Location(12,17);
		grid.set(loc, elem);
		assertTrue(grid.contains(elem));
	}

	@Test
	public void LocationOfTest() {
		IGrid<String> grid = new Grid<>(23, 67, "EMPTY");
		
		String elem = "Element";
	    assertEquals(null,grid.locationOf(elem));
		Location loc = new Location(12,17);
		grid.set(loc, elem);
		assertEquals(loc, grid.locationOf(elem));
		assertTrue(loc.equals(grid.locationOf(elem)));
	}
}
