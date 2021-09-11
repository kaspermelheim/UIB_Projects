package Lecture8;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CardDeck<T> implements ICardDeck<T> {

	//we use an ArrayList to store the cards
	ArrayList<T> cards;

	/**
	 * Generates a deck and adds all the cards
	 */
	public CardDeck() {
		cards = new ArrayList<T>(52);
		List<T> all_cards = Card.spawnDeck();
		cards.addAll(all_cards);
	}
	
// Det er fult mulig � skrive koden for � generere en kortstok her.
// Men hvis det senere skal genereres flere typer kortstokk blir det vanskelig
// � gjenbruke denne koden. Bedre hvis vi kan ha koden i Card klassen
//	private void spawnDeck() {
//		
//		for(String suit : Card.suits) {
//			for(String value : Card.names) {
//				cards.add(new Card(suit,value));
//			}
//		}
//	}


	public static void main(String[] args) {
		// Lag en ny kortstokk med 52 kort
		Card sampleCard = new Card("Spades", "Ace");
		CardDeck<Card> deck = new CardDeck<Card>(sampleCard);
		
		// stokk kortene
		deck.shuffle();
		
		// trekk 52 kort og skriv dem ut etterhvert
		for(int i=0;i<52;i++) {
			System.out.println(deck.draw());
		}
	}
	
	@Override
	public void shuffle() {
		//using existing methods normally saves you trouble
		//sometimes you will need to use google to find what you need
		Collections.shuffle(cards);
	}

	@Override
	public T draw() {
		if(this.isEmpty())
			throw new ArrayIndexOutOfBoundsException("Ingen kort igjen");
		return cards.remove(0);
	}

	@Override
	public boolean isEmpty() {
		return cards.isEmpty();
	}
}
