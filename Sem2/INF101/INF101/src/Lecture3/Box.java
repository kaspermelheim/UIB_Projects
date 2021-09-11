package Lecture3;

public class Box {
	private int height;
	private int width;
	private int length;
	
	public void setHeight(int height) {
		if(height <= 0)
			System.out.println("FEIL: kan ikke ha negativ høyde.");
		else
			this.height = height;
	}
	
	public int getHeight() {
		return height;
	}
	
	public int getWidth() {
		return width;
	}
	
	public int getLength() {
		return length;
	}
	
	//Lager boksen, gir den height, width og length
	Box(int height, int width, int length) {
		this.height = height;
		this.width = width;
		this.length = length;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Box) {
			Box b = (Box) obj;
			if(b.height == this.height && b.width == this.width && b.length == this.length) {
				return true;
			}
		}
		return false;
	}
	
	public int volume() {
		return this.height*this.width*this.length;
	}
	
	public static void staticVolume() {
		
	}
	
	public String toString() {
		String str = "Dette er en boks med høyde " + height;
		return str;
	}
	
	

}
