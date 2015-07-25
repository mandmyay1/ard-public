
public class QuickSort {
	public static void quicksort( int[] unsorted ){
		quicksort( unsorted, 0, unsorted.length-1 );
	}
	private static void quicksort(int[] unsorted, int low, int hi) {
		if( low >= hi ){
			return;
		}
		int p = partition(unsorted, low, hi);
		quicksort( unsorted, low, p-1 );
		quicksort( unsorted, p+1, hi );
	}
	private static int partition( int[] unsorted, int low, int hi ){
		int pivotIndex = (hi + low)/2;
		int pivotVal = unsorted[pivotIndex];
		
		int temp = unsorted[hi];
		unsorted[hi] = pivotVal;
		unsorted[pivotIndex] = temp;
		int finalPivotIndex = low;
		for( int i = low; i < hi; i++ ){
			if( unsorted[i] <= pivotVal ){
				temp = unsorted[i];
				unsorted[i] = unsorted[finalPivotIndex];
				unsorted[finalPivotIndex] = temp;
				finalPivotIndex ++;
			}
		}
		temp = unsorted[hi];
		unsorted[hi] = unsorted[finalPivotIndex];
		unsorted[finalPivotIndex] = temp;
		return finalPivotIndex;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] testArray = {5,4,123,7,2,5,1,875,2,4,4,54,23,54,43};
		quicksort(testArray);
		for( int b : testArray ){
			System.out.print(b);
			System.out.print(" ");
		}
	}

}
