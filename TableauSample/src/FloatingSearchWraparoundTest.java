import static org.junit.Assert.*;

import java.util.Random;

import org.junit.Test;


public class FloatingSearchWraparoundTest {

	@Test
	public void test() {
		FloatingSearchWraparound searcher = new FloatingSearchWraparound();
		float[] values = {4.0f, 5.0f, 1.0f, 2.0f, 3.0f};
		assertEquals(1, searcher.searchWithWraparound(values, 5.0f));
		assertEquals(0, searcher.searchWithWraparound(values, 4.0f));
		assertEquals(4, searcher.searchWithWraparound(values, 3.0f));
		assertEquals(-1, searcher.searchWithWraparound(values, 5.2f));
		
		assertEquals(-1, searcher.searchWithWraparound(null, 0.0f));
		
		float[] emptyArray = {};
		assertEquals(-1, searcher.searchWithWraparound(emptyArray, 5.0f));
		
		float[] repeatedValues = {2.0f, 2.0f, 2.0f, 3.0f, 3.0f, 3.0f, 4.0f, 5.0f, 1.0f, 1.5f};
		int positionOfThree = searcher.searchWithWraparound(repeatedValues, 3.0f);
		assertTrue(3 <= positionOfThree && 5 >= positionOfThree );	//Any of the 3.0f will be valid
		int positionOfTwo = searcher.searchWithWraparound(repeatedValues, 2.0f);
		assertTrue(0 <= positionOfTwo && 2 >= positionOfTwo );	//Any of the 2.0f will be valid
		assertEquals(6, searcher.searchWithWraparound(repeatedValues, 4.0f));
		
		float[] repeatsOnBothEnds = {2.0f, 2.0f, 2.0f, 2.0f, 2.0f, 4.0f, 5.0f, 1.0f, 2.0f};
		assertEquals(6, searcher.searchWithWraparound(repeatsOnBothEnds, 5.0f));
		assertEquals(5, searcher.searchWithWraparound(repeatsOnBothEnds, 4.0f));
		int positionOfTwoWithRepeatsOnEnds = searcher.searchWithWraparound(repeatsOnBothEnds, 2.0f);
		assertTrue( positionOfTwoWithRepeatsOnEnds == 0 
				 || positionOfTwoWithRepeatsOnEnds == 1
				 || positionOfTwoWithRepeatsOnEnds == 2
				 || positionOfTwoWithRepeatsOnEnds == 3
				 || positionOfTwoWithRepeatsOnEnds == 4
				 || positionOfTwoWithRepeatsOnEnds == 8);
		
		//Create a large array
		final int sizeOfLargeArray = 5000;
		float[] largeArray = new float[sizeOfLargeArray];
		Random random = new Random();
		//Create a random inflection point
		int startPoint = random.nextInt(sizeOfLargeArray);
		for(int i = 0; i < sizeOfLargeArray; i++ ){
			if( startPoint + i >= sizeOfLargeArray ){
				startPoint = -i;
			}
			largeArray[startPoint+i] = (float)i;
		}
		assertEquals(sizeOfLargeArray-3, searcher.searchWithWraparound(largeArray, largeArray[sizeOfLargeArray-3]));
		assertEquals(-1, searcher.searchWithWraparound(largeArray, (float)sizeOfLargeArray+1));
	}

}
