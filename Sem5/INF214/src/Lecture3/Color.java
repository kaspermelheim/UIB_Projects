package Lecture3;

public class Color {

	private String name;
	private int r;
	private int g;
	private int b;

	public Color(String name, int r, int g, int b) {
		this.name = name;
		this.r = r;
		this.g = g;
		this.b = b;
	}

	//method set:
	public synchronized void set(String name, int r, int g, int b) {
		this.name = name;
		this.r = r;
		this.g = g;
		this.b = b;
	}

	//method getIntegerRepresentation:
	public synchronized int getIntegerRepresentation() {
		return 1000000 * r + 1000 * g + b;
	}

	//method getName
	public synchronized String getName() {
		return this.name;
	}

	//method invert
	public synchronized void invert() {
		r = 255 - r;
		g = 255 - g;
		b = 255 - b;
	}
}
