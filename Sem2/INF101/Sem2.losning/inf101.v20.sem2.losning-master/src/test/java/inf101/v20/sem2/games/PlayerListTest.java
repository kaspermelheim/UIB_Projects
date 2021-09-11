package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Random;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import inf101.v20.sem2.terminal.ConsolePlayer;

class PlayerListTest {

	public final static Player player1 = new ConsolePlayer("X", "Martin");
	public final static Player player2 = new ConsolePlayer("O", "Laura");
	PlayerList players;
	Random r = new Random();
	
	@BeforeEach
	void createList() {
		players = new PlayerList();
		players.add(player1);
		players.add(player2);
	}
	
	@Test
	void testConstructor() {
		PlayerList players = new PlayerList();
		assertEquals(0, players.size());
	}

	@Test
	void testCurrentPlayer() {
		assertEquals(player1, players.currentPlayer());
		//consecutive calls to current player should not change the current player
		assertEquals(player1, players.currentPlayer());
	}

	@Test
	void testNextPlayer() {
		for(int i=1; i<100; i++) {
			if(i%2==1)
				assertEquals(player1, players.currentPlayer());
			else
				assertEquals(player2, players.currentPlayer());
			players.nextPlayer();
		}
	}

	@Test
	void testRemoveInt() {
		players.nextPlayer();
		assertEquals(player2, players.currentPlayer());
		assertEquals(player1,players.remove(0));
		assertEquals(player2, players.currentPlayer());
	}

	@Test
	void testRemoveIntCurrent() {
		for(int i=1; i<100; i++) {
			createList();
			testRemoveInt(r.nextInt(100), true);
		}
	}
	@Test
	void testRemoveOtherInt() {
		for(int i=1; i<100; i++) {
			createList();
			testRemoveInt(r.nextInt(100), false);
		}
	}
	
	private void advancePlayer(int n) {
		for(int i=0; i<n; i++) {
			players.nextPlayer();
		}		
	}
	
	private Player other(Player p) {
		if(p==player1) return player2;
		if(p==player2) return player1;
		throw new IllegalStateException("Unexpected player as input");
	}
	
	void testRemoveInt(int n, boolean removeCurrent) {
		advancePlayer(n);
		Player cur = players.currentPlayer();
		if(n%2 == 0)
			assertEquals(player1, cur);
		else
			assertEquals(player2, cur);
		
		if(removeCurrent) {
			assertEquals(cur,players.remove(n%2));
			assertEquals(other(cur),players.currentPlayer());
		} else {
			assertNotEquals(cur, players.remove((n+1)%2));
			assertEquals(cur, players.currentPlayer());
		}
	}

	@Test
	void testRemovePlayer() {
		for(int i=1; i<100; i++) {
			createList();
			testRemove(r.nextInt(100), true);
		}
	}
	@Test
	void testRemoveOtherPlayer() {
		for(int i=1; i<100; i++) {
			createList();
			testRemove(r.nextInt(100), false);
		}
	}

	void testRemove(int n, boolean removeCurrent) {
		advancePlayer(n);
		Player cur = players.currentPlayer();
		if(removeCurrent) {
			assertTrue(players.remove(cur));
			assertEquals(other(cur),players.currentPlayer());
		} else {
			assertNotEquals(cur, players.remove((n+1)%2));
			assertEquals(cur, players.currentPlayer());
		}
		
	}
	
	@Test
	void testRemoveTwice() {
		players.remove(player1);
		assertFalse(players.remove(player1),"Can not remove same player twice");
	}

	@Test
	void testAddAndSize() {
		assertEquals(2, players.size());
		try {
			players.add(new ConsolePlayer(player2.getSymbol(),"Anna"));
		} catch (Exception e) {
			assertTrue(e instanceof IllegalArgumentException);
			return;
		}
		fail("Should get Exception when adding 2 players with same symbol");
	}

	@Test
	void testIterator() {
		Iterator<Player> iter = players.iterator();
		assertEquals(player1, iter.next());
		assertEquals(player2, iter.next());
		assertFalse(iter.hasNext());
		try {
			iter.next();
		} catch (Exception e) {
			assertTrue(e instanceof NoSuchElementException);
		}
	}

}
