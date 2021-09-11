package Lecture6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BlackJack {

	
	public static int getValueOf(List<Card> hand) {
		int score = 0;
		int num_ace = 0;
		for(Card card : hand) {
			if(card.getValueName().equals("Ace")) {
				score += 1;
				num_ace++;
			}
			else {
				score += Math.min(card.getValue(), 10);
			}
		}
		while(num_ace > 0 && score+10 <= 21) {
			score += 10;
			num_ace--;
		}
		return score;
	}
	
	public static void main(String[] args) {
		/** ArrayList<Card> hand = new ArrayList<Card>();
		hand.add(new Card("Hearts", "Syv"));
		hand.add(new Card("Spades", "Ace"));
		
		System.out.println(BlackJack.getValueOf(hand)); 
		*/
		CardDeck deck = new CardDeck();
		deck.shuffle();
		
		int num_cards = 0;
		for(int i = 1; i <= 52; i++) {
			System.out.println(deck.draw());
			num_cards++;
		}
		
		// Teller over alle kort og sjekker om vi har en komplett kortstokk
		System.out.println("Total amount of cards: " + num_cards);

	}

}
