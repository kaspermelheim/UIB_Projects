package Lecture10;

public interface IStorage {

	public int getHeight();
	
	public int getWidth();
	
	public int getDepth();
	
	public boolean add(Clothing clothing);
	
	public boolean remove(Clothing clothing);
	
	public boolean canAdd(Clothing clothing);
	
}
