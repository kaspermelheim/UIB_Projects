package inf101.v20.sem2.games;

/**
 * This game is played on a n by n board, normally n = 3.
 * The goal is to get 3 in a row.
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class TicTacToe extends AbstractGame {
	/**
	 * Constructor for normal 3x3 TicTacToe
	 */
	public TicTacToe() {
		this(3);
	}

	/**
	 * Constructor for general nxn TicTacToe
	 * @param n the size of the board
	 */
	public TicTacToe(int n) {
		super(new GameBoard(n,n));
	}

	public TicTacToe(Iterable<Player> players) {
		this(3,players);
	}

	public TicTacToe(int n, Iterable<Player> players) {
		this(new GameBoard(n,n),players);
	}

	public TicTacToe(GameBoard board, Iterable<Player> players) {
		super(board,players);
	}

	@Override
	public boolean isWinner(Player player) {
		return board.countNumInRow(player)==board.numRows();
	}

	@Override
	public String getName() {
		return "TicTacToe";
	}

	@Override
	public TicTacToe copy() {
		TicTacToe newGame = new TicTacToe(board.copy(),players());
		newGame.setPlayer(getCurrentPlayer());
		return newGame;
	}
}
