package inf101.v20.sem2.grid;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LocationTest {

	@Test
	void testGetRowAndCol() {
		Location loc = new Location(3, 7);
		assertEquals(3, loc.getRow());
		assertEquals(7, loc.getCol());
	}

	@Test
	void testEqualsObject() {
		Location loc1 = new Location(3, 5);
		assertEquals(loc1, new Location(3, 5));
		assertNotEquals(loc1, new Location(5, 3));
		assertNotEquals(loc1, new Location(3, 3));
		assertNotEquals(loc1, new Location(5, 5));
		assertNotEquals(loc1, null);
		assertNotEquals(loc1, "Location: 3,5");		
	}

	@Test
	void testToString() {
		Location loc1 = new Location(3, 5);
		assertEquals(loc1.toString(), "Location: 3,5");	
	}

}
