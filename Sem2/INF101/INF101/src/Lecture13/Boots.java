package Lecture13;

public class Boots implements IShoes{
	
	int height;

	public int getHeight() {
		return this.height;
	}

	@Override
	public int getShoeSize() {
		return 0;
	}

	@Override
	public String getBrand() {
		return null;
	}
}
