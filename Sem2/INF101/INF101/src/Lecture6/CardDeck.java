package Lecture6;

import java.util.ArrayList;
import java.util.Collections;

public class CardDeck implements ICardCheck {
	
	
	ArrayList<Card> cards;
	
	public CardDeck() {
		cards = new ArrayList<Card>(52);
		spawnDeck();
	}
	
	private void spawnDeck() {
	
		for(String suit : Card.suits) {
			for(String value : Card.names) {
				cards.add(new Card(suit,value));
			}
		}
	}
	
	public static void main(String[] args) {
		Card card = new Card("Hearts", "King");
		System.out.println(card);
	}

	@Override
	public void shuffle() {
		Collections.shuffle(cards);
	}

	@Override
	public Card draw() {
		if(this.isEmpty()) {
			throw new ArrayIndexOutOfBoundsException("Ingen kort igjen.");
		}
		return cards.remove(0);
	}

	@Override
	public boolean isEmpty() {
		return cards.isEmpty();
	}

}
