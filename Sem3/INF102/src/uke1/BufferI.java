package uke1;

/**
 *  Buffer for a text editor. An editor stores characters. 
 *  There is a cursor between 2 characters indicating where you are currently writing.
 */
public interface BufferI {
	
	//insert char c at cursor position
	void insert(char c);

	//get the char immediately to the left the cursor position
	char get();
	
	//delete and return the character immediately to the left the cursor position
	char delete();
	
	//advance the cursor k positions to the left
	void left(int k);
	
	//advance the cursor k positions to the right
	void right(int k);
	
	//return number of characters in the buffer
	int size();
}
