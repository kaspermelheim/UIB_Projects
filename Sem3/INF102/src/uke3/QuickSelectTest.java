package uke3;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class QuickSelectTest {

    @Test
    void shuffleTest(){
        List<Integer> numbers = Arrays.asList(new Integer[] {0,5,2,4,1,3});
        assertEquals(2, new QuickSelect().findKth(numbers, 3));
    }

    @Test
    void kLessThan1Test(){
        List<Integer> numbers = Arrays.asList(new Integer[] {0,5,2,4,1,3});
        assertThrows(IllegalArgumentException.class, () -> {new QuickSelect().findKth(numbers, 0);});
    }

    @Test
    void kToLargeTest(){
        List<Integer> numbers = Arrays.asList(new Integer[] {0,5,2,4,1,3});
        assertThrows(IndexOutOfBoundsException.class, () -> {new QuickSelect().findKth(numbers, 7);});
    }
}
