package Lecture3;

import java.util.Random;

/**
 * Some useful methods to be used on a Box
 * These methods could be moved to the Box class
 * @author mva021
 *
 */
/**
 * @author mva021
 *
 */
class BoxUtil{
	/**
	 * Draws a box in the terminal window
	 * Works best for Box with small values unless you decrease the font size in the console
	 * @param b - The Box to draw
	 */
	public static void draw(Box b)
	{
		int height = b.getHeight();
		int width = b.getWidth();
		int depth = b.getLength();

		String s = "";
		for(int j = 1; j<=height+width+depth; j++)
		{
			s = s+'\n';
			for(int i = 1; i<=width+depth+3; i++)
			{
				if(i==1 && j>depth && j<=depth+height)
					s = s+'|';
				else if(i==width+depth+3 && j>width && j<=width+height)
					s = s+'|';
				else if(i==width+2 && j>width+depth)
					s = s+'|';
				else if(i>1 && i+j==depth+2)
					s = s+'/';
				else if(i+j==2*width+depth+3 && i>width+2 && i<width+depth+3)
					s = s+'/';
				else if(i+j==2*width+depth+height+3 && i>width+2 && i<width+depth+3)
					s = s+'/';
				else if(i-j==depth+2 && i<width+depth+3)
					s = s+'\\';
				else if(i-j==1-depth && i>1 && i<=width+1)
					s = s+'\\';
				else if(i-j==1-depth-height && i>1)
					s = s+'\\';
				else
					s = s+' ';
			}
		}
		System.out.println(s);
	}

	/**
	 * Draws all boxes in a list
	 * @param boxes - the list of boxes to draw
	 */
	public static void draw(Box[] boxes)
	{
		for(int i=0; i<boxes.length; i++)
			draw(boxes[i]);
	}

	
	/**
	 * Creates a random box where height, width and length are from 2 to 11
	 * @return a Box
	 */
	public static Box getRandomBox()
	{
		Random r = new Random();
		Box b = new Box(r.nextInt(10)+2,r.nextInt(10)+2,r.nextInt(10)+2);
		return b;
	}

	/**
	 * Creates a list of random boxes
	 * @return a list of boxes
	 */
	public static Box[] getRandomBoxes(int n)
	{
		Box[] boxes = new Box[n];
		for(int i = 0; i<n; i++)
		{
			boxes[i] = BoxUtil.getRandomBox();
		}
		return boxes;
	}
}
