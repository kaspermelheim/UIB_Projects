package uke3;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Collections;
import java.util.List;

import org.junit.jupiter.api.Test;

class CardSorterTest {

	CardSorter cs = new CardSorter();
	
	@Test
	void testSortByValue() {
		List<Card> cards = Card.spawnDeck();
		Collections.shuffle(cards);
		cs.sortByValue(cards);
		for(int i=1; i<cards.size(); i++) {
			assertTrue(cards.get(i).getValue() >= cards.get(i-1).getValue());
		}
	}

	@Test
	void testSortBySuit() {
		List<Card> cards = Card.spawnDeck();
		Collections.shuffle(cards);
		CardSorter cs = new CardSorter();
		cs.sortBySuit(cards);
		for(int i=0; i<52; i++) {
			assertEquals(Card.suits[i/13] ,cards.get(i).suit);
			assertEquals((i%13)+1 ,cards.get(i).getValue());
		}
	}
}
