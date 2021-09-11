package uke2;

public class Guesser implements GuesserI {

	@Override
	public int interrogate(SecretNumber secret) {
		int low = 0;
		int high = 1024;
		while(low + 1 < high) {
			int mid = (low + high) / 2;
			String ans = secret.makeGuess(mid);
			if(ans.compareTo("correct") == 0) return mid;
			else if (ans.compareTo("bigger") == 0) low = mid + 1;
			else high = mid;
		}
		return high;
	}

}
