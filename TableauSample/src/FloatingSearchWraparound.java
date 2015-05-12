
public class FloatingSearchWraparound {

	/**
	 * Looks for the location of x in the array of values
	 * @param values The array of floats - sorted but have a wrap-around
	 * @param x The value to search for
	 * @return -1 if not found, the position in the array if found
	 */
	public int searchWithWraparound(float[] values, float x){
		if( null == values || values.length == 0 ){
			return -1;
		}
		return searchWithWraparound(values, x, 0, values.length-1);
	}
	private int searchWithWraparound(float[] values, float x, int start, int end){
		int middle = (start + end)/2;
		if( values[middle] == x ){
			return middle;
		}
		
		if( end < start){
			return -1; //error condition
		}
		
		if( values[start] < values[middle] ){
			//left half is in order
			if( values[start] <= x && values[middle] >= x ){
				// x is between start and middle, so search left side
				return searchWithWraparound(values, x, start, middle-1);
			}
			else{
				// x is between middle and end, so search right side
				return searchWithWraparound(values, x, middle+1, end);
			}
		}
		else if( values[middle] < values[end] ){
			//right half is in order
			if( values[middle] <= x && values[end] >= x ){
				// x is between start and middle so search left side
				return searchWithWraparound(values, x, middle+1, end);
			}
			else{
				// x is between middle and end, so search right side
				return searchWithWraparound(values, x, start, middle-1);
			}
		}
		else if( values[start] == values[middle] ){
			//Left half is all the same value
			if( values[middle] == values[end] ){
				//Need to search both sides
				int ret = searchWithWraparound(values, x, start, middle-1);
				if( -1 == ret ){
					ret = searchWithWraparound(values, x, middle+1, end);
				}
				return ret;
			}
			else{
				//Just need to check the right side
				return searchWithWraparound(values, x, middle+1, end);
			}
		}
		return -1;
	}
}
