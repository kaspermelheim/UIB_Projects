package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.terminal.ConsolePlayer;

class TicTacToeTest {

	public final static Player player1 = new ConsolePlayer("X", "Martin");
	public final static Player player2 = new ConsolePlayer("O", "Laura");
	public TicTacToe tictactoe;

	@BeforeEach
	void initGame() {
		tictactoe = makeGame();
	}

	public static TicTacToe makeGame() {
		TicTacToe tictactoe = new TicTacToe();
		tictactoe.addPlayer(player1);
		tictactoe.addPlayer(player2);
		return tictactoe;
	}
	
	void makedraw() {
		tictactoe.makeMove(new Location(1,1));
		tictactoe.makeMove(new Location(0,0));
		tictactoe.makeMove(new Location(0,1));
		tictactoe.makeMove(new Location(2,1));
		tictactoe.makeMove(new Location(2,0));
		tictactoe.makeMove(new Location(0,2));
		tictactoe.makeMove(new Location(1,2));
		tictactoe.makeMove(new Location(1,0));
		tictactoe.makeMove(new Location(2,2));
	}

	void makeplayer1Win() { //horizontal win
		tictactoe.makeMove(new Location(1,1));
		tictactoe.makeMove(new Location(1,0));
		tictactoe.makeMove(new Location(0,0));
		tictactoe.makeMove(new Location(2,2));
		tictactoe.makeMove(new Location(0,2));
		tictactoe.makeMove(new Location(2,0));
		tictactoe.makeMove(new Location(0,1));
	}

	void makeplayer2Win() { //vertical win
		tictactoe.makeMove(new Location(0,1));
		tictactoe.makeMove(new Location(1,1));
		tictactoe.makeMove(new Location(2,1));
		tictactoe.makeMove(new Location(0,2));
		tictactoe.makeMove(new Location(2,0));
		tictactoe.makeMove(new Location(2,2));
		tictactoe.makeMove(new Location(0,0));
		tictactoe.makeMove(new Location(1,2));
	}

	@Test
	void testIsWinnerWithDraw() {
		makedraw();
		assertFalse(tictactoe.isWinner(player1));
		assertFalse(tictactoe.isWinner(player2));
	}

	@Test
	void testIsWinnerWithPlayer1() {
		makeplayer1Win();
		assertTrue(tictactoe.isWinner(player1));
		assertFalse(tictactoe.isWinner(player2));
	}

	@Test
	void testIsWinnerWithPlayer2() {
		makeplayer2Win();
		assertFalse(tictactoe.isWinner(player1));
		assertTrue(tictactoe.isWinner(player2));
	}

	@Test
	void testCanPlace() {
		for(Location loc : tictactoe.board.locations()) {
			if(!tictactoe.gameOver()) {
				assertTrue(tictactoe.canPlace(loc, player1));
				assertTrue(tictactoe.canPlace(loc, player2));
				tictactoe.makeMove(loc);
				assertFalse(tictactoe.canPlace(loc, player1));
				assertFalse(tictactoe.canPlace(loc, player2));
			}
		
		}
		assertFalse(tictactoe.canPlace(new Location(1, 3),player1));
		assertFalse(tictactoe.canPlace(new Location(3, 2),player2));
		assertFalse(tictactoe.canPlace(new Location(-1, 1),player2));
		assertFalse(tictactoe.canPlace(new Location(0, -1),player1));
	}

	@Test
	void testHasWinnerWithDraw() {
		makedraw();
		assertFalse(tictactoe.hasWinner());
	}

	@Test
	void testHasWinnerWithPlayer1() {
		makeplayer1Win();
		assertTrue(tictactoe.hasWinner());
	}

	@Test
	void testHasWinnerWithPlayer2() {
		makeplayer2Win();
		assertTrue(tictactoe.hasWinner());
	}

	@Test
	void testIsDraw() {
		makedraw();
		assertTrue(tictactoe.isDraw());
	}

	@Test
	void testGameOver() {
		makedraw();
		assertTrue(tictactoe.gameOver());
	}

	@Test
	void testHasPossibleMoves() {
		makedraw();
		assertFalse(tictactoe.hasPossibleMoves(player1));
		assertFalse(tictactoe.hasPossibleMoves(player2));
	}

}
