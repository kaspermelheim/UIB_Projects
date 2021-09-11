import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {

    @Test
    void regularNumberShouldReturnAsString() {
        FizzBuzz fb = new FizzBuzz();

        String result = fb.convert(2);

        assertEquals("2", result);
    }

    @Test
    void threeShouldReturnAsFiz() {
        FizzBuzz fb = new FizzBuzz();

        String result = fb.convert(3);

        assertEquals("fiz", result);
    }

    @Test
    void fiveShouldReturnAsBuzz() {
        FizzBuzz fb = new FizzBuzz();

        String result = fb.convert(5);

        assertEquals("buzz", result);
    }
}
