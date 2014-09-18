package src;
import java.io.BufferedReader;
import java.io.InputStreamReader;



public class PiCalculator {
	public static void main(String[] args){
		try{
			BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));

			System.out.println("Compute pi to the Nth digit: Enter N: ");
			String input = buff.readLine();
			
			int iRead = Integer.parseInt(input);
			
			//java.lang.Math.pow(iRead, iRead);
		} catch( Exception e ){
			e.printStackTrace();
		}
	}
	
	// formula PI = 16 * atan( 1/5 ) - 4 * atan( 1/239 )
	// atan( x ) = x^1/1 + x^3/3 + x^5/5 + ---
	public double computeNextDigit(double total, int power){
		//java.lang.math
		return 0.0;
	}
}
