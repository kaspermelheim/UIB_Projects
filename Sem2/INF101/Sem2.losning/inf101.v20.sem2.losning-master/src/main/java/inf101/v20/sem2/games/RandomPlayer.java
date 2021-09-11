package inf101.v20.sem2.games;

import java.util.Collections;
import java.util.List;

import inf101.v20.sem2.grid.Location;

/**
 * This Player chooses a random move among all the possible moves.
 * This player can play any game which implements the possibleMoves() method.
 * 
 * If a game where no possible moves exist is given, the player will throw an Exception
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class RandomPlayer extends AbstractPlayer {

	public RandomPlayer(String piece, String name) {
		super(piece, name);
	}

	public RandomPlayer(String piece) {
		super(piece, "Random player");
	}

	@Override
	public Location getMove(IGame game) {
		List<Location> moves = game.possibleMoves();
		if(moves.isEmpty())
			throw new IllegalStateException("No possible moves to choose, game should have ended!");
		Collections.shuffle(moves);
		return moves.get(0);
	}
}
