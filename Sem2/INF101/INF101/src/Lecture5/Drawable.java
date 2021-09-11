package Lecture5;

public interface Drawable {

	/**
	 * Instruct painter how to draw this object
	 * @param painter
	 */
	public void draw(Painter painter, CameraPosition cp);
		
	public Position getPosition();
	
}