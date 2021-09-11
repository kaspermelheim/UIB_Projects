package inf101.v20.sem2.games;

import org.junit.jupiter.api.Test;

import inf101.v20.sem2.terminal.ConsolePlayer;

class ConsolePlayerTest {

	@Test
	void testConstructor() {
		String symbol = "X";
		String name = "Martin";
		Player p = new ConsolePlayer(symbol, name);
		PlayerTest.testConstructor(symbol, name, p);
	}

}
