package Lecture10;

import java.util.ArrayList;
import java.util.List;

public class Wardrobe {
	
	private List<IStorage> storage;
	
	public Wardrobe() {
		storage = new ArrayList<IStorage>();
	}

	public void BuildShelf() {
		storage.add(new Shelf(60, 60, 60));
	}
	
	public void BuildDrawer() {
		storage.add(new Drawer(60, 60, 15));
	}
	
	public boolean put(Clothing item) {
		for(IStorage place : storage) {
			if(place.canAdd(item)) {
				place.add(item);
				return true;
			}
		}
		return false;
	}
	
	public boolean get(Clothing item) {
		for(IStorage place : storage) {
			if(place.remove(item)) {
				return true;
			}
		}
		return false;
	}
	
	public static buildDreamWardrobe() {
		Wardrobe myWardrobe = new Wardrobe();
		Drawer standardDrawer = new Drawer(60, 60, 15);
		
		for(int i = 0; i <= 10; i++) {
			myWardrobe.BuildShelf();
		}
		
		return myWardrobe;
		
	}
}
