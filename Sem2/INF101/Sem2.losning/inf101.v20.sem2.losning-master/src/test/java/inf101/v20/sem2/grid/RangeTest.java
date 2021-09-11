package inf101.v20.sem2.grid;

import static inf101.v20.sem2.tools.Range.range;
import static org.junit.jupiter.api.Assertions.*;

import java.util.NoSuchElementException;

import org.junit.jupiter.api.Test;

import inf101.v20.sem2.tools.Range;

class RangeTest {

	@Test
	void testRange() {
		Range range1 = new Range(10);
		Range range2 = new Range(-1);
	}

	@Test
	void testHasNext() {
		int n=10;
		Range range = range(n);
		int count = 0;
		while(range.hasNext()) {
			range.next();
			count++;
		}
		assertEquals(n, count);
			
	}

	@Test
	void testNext() {
		int n=10;
		Range range = range(n);
		for(int i=0; i<n; i++){
			assertEquals(i, range.next());
		}
		try {
			range.next();
		} catch (Exception e) {
			assertTrue(e instanceof NoSuchElementException);
			return;
		}
		fail("range.next() should not work after reaching the end of the range.");
	}

	@Test
	void testIterator() {
		int n = 10;
		Range r = range(n);
		for(int i : range(n))
			assertEquals(r.next(), i);
	}

}
