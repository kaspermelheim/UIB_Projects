package Lecture10;

import java.util.ArrayList;
import java.util.List;

public class Shelf implements IStorage {

	int height;
	int width;
	int depth;
	List<Clothing> clothes;
	
	public Shelf(int width, int depth, int height) {
		this.height = height;
		this.width = width;
		this.depth = depth;
		clothes = new ArrayList<Clothing>();
	}

	public int getHeight() {
		return this.height;
	}
	
	public int getWidth() {
		return width;
	}
	
	public int getDepth() {
		return depth;
	}
	
	public boolean add(Clothing clothing) {
		if(canAdd(clothing)) {
			clothes.add(clothing);
			return true;
		}
		else {
			return false;
		}
	}
	
	public boolean canAdd(Clothing item) {
		if(item.isDirty()) {
			return false;
		}
		if(item.getType().equals("Socks")) {
			return false;
		}
		
		return true;
	}
	
	public boolean remove(Clothing item) {
		if(clothes.contains(item)) {
			clothes.remove(item);
			return true;
		}
		else {
			return false;
		}
	}
	
	public static void main(String[] args) {
		
		Shelf shelf = new Shelf(60, 40, 30);
		
		if(shelf.add(new Clothing("Levis", 20, "Jeans"))) {
			System.out.println("La den på en hylle!");
		}
		else {
			System.out.println("Kunne ikke legge den på hyllen.");
		}
		
	}
	
	
}
