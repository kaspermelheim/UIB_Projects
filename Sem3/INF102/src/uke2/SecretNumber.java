package uke2;

public class SecretNumber {
    private int secret;
    private int guesses;

    SecretNumber(int secret){
        assert(secret < 1024);
        this.secret = secret;
        this.guesses = 0;
    }

    public String makeGuess(int guess){
        guesses += 1;
        if (guess < secret) return "bigger";
        else if (guess > secret) return "smaller";
        else return "correct";
    }

    public int numberOfGuesses(){
        return guesses;
    }
}