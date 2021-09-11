package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Random;
import java.util.Scanner;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.terminal.ConsolePlayer;

class GameBoardTest {

	public final static Player player1 = new ConsolePlayer("X", "Martin");
	public final static Player player2 = new ConsolePlayer("O", "Laura");
	GameBoard board;
	public final Random rand = new Random();
	
	@BeforeEach
	private void createGame() {
		board = new GameBoard(4,5);
	}
	
	@Test
	void testCanConstruct() {
		createGame();
		try {
			board = new GameBoard(5,-3);
		} catch (Exception e) {
			assertTrue(e instanceof IllegalArgumentException,"Wrong type of exception is thrown");
			return;
		}
		fail("No Exception thrown on illegal input");
	}

	@Test
	void testSetAndGet() {
		Location loc = new Location(3,3);
		board.set(loc, player1);
		assertEquals(player1, board.get(loc));
		board.set(new Location(board.numRows()-1,board.numCols()-1), player1);
		boolean getException = false;
		try {
			board.set(new Location(3,board.numCols()), player1);
		} catch (Exception e) {
			assertTrue(e instanceof IndexOutOfBoundsException);
			getException = true;
		}
		if(!getException)
			fail("should get IndexOutOfBoundsException");
		getException = false;
		try {
			board.set(new Location(3,3), player2);
		} catch (Exception e) {
			assertTrue(e instanceof IllegalArgumentException,e.getMessage());
			getException = true;
		}
		if(!getException)
			fail("should get IllegalArgumentException");
		
	}

	@Test
	void testIsEmpty() {
		board.set(new Location(3,3), player1);
		assertTrue(board.isEmpty(new Location(2,2)));
		assertFalse(board.isEmpty(new Location(3,3)));
		
	}

	@Test
	void testCountPlayerDiagonalUp() {
		assertEquals(0,board.countNumInRow(player1));
		board.set(new Location(1, 1), player1);
		board.set(new Location(2, 2), player1);
		board.set(new Location(3, 3), player1);
		assertEquals(3,board.countNumInRow(player1));
	}

	@Test
	void testCountPlayerDiagonalDown() {
		assertEquals(0,board.countNumInRow(player1));
		board.set(new Location(1, 3), player1);
		board.set(new Location(2, 2), player1);
		board.set(new Location(3, 1), player1);
		assertEquals(3,board.countNumInRow(player1));
	}

	@Test
	void testCountPlayerHorizontal() {
		assertEquals(0,board.countNumInRow(player1));
		for(int col : board.colIndices())
			board.set(new Location(3, col), player1);
		assertEquals(board.numCols(),board.countNumInRow(player1));
		assertEquals(0,board.countNumInRow(player2));
	}

	@Test
	void testCountPlayerVertical() {
		assertEquals(0,board.countNumInRow(player1));
		for(int row : board.rowIndices())
			board.set(new Location(row, 3), player1);
		assertEquals(board.numRows(),board.countNumInRow(player1));
		assertEquals(0,board.countNumInRow(player2));
	}

	@Test
	void testIsFull() {
		int num = board.numRows()*board.numCols();
		
		for(Location loc : board.locations()) {
			board.set(loc, getRandomPlayer());
			num--;
			if(num>0) {
				assertFalse(board.isFull(),"Not full, there is still "+num +" pieces to place.");
			}
		}
		assertTrue(board.isFull());
	}
	
	private void fillBoard() {
		for(Location loc : board.locations()) {
			board.set(loc, getRandomPlayer());
		}
	}

	private Player getRandomPlayer() {
		if(rand.nextBoolean())
			return player1;
		else
			return player2;
	}

	@Test
	void testGetHeightAndWidth() {
		int rows = 4;
		int cols = 5;
		board = new GameBoard(rows,cols);
		assertEquals(rows,board.numRows());
		assertEquals(cols,board.numCols());
	}
	
	@Test
	void testToString() {
		fillBoard();
		Scanner sc = new Scanner(board.toString());
		int numLines=0;
		while(sc.hasNextLine()) {
			String line = sc.nextLine();
			int numPlayers=0;
			for(char c : line.toCharArray()) {
				if(c==player1.getSymbol().charAt(0) || c==player2.getSymbol().charAt(0)) {
					numPlayers++;
				}
			}
			if(numPlayers>0) {
				assertEquals(board.numCols(), numPlayers);
				numLines++;
			}
		}
		sc.close();
		assertEquals(board.numRows(), numLines);
	}
	
	@Test
	void testCopy() {
		fillBoard();
		GameBoard newBoard = board.copy();
		for(Location loc : board.locations()) {
			assertEquals(board.get(loc), newBoard.get(loc));
		}
			
	}

}
