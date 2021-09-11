import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TestingTest {
    @Test
    void checkIfHello() {
        Testing tester = new Testing();

        String result = Testing.toText(1);
        assertEquals("One", result);
    }

}