import static org.junit.Assert.*;
import org.junit.Test;

public class StringRearrange {
	/**
	 * even method
	 * @param i The integer to check
	 * @return True if the integer passed in is an even number, False otherwise.
	 */
	private static boolean even(int i){
		return (i%2 == 0);
	}
	
	/**
	 * reOrder method
	 * Attempt 1 to re-order based on odd/even using StringBuilders
	 * @param input The string to re-order in the form of a character array
	 * @return The re-ordered string. All characters at odd indices from the input string will come before 
	 *         the characters from even indices.
	 */
	public String reOrder(char[] input){
		if( null == input ){
			return "";
		}
		StringBuilder evens = new StringBuilder();
		StringBuilder odds = new StringBuilder();
		for( int i = 0; i < input.length; i++ ){
			if( StringRearrange.even(i) ){
				evens.append(input[i]);
			}
			else{
				odds.append(input[i]);
			}
		}
		return odds.toString() + evens.toString();
	}
	
	/**
	 * reOrderInPlace method
	 * Attempt 2 to re-order with only a character array.
	 * @param input The string to re-order in the form of a character array
	 * @return The re-ordered string. All characters at odd indices from the input string will come before 
	 *         the characters from even indices.
	 */
	public String reOrderInPlace(char[] input){
		if( null == input ){
			return "";
		}
		char[] returnArray = new char[input.length];
		int oddsStart = 0;
		int evensStart = input.length/2;
		for( int i = 0; i < input.length; i++ ){
			if( StringRearrange.even(i) ){
				returnArray[evensStart] = input[i];
				evensStart++;
			}
			else{
				returnArray[oddsStart] = input[i];
				oddsStart++;
			}
		}
		
		return new String(returnArray);
	}
	
	//Private function used for testing below
	private void firstHalfOddSecondHalfEven(String input){
		for( int i = 0; i < input.length(); i++ ){
			int oneInt = Integer.parseInt(input.substring(i,i+1));
			if( i < input.length() /2 ){
				//All indices less than half should be ODD
				assertFalse(StringRearrange.even(oneInt));
			}
			else{
				//All indices greater than half should be EVEN
				assertTrue(StringRearrange.even(oneInt));
			}
		}
	}
	@Test
	public void test(){
		//Test the even function
		StringRearrange rearranger = new StringRearrange();
		assertFalse(StringRearrange.even(-1));
		assertFalse(StringRearrange.even(1));
		assertFalse(StringRearrange.even(123456789));
		
		assertTrue(StringRearrange.even(0));
		assertTrue(StringRearrange.even(-2));
		assertTrue(StringRearrange.even(12345678));
		
		//Need to generate a large number. "01234567890123456...."
		//This should re-order into "1357913579...0246802468..."
		StringBuilder largeInputBuilder = new StringBuilder();
		final int sizeOfLargeInput = 5000;
		for( int i = 0; i < sizeOfLargeInput; i++ ){
			int val = i%10;
			largeInputBuilder.append(val);
		}
		String largeInput = largeInputBuilder.toString();
		
		//Test the first method
		assertEquals("bdac", rearranger.reOrder("abcd".toCharArray()));
		assertEquals("bdace", rearranger.reOrder("abcde".toCharArray()));
		assertEquals("", rearranger.reOrder(null));
		assertEquals("", rearranger.reOrder("".toCharArray()));
		assertEquals("1357902468",rearranger.reOrder("0123456789".toCharArray()));
		
		String largeResult = rearranger.reOrder(largeInput.toCharArray());
		firstHalfOddSecondHalfEven(largeResult);

		//Test the second method
		assertEquals("bdac", rearranger.reOrderInPlace("abcd".toCharArray()));
		assertEquals("bdace", rearranger.reOrderInPlace("abcde".toCharArray()));
		assertEquals("", rearranger.reOrderInPlace(null));
		assertEquals("", rearranger.reOrderInPlace("".toCharArray()));
		assertEquals("1357902468",rearranger.reOrderInPlace("0123456789".toCharArray()));
		
		String largeResultInPlace = rearranger.reOrderInPlace(largeInput.toCharArray());
		firstHalfOddSecondHalfEven(largeResultInPlace);
	}
	
}
