import java.util.Arrays;

public class MergeNames {

	public static String[] uniqueNames(String[] names1, String[] names2) {
		String[] newArray = new String[] {"t","t","t","t"};

		for (int x = 0; x < 12; x++) {
			for (String i : names1){
				for (String j : names2){
					if (!Arrays.asList(newArray).contains(i)){
						newArray[x] = i;
					}
				}
			}
		}
		System.out.println(newArray);
		return newArray;
	}

	public static void main(String[] args) {
		String[] names1 = new String[] {"Ava", "Emma", "Olivia"};
		String[] names2 = new String[] {"Olivia", "Sophia", "Emma"};
		System.out.println(String.join(", ", MergeNames.uniqueNames(names1, names2))); // should print Ava, Emma, Olivia, Sophia
	}
}