package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import inf101.v20.sem2.grid.Location;

class PlayerTest {

	public static void testConstructor(String symbol, String name, Player p) {
		assertEquals(name, p.getName());
		assertEquals(symbol, p.getSymbol());
	}

	@Test
	void testisValidName() {
		assertTrue(Player.isValidName("Martin"));
		assertFalse(Player.isValidName(""));
		assertFalse(Player.isValidName(" "));
		assertFalse(Player.isValidName("\n"));
		assertFalse(Player.isValidName("\t"));
	}
	
	@Test
	void testValidateName() {
		String name = "Martin";
		assertEquals(name, Player.validateName(name));
		try {
			Player.validateName("");
		} catch (IllegalArgumentException e) {
			return;
		} catch(Exception e) {
			fail("Should throw an IllegalArgumentException");
		}
	}
	
}
