
public class FindSquareRoot {

	public static void main(String[] args) {
		int numberInput = 15625;//Integer.parseInt(args[0]);
		FindSquareRoot sq = new FindSquareRoot();
		System.out.println(Integer.toString(sq.findSquare(0,numberInput, numberInput/2, numberInput)));
	}
	int findSquare(int min, int max, int guess, int original){
		int gsquare = guess * guess;
		if(gsquare == original){ return guess; }
		else if( gsquare > original ){ return findSquare( min, guess, (guess + min)/2, original ); }
		else if( gsquare < original ){ return findSquare(guess, max, (max + guess)/2, original); }
		return 0;
	}

}
