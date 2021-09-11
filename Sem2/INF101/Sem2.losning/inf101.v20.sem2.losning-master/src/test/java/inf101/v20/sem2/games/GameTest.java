package inf101.v20.sem2.games;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.Collections;

import org.junit.jupiter.api.Test;

public class GameTest {

	@Test
	void TwoAICanPlay() {
		playGame(new TicTacToe(getMiniMaxPlayers()));
		playGame(new ConnectFour(getMiniMaxPlayers()));
	}

	@Test
	void TwoRandomCanPlay() {
		playGame(new TicTacToe(getRandomPlayers()));
		playGame(new ConnectFour(getRandomPlayers()));
	}

	@Test
	void AICanBeatRandomTicTacToe() {
		int aiwins =0;
		int randomwins=0;
		for(int i=0; i<100; i++) {
			AbstractGame game = new TicTacToe(getTwoDifferentAI());
			int result = AICanBeatRandom(game);
			if(result == 1)
				aiwins++;
			if(result == -1)
				randomwins++;
		}
		assertTrue(aiwins>5*randomwins,"random won "+randomwins+", ai won "+aiwins);
	}

	@Test
	void AICanBeatRandomFourInRow() {
		int aiwins =0;
		int randomwins=0;
		for(int i=0; i<100; i++) {
			AbstractGame game = new ConnectFour(getTwoDifferentAI());
			int result = AICanBeatRandom(game);
			if(result == 1)
				aiwins++;
			if(result == -1)
				randomwins++;
		}
		assertTrue(aiwins>5*randomwins,"random won "+randomwins+", ai won "+aiwins);
	}

	
	int AICanBeatRandom(AbstractGame game) {
		playGame(game);
		for(Player player : game.players()) {
			if(game.isWinner(player)) {
				if(player instanceof MiniMaxPlayer)
					return 1;
				if(player instanceof RandomPlayer)
					return -1;
			}
		}
		return 0;
	}

	private ArrayList<Player> getMiniMaxPlayers() {
		ArrayList<Player> players = new ArrayList<Player>();
		players.add(new MiniMaxPlayer("X", 3));
		players.add(new MiniMaxPlayer("O", 3));
		return players;
	}

	private ArrayList<Player> getRandomPlayers() {
		ArrayList<Player> players = new ArrayList<Player>();
		players.add(new RandomPlayer("X"));
		players.add(new RandomPlayer("O","Random 2"));
		return players;
	}

	private ArrayList<Player> getTwoDifferentAI() {
		ArrayList<Player> players = new ArrayList<Player>();
		players.add(new MiniMaxPlayer("X", 3));
		players.add(new RandomPlayer("O"));
		Collections.shuffle(players);
		return players;
	}

	void playGame(AbstractGame game) {
		game.start();
		assertTrue(game.gameOver());		
	}

}
