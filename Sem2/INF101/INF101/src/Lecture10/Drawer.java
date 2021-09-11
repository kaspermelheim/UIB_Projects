package Lecture10;

import java.util.ArrayList;
import java.util.List;

public class Drawer implements IStorage {
	
	int height;
	int width;
	int depth;
	List<Clothing> clothes;
	
	public Drawer(int width, int depth, int height) {
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

	public boolean remove(Clothing item) {
		if(clothes.contains(item)) {
			clothes.remove(item);
			return true;
		}
		else {
			return false;
		}
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
		if(item.getType().equals("Shoes")) {
			return false;
		}
		
		return true;
	}
	
}
