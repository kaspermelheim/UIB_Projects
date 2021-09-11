package uke1;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import Lecture2.HashDuplicateFinder;
import Lecture2.SimpleDuplicateFinder;

public class DuplicateTimer {
	
	static Random r = new Random();

	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			timeSimple(10000);
			timeHash(10000);
			timeFast(10000);
		}
		
		double Simple1000 = 0;
		double Simple10000 = 0;
		double Hash1000 = 0;
		double Hash10000 = 0;
		double Fast1000 = 0;
		double Fast10000 = 0;
		
		for (int i = 0; i < 100; i++) {
			Simple1000 += timeSimple(1000);
			Hash1000 += timeHash(1000);
			Fast1000 += timeFast(1000);
			Simple10000 += timeSimple(10000);
			Hash10000 += timeHash(10000);
			Fast10000 += timeFast(10000);
		}
		
		System.out.printf("Simple: 1000: %.3f, 10000: %.3f\n", Simple1000, Simple10000);
		System.out.printf("Hash: 1000: %.3f, 10000: %.3f\n", Hash1000, Hash10000);
		System.out.printf("Fast: 1000: %.3f, 10000: %.3f\n", Fast1000, Fast10000);
	}
	
	static double timeSimple(int size) {
		List<Integer> numbers = new ArrayList<>();
		for (int i = 0; i < size; i++) {
			numbers.add(r.nextInt() % 10000);
		}
		long start = System.currentTimeMillis();
		new SimpleDuplicateFinder().findDuplicate(numbers);
		long end = System.currentTimeMillis();
		return (end - start) / 1000d;
	}
	
	static double timeHash(int size) {
		List<Integer> numbers = new ArrayList<>();
		for (int i = 0; i < size; i++) {
			numbers.add(r.nextInt() % 10000);
		}
		long start = System.currentTimeMillis();
		new HashDuplicateFinder().findDuplicate(numbers);
		long end = System.currentTimeMillis();
		return (end - start) / 1000d;
	}
	
	static double timeFast(int size) {
		List<Integer> numbers = new ArrayList<>();
		for (int i = 0; i < size; i++) {
			numbers.add(r.nextInt() % 10000);
		}
		long start = System.currentTimeMillis();
		new SimpleDuplicateFinder().findDuplicate(numbers);
		long end = System.currentTimeMillis();
		return (end - start) / 1000d;
	}
}
