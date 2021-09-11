package Lecture9;

import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDate;
import java.util.ArrayList;

import org.junit.jupiter.api.Test;

class DayTest {
	
	private LocalDate getToday() {
		return LocalDate.of(2020, 2, 10);
	}
	
	private ArrayList<LocalDate> getPastTuesdays() {
		ArrayList<LocalDate> list = new ArrayList<LocalDate>();
		
		
		return list;
	}
	
	@Test
	void textWeekdayTuesdays() {
		ArrayList<LocalDate> tuesdays = getPastTuesdays();
		for(LocalDate tuesday : tuesdays) {
			assertEquals("Tuesday", Day.weekday(tuesday), "Should be a tuesday.");
		}
	}
	
	@Test
	void textWeekdayWednesdays() {
		ArrayList<LocalDate> tuesdays = getPastTuesdays();
		for(LocalDate tuesday : tuesdays) {
			LocalDate wednesday = tuesday.plusDays(1);
			assertEquals("Wednesday", Day.weekday(wednesday), "Should be a wednesday.");
		}
	}

	@Test
	void testWeekdayToday() {
		LocalDate today = getToday();
		String weekday = Day.weekday(today);
		assertEquals("Monday", weekday, "Today should be a monday.");
	}
	
	@Test
	void testWeekdayTomorrow() {
		LocalDate today = getToday();
		LocalDate tomorrow = today.plusDays(1);
		String weekday = Day.weekday(tomorrow);
		assertEquals("Tuesday", weekday, "Today should be a tuesday.");
	}

}
