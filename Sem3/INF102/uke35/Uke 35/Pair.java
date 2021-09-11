package closest_pair;

/**
 * Class that holds a pair of double values.
 * @author mva021
 *
 */
public class Pair {

	double a;
	double b;
	
	Pair(double a, double b){
		this.a = a;
		this.b = b;
	}
	
	
	public double difference() {
		return Math.abs(a-b);
	}
	
	@Override
		public String toString() {
			return "("+a+","+b+")";
		}
}
