import java.util.Scanner;
public class GuessNumber {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int lowest = 0, highest = 100, guess = 0;
		boolean found = false;
		int count = 0;
		while( !found ){
			guess = (highest+1 + lowest)/2;
			System.out.println("Is your number " + Integer.toString(guess) + "? (Y)es,(H)igher,(L)ower");
			String result = s.next();
			count ++;
			if( result.equalsIgnoreCase("y") || result.equalsIgnoreCase("YES")){ found = true; }
			else if( result.equalsIgnoreCase("H") || result.equalsIgnoreCase("HIGHER")){ lowest = guess; }
			else if( result.equalsIgnoreCase("L") || result.equalsIgnoreCase("Lower")){ highest = guess; }
			else{ count--; }
		}
		System.out.println("Found the answer " + Integer.toString(guess) + " in " + Integer.toString(count) + " guesses");
		s.close();
	}
}
