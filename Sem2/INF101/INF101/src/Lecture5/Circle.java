package Lecture5;

public class Circle {

	private Position pos;
	private int radius;
	
	public Circle(int x, int y) {
		this(x,y,20);
	}

	public Circle(int x, int y, int radius) {
		pos = new Position(x,y);
		this.radius = radius;
	}

	@Override
	public Position getPosition() {
		return pos;
	}

	@Override
	public void draw(Painter painter) {
		painter.drawCircle(pos.getX(), pos.getY(), radius, radius);
	}

}
