package inf101.v20.sem2.games;

import inf101.v20.sem2.grid.Location;

/**
 * This AI is based on an algorithm that is not curriculum for INF101, but maybe for INF102.
 * Since many of the students had tried implementing such an AI I have included one in this solution.
 * But such a level of AI is not expected at the level of INF101. 
 * 
 * This player will work both for TicTacToe and for FourInARow
 * 
 * This player uses a minimax strategy to search for the best move.
 * That means that it tries all possible moves and gives a score to each move.
 * The score is given by calling the method recursively for the other player to
 * make the move that is best for him.
 * We assume that what is best for you is worst for your opponent, 
 * otherwise this strategy will not work.
 * 
 * In this case we give score 1 for win, score for draw and score -1 for loosing.
 * Note that the sum of the scores for both players always is 0.
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class MiniMaxPlayer extends AbstractPlayer {

	int depth; //defines how many steps ahead the search should continue;
	
	public MiniMaxPlayer(String piece, int level) {
		super(piece, "MiniMax");
		depth = level;
	}

	@Override
	public Location getMove(IGame game) {
		Strategy best = bestMove(game,depth);
		return best.move;
	}

	/**
	 * Chooses the move that maximizes the players score
	 * @param game
	 * @param depth
	 * @return
	 */
	private Strategy bestMove(IGame game,int depth){
		Strategy best = null;
		
		//try each possible strategy
		for (Location loc : game.possibleMoves()) {
			//make a copy of the game and try the move 
			IGame newGame = game.copy();
			newGame.makeMove(loc); //note that this changes the current player in the copy but not the real game
			int score = 0;
			if(newGame.gameOver() || depth==1) { //No more moves can be made
				score = score(newGame,game.getCurrentPlayer());
			}else {
				//call recursively such that the opponent makes the move that is best for him
				//change the sign since this is the score of the best move for opponent
				score = -bestMove(newGame, depth-1).score;
			}
			
			//keep the best Strategy
			if(best==null) {
				best = new Strategy(loc,score);
			}else {
				if(score>best.score)
					best = new Strategy(loc, score);
			}
		}
		if(best == null)
			System.err.println("This should not happen!");
		return best;

	}
	
	/**
	 * Computes a score for the player p in the current game
	 * to be used when choosing the best move.
	 * @param game
	 * @param p
	 * @return
	 */
	private int score(IGame game, Player p) {
		if(game.isWinner(p)) {
			return 1;
		}
		if(game.isWinner(getOpponent(game, p))) {
			return -1;
		}
		return 0;
	}



	/**
	 * @param player - the current player
	 * @param game - the game
	 * @return An opponent in the game, this is only uniquely defined in a 2 player game
	 */
	public static Player getOpponent(IGame game, Player player) {
		for(Player p : game.players()) {
			if(p != player) {
				return p;
			}
		}
		throw new IllegalStateException("There must be 2 different players in the game");
	}


}

/**
 * A inner class only to be used by MiniMax player
 * This class keeps track of a move and a score associated with that move
 * 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
class Strategy{
	Location move;
	int score;

	public Strategy(Location move, int score) {
		this.move = move;
		this.score = score;
	}
}



