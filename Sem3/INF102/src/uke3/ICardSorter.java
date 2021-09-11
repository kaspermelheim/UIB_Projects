package uke3;

import java.util.List;

/**
 * This interface describes the methods needed 
 * to sort cards in 2 different ways.
 * 
 * @author Martin Vatshelle
 */
public interface ICardSorter {

	/**
	 * This sorts a list of cards by value 
	 * i.e. Ace, Two, Three, ..., Queen and King
	 * Cards of equal value can be placed in any order
	 * @param cards - The list of cards to be sorted
	 */
	public void sortByValue(List<Card> cards);

	/**
	 * This sorts a list of cards by Suit 
	 * i.e. Spades, Hearts, Clubs and Diamonds
	 * Cards of equal suit should be sorted by their value
	 * @param cards
	 */
	public void sortBySuit(List<Card> cards);
}
