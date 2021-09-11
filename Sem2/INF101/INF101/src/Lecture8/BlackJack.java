package Lecture8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BlackJack {
	
	List<IPlayer> players;
	
	BlackJack() {
		players = new ArrayList<IPlayer>();
		players.add(new Player());
		
		playRound(players);
	}
	
	private void playRound(List<IPlayer> players2) {
		Card sampleCard = new Card("Spades", "Ace");
		CardDeck<Card> deck = new CardDeck<Card>(sampleCard);
		
		ArrayList<ArrayList<Card>> playerCards = new ArrayList<ArrayList<Card>>(players.size());
		
		for(int i=0; i<players.size(); i++) {
			new ArrayList<Card>();
			playerCards.add();
		}
	}

	public List<Card> getHand(IPlayer player) {
		return null;
	}

	/**
	 * Computes the score for a BlackJack hand 
	 * @param hand the list of cards this player has
	 * @return the value of this hand
	 */
	public static int getValueOf(List<Card> hand){
		int score = 0; //the sum of card values
		int num_ace = 0; // number of aces (could make this a boolean as one never benefits from 2 aces
		
		// loop through cards (: notation works because List<Card> implements Iterable<Card>
		for(Card card : hand) {
			//Aces are special
			if(card.getValueName().equals("Ace")) {
				score +=1; //compute score if ace is counted as 1
				num_ace++;
			}else {
				//Knight, Queen and King should all count as 10, but card.getValue() > 10
				score += Math.min(card.getValue(),10);
			}
		}
		//turn an ace into 11 if that improves score
		while(num_ace>0 && score+10<=21) {
			score += 10;
			num_ace--;
		}
		return score;
		
	}
	public static void main(String[] args) {
		// lag en ny liste med kort
		ArrayList<Card> hand = new ArrayList<Card>();
		hand.add(new Card("Hjerter", "Syv"));
		hand.add(new Card("Spades", "Ace"));
		
		// skriv ut BlackJack verdien
		System.out.println(BlackJack.getValueOf(hand));
		
		//test � endre p� final verdier
		//keyword final f�r en variabel betyr at denne kun kan settes en gang og ikke kan endres senere
//		Card.suits = new String[3]; // can not change final variables

		// suits er en referanse til et objekt (minneadresse) selv om denne referansen er final og
		// ikke kan endres s� kan objectet som suits refererer til likevel endres
		Card.suits[0] = "Spar";
		System.out.println(Arrays.toString(Card.suits));
		
	}
}

