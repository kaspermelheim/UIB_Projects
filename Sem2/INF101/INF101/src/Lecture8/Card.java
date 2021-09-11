package Lecture8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * A card from a standard deck of 52 card playing cards
 * @author mva021
 *
 */
public class Card implements ICard {

	static final String[] names = {"Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine", "Ten", "Knight", "Queen", "King"};
	static final String[] suits = {"Spades","Hearts","Clubs","Diamonds"};

	String suit;
	String value;
	
	/**
	 * Constructor
	 * @param suit -should be one of Hearts, Diamonds, Clubs, Spades
	 * @param value -should be one of the card values in {@code names}
	 */
	public Card(String suit, String value) {
		//convert the array of valid value names to a List
		List<String> validNames = Arrays.asList(names);
		// check that given value is among the valid listed value names
		// ! is negation of boolean value
		if(!validNames.contains(value)) {
			throw new IllegalArgumentException(value +" is not a valid card value");
		}
		// check same for suits (note here we repeat code... could be improved)
		List<String> validSuits = Arrays.asList(suits);
		if(!validSuits.contains(suit)) {
			throw new IllegalArgumentException(suit +" is not a valid card suit");
		}

		this.suit = suit;
		this.value = value;
	}
	
	/**
	 * Gets the name of the card value e.g. Ace, Six, Queen
	 * @return
	 */
	public String getValueName() {
		return value;
	}
	
	/**
	 * Gets the standard int value corresponding to the card
	 * This value may vary depending on the game played,
	 * if this is the case a special function within that game should convert.
	 * @return value with 1 <= value <= 13 
	 */
	public int getValue() {
		//convert the array names to a List
		List<String> al = Arrays.asList(names);
		//find the index in the array and add 1 to make from 1 to 13
		return al.indexOf(value)+1;
	}
	
	@Override
	public String toString() {
		return value+" of "+suit;
	}
	
	/**
	 * Makes a List of cards which contains all the valid cards a deck can have.
	 * @return a list of 52 different cards
	 */
	public List<Card> spawnDeck() {
		
		ArrayList<Card> deck = new ArrayList<Card>();
		
		for(String suit : Card.suits) {
			for(String value : Card.names) {
				deck.add(new Card(suit,value));
			}
		}
		return deck;
	}
}