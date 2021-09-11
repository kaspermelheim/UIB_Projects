package Lecture8;

import java.util.List;

public interface IPlayer {

	boolean getAnotherCard(List<Card> hand, List<IPlayer> players);
	
//	List<Card> getHand(BlackJack game);
}
