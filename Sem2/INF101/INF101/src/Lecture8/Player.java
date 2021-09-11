package Lecture8;

import java.util.List;

public class Player implements IPlayer {

	@Override
	public boolean getAnotherCard(List<Card> hand, List<IPlayer> players) {
		if(BlackJack.getValueOf(hand) < 12) {
			return true;
		}
		else {
			return false;
		}
	}

}
