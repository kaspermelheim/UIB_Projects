package inf112_tester;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class RomanNumeralConverterTest {

	@Test
	void oneShouldConvertToI() {
		RomanNumeralConverter converter = new RomanNumeralConverter();
		
		String result = converter.convert(1);
		assertEquals("I", result);
	}
	
	@Test
	void twoShouldConvertToII() {
		RomanNumeralConverter converter = new RomanNumeralConverter();
		
		String result = converter.convert(2);
		assertEquals("II", result);
	}
	
	@Test
	void threeShouldConvertToIII() {
		RomanNumeralConverter converter = new RomanNumeralConverter();
		
		String result = converter.convert(3);
		assertEquals("III", result);
	}

}
