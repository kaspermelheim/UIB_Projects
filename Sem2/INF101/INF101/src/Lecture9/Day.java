package Lecture9;

import java.time.LocalDate;

public class Day {

	static String weekday(LocalDate day) {
		
		int daysBefore = getDaysBefore(day);
		daysBefore = daysBefore%7;
		
		if(daysBefore%7) {
			
		}
		
		switch(daysBefore%7) {
		
		case 0:
			return "Monday";
		case 1:
			return "Sunday";
		case 2:
			return "Saturday";
		case 3:
			return "Friday";
		case 4:
			return "Thursday";
		case 5:
			return "Wednesday";
		case 6: 
			return "Tuesday";
			
		default:
			throw new IllegalArgumentException("Unexpected value: "+ daysBefore%7);
	}
		
}
		
	
	/**
	 * Counts day before Monday 10 of February 2020
	 * @param day
	 * @return
	 */
	
	private static int getDaysBefore(LocalDate day) {
		
		LocalDate today = LocalDate.of(2020, 2, 10);
		int daysBefore = 0;
		
		while(day.isBefore(today)) {
			daysBefore++;
			day = day.plusDays(1);
		}
		
		while(day.isAfter(today)) {
			daysBefore++;
			day = day.minusDays(1);
		}
		
		return daysBefore;
	}
}