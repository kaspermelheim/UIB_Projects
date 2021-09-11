package inf101.v20.sem2.GUI;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

import inf101.v20.sem2.games.ConnectFour;
import inf101.v20.sem2.games.AbstractGame;
import inf101.v20.sem2.games.MiniMaxPlayer;
import inf101.v20.sem2.games.Player;
import inf101.v20.sem2.games.TicTacToe;

/**
 * This class combines two buttons with a MNKGameGUI in one JFrame
 * The buttons are used to select type of game to play.
 *  
 * @author Anna Eilertsen - anna.eilertsen@uib.no 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class GameGUI implements ActionListener{

	private JButton playConnectFourButton; //Button to start new 4 in row game
	private JButton playTicTacToeButton; //Button to start new TicTacToe game
	private JFrame frame;
	private MNKGameGUI gameBoard;

	public GameGUI(MNKGameGUI gameBoard) {
		this.gameBoard = gameBoard;
		JPanel buttons = createButtonPanel();
		
		//make new main window for the game
		frame = new JFrame(); 
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.add(buttons, BorderLayout.SOUTH);
		
		drawGameBoard();
	}

	public static void main(String[] args) {
		AbstractGame game = new TicTacToe(GameGUI.getPlayers());
		MNKGameGUI gameGUI = new MNKGameGUI(game);
		new GameGUI(gameGUI);
		game.start();
	}

	/**
	 * Draws the gameBoard on the JFrame 
	 * and refreshes the rest of the graphics
	 */
	private void drawGameBoard() {
		//add the clickable grid panel
		frame.add("Center", gameBoard);
		frame.pack();
		frame.setVisible(true);
		//update to reflect the state of the game
		gameBoard.updateUI();
	}

	/**
	 * Helper method that creates the button panel 
	 */
	private JPanel createButtonPanel() {
		playTicTacToeButton = new JButton();
		playTicTacToeButton.addActionListener(this);
		playTicTacToeButton.setText("Tic-Tac-Toe");

		playConnectFourButton = new JButton();
		playConnectFourButton.addActionListener(this);
		playConnectFourButton.setText("Connect Four");
		
		JPanel buttons = new JPanel();
		buttons.setLayout(new BorderLayout());
		buttons.add(playConnectFourButton, BorderLayout.WEST);
		buttons.add(playTicTacToeButton, BorderLayout.EAST);
		return buttons;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
	 * Called whenever a button is pressed  
	 */
	@Override
	public void actionPerformed(ActionEvent e) {
		Iterable<Player> players = getPlayers();
		frame.remove(gameBoard);
		if(e.getSource() == playConnectFourButton) {
			this.gameBoard = new MNKGameGUI(new ConnectFour(players));
		}
		if(e.getSource() == playTicTacToeButton) {
			this.gameBoard = new MNKGameGUI(new TicTacToe(players));
		}
		
		drawGameBoard();
	}
	
	/**
	 * Generates a list of players based on user input
	 * 
	 * @return an Iterable of 2 Players
	 */
	public static Iterable<Player> getPlayers() {
		ArrayList<Player> players = new ArrayList<Player>();
		//add player1
		players.add(new GuiPlayer(AbstractGame.piece1));
		//add player2
		if(promptMultiplayer()) {
			players.add(new GuiPlayer(AbstractGame.piece2));
		}else {
			//make AI
			//TODO: prompt for level of intelligence in AI player
			players.add(new MiniMaxPlayer(AbstractGame.piece2, 5));
		}
		
		
		return players;
	}

	/**
	 * Helper method that prompts for multiplayer or not  
	 * @return true if multiplayer is selected, false otherwise
	 */
	private static boolean promptMultiplayer() {
		Object[] possibilities = {"Multiplayer", "Single Player (against AI)"};
		String s = (String)JOptionPane.showInputDialog(
				null,
				"Welcome:\n"
						+ "Select one or two players",
						"MKGame StartUp",
						JOptionPane.PLAIN_MESSAGE,
						null,
						possibilities,
						null);

		//If a string was returned, say so.
		if ((s != null) && (s.length() > 0)) {
			System.out.println("Received " + s);
		}
		return s.equals(possibilities[0]);
	}
}
