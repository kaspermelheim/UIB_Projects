package inf101.v20.sem2.terminal;

import static inf101.v20.sem2.terminal.TerminalInput.*;

import java.util.Scanner;

import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.games.AbstractPlayer;
import inf101.v20.sem2.games.ConnectFour;
import inf101.v20.sem2.games.IGame;

/**
 * This Player enables the user to play the game by using the keyboard.
 * There is in reality two different players here, 
 * one for TicTacToe and one for FourInARow
 * If you check out the makeMove method it is only an if else choosing between the two types
 * 
 * I thought still it was good to keep all this code in one class as then
 * all players can be used in both games.
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class ConsolePlayer extends AbstractPlayer {

	/**
	 * The Scanner used to read from the terminal.
	 * We use one single static Scanner for all players 
	 * rather than starting a new Scanner as all ConsolePlayers
	 * on the same computer will be typing on the same keyboard.
	 * If this game were to be played over network this might need to change.
	 */
	static Scanner sc = new Scanner(System.in);
	
	/**
	 * Creates new console player
	 * @param symbol
	 * @param name
	 */
	public ConsolePlayer(String symbol, String name) {
		super(symbol,name);
	}
	
	/**
	 * Creates new Console player by reading name from Console
	 * @param symbol
	 */
	public ConsolePlayer(String symbol) {
		super(symbol,"player");
		name = readPlayerName(symbol);
	}


	/**
	 * Reads in a move from terminal
	 */
	@Override
	public Location getMove(IGame game) {
		game.getGameBoard().printBoard();
		if(game instanceof ConnectFour) {
			return getColumn((ConnectFour) game);
		}
		else
			return getLocation(game);
	}
	
	/**
	 * Reads input for the FourInARow game
	 */
	private Location getColumn(ConnectFour game) {
		System.out.println("Player "+this.toString()+" type [Col] to make a move.");
		boolean done = false;
		int col = 0;
		while(!done) {
			col = readInt(sc,"column");
			if(game.canPlace(game.drop(col), this)) {
				done = true;
			}
			else {
				System.out.println("Can not place there. Try again");
			}
		}
		return game.drop(col);
	}

	/**
	 * Reads in a player name, only requirement is that name is not empty
	 * @param sc
	 */
	public static String readPlayerName(String symbol) {
		System.out.println("Player "+symbol+" type your name:");
		return readName(sc,"Name");
	}

	/**
	 * Can read input for any game where input is an x,y location
	 * @param game
	 * @return
	 */
	private Location getLocation(IGame game){
		System.out.println("Player "+this.toString()+" type [Row] [Col] to make a move.");
		boolean done = false;
		int row = 0;
		int col = 0;
		while(!done) {
			row = readInt(sc,"row");
			col = readInt(sc,"column");
			if(game.canPlace(new Location(row, col), this)) {
				done = true;
			}
			else {
				System.out.println("Can not place there. Try again");
			}
		}
		return new Location(row, col);
	}
}
