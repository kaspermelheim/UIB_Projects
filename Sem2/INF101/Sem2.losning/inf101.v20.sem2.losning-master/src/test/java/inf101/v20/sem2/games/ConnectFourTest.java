package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Random;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.terminal.ConsolePlayer;

class ConnectFourTest {

	public final static Player player1 = new ConsolePlayer("X", "Martin");
	public final static Player player2 = new ConsolePlayer("O", "Laura");
	public ConnectFour game;
	public final Random rand = new Random();

	@BeforeEach
	void initGame() {
		game = makeGame();
	}

	public static ConnectFour makeGame() {
		ConnectFour game = new ConnectFour();
		game.addPlayer(player1);
		game.addPlayer(player2);
		return game;
	}
	
	public int rows() {
		return game.getGameBoard().numRows();
	}

	public int cols() {
		return game.getGameBoard().numCols();
	}

	private void fillBoard() {
		for(Location loc : game.getGameBoard().locations()) {
			game.makeMove(game.drop(loc), getRandomPlayer());
		}
	}

	private Player getRandomPlayer() {
		if(rand.nextBoolean())
			return player1;
		else
			return player2;
	}

	@Test
	void testCanPlace() {
		assertTrue(game.canPlace(new Location(rows()-1,0), player1));
		assertFalse(game.canPlace(new Location(rows(),0), player1));
		assertFalse(game.canPlace(new Location(rows()-2,0), player1));
	}

	@Test
	void testGetName() {
		assertTrue(!game.getName().isBlank());
	}

	@Test
	void testCopy() {
		AbstractGame newGame = game.copy();
		for(Location loc : game.getGameBoard().locations()) {
			assertTrue(game.getGameBoard().get(loc) == newGame.getGameBoard().get(loc));			
		}
		Location loc = new Location(rows()-1,0);
		game.makeMove(loc);
		assertFalse(game.getGameBoard().get(loc) == newGame.getGameBoard().get(loc));
		assertFalse(game.getCurrentPlayer() == newGame.getCurrentPlayer());
	}

	@Test
	void testIsWinner() {
		game.makeMove(new Location(5, 0),player2);
		game.makeMove(new Location(5, 1),player2);
		game.makeMove(new Location(5, 2),player2);
		game.makeMove(new Location(5, 3),player2);
		assertTrue(game.isWinner(player2));
		assertFalse(game.isWinner(player1));
	}

	@Test
	void testIsWinnerLongHorisontal() {
		game.makeMove(game.drop(1));
		game.makeMove(game.drop(1));
		game.makeMove(game.drop(2));
		game.makeMove(game.drop(2));
		game.makeMove(game.drop(4));
		game.makeMove(game.drop(4));
		game.makeMove(game.drop(5));
		game.makeMove(game.drop(5));
		game.makeMove(game.drop(3));
		assertTrue(game.isWinner(player1));
		assertFalse(game.isWinner(player2));
	}

	@Test
	void testDrop() {
		for(Location loc : game.getGameBoard().locations()) {
			Location toPlace = game.drop(loc);
			assertNotEquals(null, toPlace,"Drop method should not return null");
			assertTrue(game.canPlace(toPlace,player1));
		}
	}

	@Test
	void testDropColumn() {
		for(int i=0;i<3;i++) {
			game.makeMove(game.drop(3));
			game.makeMove(game.drop(4));
		}
		assertFalse(game.isWinner(player1));
		assertFalse(game.isWinner(player2));
		game.makeMove(game.drop(3));
		assertTrue(game.isWinner(player1));
	}

	@Test
	void testHasWinner() {
		for(int i=0; i<100; i++) {
			initGame();
			fillBoard();
			assertEquals(game.isWinner(player1) || game.isWinner(player2), game.hasWinner());
			assertEquals(game.hasWinner() || game.isDraw(),game.gameOver());
		}
	}

	@Test
	void testPossibleMovesPlayer() {
		assertEquals(cols(), game.possibleMoves().size());
	}

	@Test
	void testGetCurrentPlayer() {
		assertEquals(player1, game.getCurrentPlayer());
		game.players.nextPlayer();
		assertEquals(player2, game.getCurrentPlayer());
		game.players.nextPlayer();
		assertEquals(player1, game.getCurrentPlayer());
	}

	@Test
	void testSetPlayer() {
		assertEquals(player1, game.getCurrentPlayer());
		game.setPlayer(player2);
		assertEquals(player2, game.getCurrentPlayer());
		game.setPlayer(player2);
	}

}
