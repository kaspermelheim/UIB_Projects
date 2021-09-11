package inf101.v20.sem2.terminal;

import java.util.ArrayList;
import java.util.Scanner;

import inf101.v20.sem2.games.ConnectFour;
import inf101.v20.sem2.games.IGame;
import inf101.v20.sem2.games.MiniMaxPlayer;
import inf101.v20.sem2.games.Player;
import inf101.v20.sem2.games.TicTacToe;

public class TerminalMenu {

	public TerminalMenu() {
		// TODO Auto-generated constructor stub
	}
	
	public static void main(String[] args) {
		System.out.println("Player 1, what is your name?");
		ArrayList<Player> players = new ArrayList<Player>();
		players.add(new ConsolePlayer("X"));
		System.out.println("(1) Two players or \n(2) play against computer?");
		int multiplayerChoice = TerminalInput.readInt(new Scanner(System.in), "game id");
		switch (multiplayerChoice) {
		case 1:
			players.add(new ConsolePlayer("O"));
			break;
		case 2:
			players.add(new MiniMaxPlayer("O", 5));
			break;
		default:
			throw new IllegalArgumentException("Unexpected value: " + multiplayerChoice);
		}
		
		System.out.println("Which game do you wish to play?");
		System.out.println("Press 1 for TicTacToe and 2 for Connect 4");
		int choice = TerminalInput.readInt(new Scanner(System.in), "game id");
		IGame game;
		switch (choice) {
		case 1:
			game = new TicTacToe(players);
			break;

		case 2:
			game = new ConnectFour(players);
			break;
		default:
			throw new IllegalArgumentException("Unexpected value: " + choice);
		}
		game.start();
	}
}
