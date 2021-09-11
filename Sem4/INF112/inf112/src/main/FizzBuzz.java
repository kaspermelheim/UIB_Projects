
public class FizzBuzz {
    public String convert(int input) {
        if(input % 5 == 0) {
            return "fiz";
        }
        if(input == 5) {
            return "buzz";
        }
        return Integer.toString(input);
    }
}
