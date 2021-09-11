package inf101.v20.sem2.games;

import java.util.List;

import inf101.v20.sem2.grid.Location;

/**
 * This Interface is used to describe what is needed for playing a Game
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public interface IGame {

	/**
	 * This method starts the game
	 */
	public void start();
	
	/**
	 * Lists the players in this game.
	 * @return
	 */
	public Iterable<Player> players();

	/**
	 * @return The name of the game
	 */
	public String getName();

	/**
	 * The game has rules for where the players can place.
	 * In both TicTacToe and Connect4 it does not matter who the player is, but it might in other games.
	 * 
	 * This is both used to verify that the move a Player returns is valid
	 * and for the AI to know where it can place.
	 * 
	 * @param loc - where to place
	 * @param player - who wants to place
	 * @return true if it is a valid move, false otherwise.
	 */
	public boolean canPlace(Location loc, Player player);
		
	/**
	 * Only if the game supports a GUI mode.
	 * In GUI mode the game is driven by mouse clicks and not a game loop.
	 * This method restarts the game when a mouse click is detected
	 * @param loc - The location which was clicked
	 */
	public void makeGuiMove(Location loc);

	/**
	 * Some methods needs to access information about the game board 
	 * but only have a reference to the game.
	 * @return the game board
	 */
	public GameBoard getGameBoard();

	/**
	 * @return The name of the current player
	 */
	public Player getCurrentPlayer();

	/**
	 * Will find all the possible moves the current player can make
	 * This is mainly for the AI to more easily select a move.
	 * Did not need to be in the Interface, but it might be a handy method to have.
	 * 
	 * @return list of all possible Locations for next move
	 */
	public List<Location> possibleMoves();
	
	/**
	 * Will find all the possible moves the given player can make
	 * @return
	 */
	public List<Location> possibleMoves(Player p);


	/**
	 * Checks the win conditions of the game
	 * @param player
	 * @return
	 */
	public boolean isWinner(Player p);

	/**
	 * Checks if the game is a draw
	 * @return true if the game is a draw, false otherwise
	 */
	public boolean isDraw();

	/**
	 * Creates a copy of the game.
	 * 
	 * This method is needed for the AI players to try out different moves without
	 * actually changing the game.
	 * 
	 * @return a copy of the game.
	 */
	public IGame copy();

	/**
	 * This method is used for testing and by the AI which simulates
	 * several moves ahead to find the best move.
	 * @param loc
	 * @return
	 */
	public boolean makeMove(Location loc);

	/**
	 * This method
	 * @return
	 */
	public boolean gameOver();
}
