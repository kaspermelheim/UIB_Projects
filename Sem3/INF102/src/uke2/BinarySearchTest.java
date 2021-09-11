package uke2;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class BinarySearchTest{
    List<Integer> numbers = Arrays.asList(new Integer[]{1, 2, 2, 4, 5, 7, 9});

    @Test
    void searchFindsIndex() {
        assertEquals(3, new BinarySearch().search(numbers, 4));
    }

    @Test
    void searchHandlesDuplicates() {
        assertEquals(1, new BinarySearch().search(numbers, 2));
    }

    @Test
    void searchHandlesSearchMiss() {
        assertEquals(-1, new BinarySearch().search(numbers, 6));
    }
}
