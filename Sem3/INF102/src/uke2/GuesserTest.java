package uke2;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GuesserTest {

    @Test
    void searchWorks() {
        SecretNumber secret = new SecretNumber(42);
        assertEquals(42, new Guesser().interrogate(secret));

    }

    @Test
    void atLeastHalfEfficiency() {
        SecretNumber secret = new SecretNumber(842);
        assertEquals(842, new Guesser().interrogate(secret));
        assertTrue(secret.numberOfGuesses() <= 20);
    }

    @Test
    void optimalEfficiency() {
        SecretNumber secret = new SecretNumber(842);
        assertEquals(842, new Guesser().interrogate(secret));
        assertTrue(secret.numberOfGuesses() <= 10);
    }
}