package inf101.v20.sem2.GUI;

import javax.swing.JOptionPane;

import inf101.v20.sem2.grid.Location;
import inf101.v20.sem2.games.AbstractPlayer;
import inf101.v20.sem2.games.IGame;
import inf101.v20.sem2.games.Player;

/**
 * This Player should be used if one wants input from GUI.
 * The game loop will stop when reaching an instance of GuiPlayer 
 * and when a mouse click is detected the game loop will resume.
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class GuiPlayer extends AbstractPlayer {

	public GuiPlayer(String piece, String name) {
		super(piece, name);
	}

	public GuiPlayer(String piece) {
		super(piece, readPlayerName(piece));
	}

	@Override
	public Location getMove(IGame game) {
		throw new IllegalStateException("This method should not be called.");
	}
	
	/**
	 * Asks player to type in name in a GUI pop up
	 * @param symbol - The symbol representing this player
	 * @return the name chosen by the player 
	 */
	public static String readPlayerName(String symbol) {
		String name = null; 
		while(!Player.isValidName(name)) {
			name = JOptionPane.showInputDialog("Player "+symbol+". Type in your name.");
		}
		return name;
	}
}
