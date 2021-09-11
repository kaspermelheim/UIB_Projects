package Lecture3;

public class TestBox {

	public static void main(String[] args) {
		Box minBoks = new Box(5,7,4);
		Box dinBoks = new Box(20,20,50);
		
		System.out.println(minBoks.volume());
		//Box.staticVolume(minBoks);
		
		BoxUtil.draw(minBoks);
		//if(!minBoks.equals(dinBoks)) {
		//	BoxUtil.draw(dinBoks); }
		
		//minBoks.setHeight(10);
		//dinBoks.setHeight(20);
		
		//System.out.println("Min: "+ minBoks);
		//System.out.println("Din: " + dinBoks);
		
		//System.out.println("Total høyde er "+(minBoks.getHeight() + dinBoks.getHeight()));

	}

}
