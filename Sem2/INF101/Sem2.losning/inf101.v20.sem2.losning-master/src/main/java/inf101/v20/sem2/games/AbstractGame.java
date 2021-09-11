package inf101.v20.sem2.games;

import java.util.ArrayList;
import java.util.List;

import inf101.v20.sem2.GUI.GuiPlayer;
import inf101.v20.sem2.GUI.MNKGameGUI;
import inf101.v20.sem2.grid.Location;

/**
 * A game consists of a GameBoard, and 2 players which each has a piece.
 * Pieces are then placed on the board until a winning, loosing or draw condition
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public abstract class AbstractGame implements IGame {

	GameBoard board;
	PlayerList players;
	MNKGameGUI gui = null;
	public static final String piece1 = "X";
	public static final String piece2 = "O";

	
	//**********   CONSTRUCTORS   **********//
	/**
	 * Constructor
	 * @param board - The board to play on
	 * @param players - The players to play the game
	 */
	public AbstractGame(GameBoard board, Iterable<Player> players) {
		this(board);
		for(Player p: players) {
			addPlayer(p);
		}
	}

	/**
	 * Constructor which creates a game without players
	 * @param board
	 */
	public AbstractGame(GameBoard board) {
		players = new PlayerList();
		this.board = board;
	}
	
	//**********   PLAYER METHODS   **********//

	/**
	 * @return an Iterable over players in this game
	 */
	public Iterable<Player> players(){
		return players;
	}

	public void setGui(MNKGameGUI gui){
		this.gui = gui;
	}
	
	/**
	 * Adds a player to this game, each player must select a Piece before join
	 * @param p
	 */
	public void addPlayer(Player p) {
		
		for(Player player : players())
		{
			if(p.usesSameSymbol(player))
				throw new IllegalArgumentException("Two players "+p+" and " +player+" can not have the same piece");
		}
		players.add(p);
	}

	//**********   GAME LOOP   **********//

	/**
	 * This method starts the game.
	 * and keeps running until the game is over
	 */
	@Override
	public void start() {
		while(!gameOver()) {
			if(currentIsGuiPlayer()) {
				//The current player is a GUI player and we need to wait for
				//the player to click
				stop();
				return;
			}
			doTurn();
		}
		stop();
		printResult();
	}
	
	protected void stop() {
		//nothing needed to do to stop the game in normal mode.
		//Only in GUI mode this is needed.
		if(gui != null) {
			gui.updateUI();
			showMessage(getCurrentPlayer() +" it is your turn.");
		}
	}

	private boolean currentIsGuiPlayer(){
		return (players.currentPlayer() instanceof GuiPlayer);
	}

	/**
	 * This method lets the current player do its turn 
	 * and then advances to next player.
	 * 
	 * If a player makes invalid move let the player try again
	 * 
	 */
	private void doTurn() {
		Player player = players.currentPlayer();
		while(players.currentPlayer()==player) {
			try {
				Location loc = player.getMove(this); //the location current player wants to place on
				makeMove(loc,player);
			} catch (Exception e) {
				System.out.println("Player "+player+" failed to make a move.");
				System.out.println("Try again");				
			}	
		}
	}

	/**
	 * Makes a move, making sure: 
	 * - that the location is valid, 
	 * - that the player is allowed to make a move at the current time
	 * - that the turn moves to next player
	 * @param loc
	 * @param player
	 */
	protected void makeMove(Location loc, Player player) {
		//TODO: test what happens if called with wrong player.
		if(canPlace(loc, player)) {
			board.set(loc, player);
			players.nextPlayer();
		}else {
			throw new IllegalArgumentException("Can not place there");
		}
	}

	/**
	 * Makes a move for the current player
	 * @param loc
	 * @return
	 */
	public boolean makeMove(Location loc) {
		if(gameOver())
			return false;
		try {
			makeMove(loc,players.currentPlayer());
		}catch(IllegalArgumentException e) {
			//invalid move
			return false;
		}
		return true;
	}

	//**********   GAME LOGICS   **********//

	/**
	 * This method describes where on a board the players are allowed to place
	 * In this abstract class any position which is free is allowed
	 * @param loc - The location a player wishes to place in
	 * @param p - the player that wishes to place
	 * @return true if "loc" is a valid move for "p", false otherwise
	 */
	public boolean canPlace(Location loc, Player p) {
		if(!board.validLocation(loc))
			return false;
		return board.isEmpty(loc);
	}


	/**
	 * If the game is over a message is printed 
	 */

	private void printResult() {
		for(Player p : players) {
			if(isWinner(p)) {
				showMessage(p+ " is the winner!");
				return;
			}
		}
		if(gameOver()) {
			showMessage("It is a draw!");
		}else
			showMessage("The game is ongoing!");
	}

	private void showMessage(String message) {
		System.out.println(message);
		if(gui!=null)
			gui.updateMessage(message);		
	}
	/**
	 * Checks if there is a winner in the game
	 * @return
	 */
	protected boolean hasWinner() {
		for(Player p : players) {
			if(isWinner(p))
				return true;
		}
		return false;
	}


	/**
	 * Checks if the game is a draw, a game is a draw when there is no possible move
	 * and no player has won.
	 * @return
	 */
	public boolean isDraw() {
		return board.isFull() && !hasWinner();
	}

	/**
	 * This method checks if the game is over
	 * @return
	 */
	public boolean gameOver() {
		return hasWinner() || isDraw();
	}

	/**
	 * Checks if the given player has any possible moves
	 * @param p
	 * @return
	 */
	public boolean hasPossibleMoves(Player p) {
		return !possibleMoves(p).isEmpty();
	}

	@Override
	public List<Location> possibleMoves(){
		return possibleMoves(players.currentPlayer());
	}
	
	@Override
	public List<Location> possibleMoves(Player p){
		ArrayList<Location> moves = new ArrayList<Location>();
		for(Location loc : board.locations()) {
			if(canPlace(loc, p))
				moves.add(loc);
		}
		return moves;
	}
	
	@Override
	public GameBoard getGameBoard() {
		return board.copy();
	}

	public void printBoard() {
		board.printBoard();
	}

	@Override
	public Player getCurrentPlayer() {
		return players.currentPlayer();
	}

	@Override
	public void makeGuiMove(Location loc) {
		if(!currentIsGuiPlayer())
			return; //Only GuiPlayer may call this method
		if(gameOver()) //can not make more moves after there is a winner
			return;
		makeMove(loc);
		start();
	}
	
	/**
	 * Advances the PlayerList until currentPlayer equals the given player.
	 * This can be used for deciding who should be the first player.
	 * It is also used by the copy method.
	 * 
	 * @param player the player which should be the current player
	 */
	public void setPlayer(Player player) {
		while(player != getCurrentPlayer()) {
			players.nextPlayer();
		}
	}
	
}

