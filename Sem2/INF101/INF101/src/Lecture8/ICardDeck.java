package Lecture8;

/**
 * A deck of playing cards
 * Normal deck of cards contains 52 unique cards, 
 * but a deck can have more cards and some can be repeated
 *
 * @author mva021
 *
 */
public interface ICardDeck<T> {

	/**
	 * Makes sure subsequent calls to draw() returns a random card
	 */
	public void shuffle();

	/**
	 * Gets the top card from the deck.
	 * That card is removed such that subsequent calls to draw will not get the same card
	 * @return one of the cards remaining in the deck
	 */
	public T draw();

	/**
	 * Returns {@code true} if this deck contains no cards.
	 *
	 * @return {@code true} if this deck contains no cards
	 */
	public boolean isEmpty();
}