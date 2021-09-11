package Lecture10;

public class Clothing {
	
	private String brand;
	private int size;
	private String type;
	public boolean isDirty;
	public boolean didShrink;

	public Clothing(String brand, int size, String type) {
		this.brand = brand;
		this.size = size;
		this.type = type;
	}

	public String getBrand() {
		return brand;
	}
	
	public String getType() {
		return this.type;
	}
	
	public int getSize() {
		return this.size;
	}
	
	public void makeDirty() {
		isDirty = true;
		
	}
	
	public boolean isDirty() {
		return isDirty;
	}
	
	public void makeClean() {
		isDirty = false;
	}
	
	public void shrink() {
		size = size - 1;
	}
	
}
