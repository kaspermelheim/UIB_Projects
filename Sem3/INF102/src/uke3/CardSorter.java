package uke3;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class CardSorter implements ICardSorter {

	@Override
	public void sortByValue(List<Card> cards) {
		Collections.sort(cards,  new compareByValue());

	}

	@Override
	public void sortBySuit(List<Card> cards) {
		Collections.sort(cards,  new compareByValue());
		Collections.sort(cards, new compareBySuit());

	}
	
	static class compareByValue implements Comparator<Card> {
		public int compare(Card c1, Card c2) {
			return indexOf(Card.names, c1.value) - indexOf(Card.names, c2.value);
		}
	}
	
	static class compareBySuit implements Comparator<Card> {
		public int compare(Card c1, Card c2) {
			return indexOf(Card.suits, c1.suit) - indexOf(Card.suits, c2.suit);
		}
	}
	
	static int indexOf(String[] list, String item) {
		for(int i = 0; i < list.length; i++) {
			if (item.equals(list[i])) return i;
		}
		
		return -1;
	}

}
