
public class Quicksort {
	
	public void sort(int[] arr, int low, int high){
		int p = partition(arr, low, high);
		if( low < p-1 ){ 
			sort(arr, low, p-1);
		}
		if( p < high ){
			sort(arr, p, high);
		}
	}
	
	public int partition(int[] arr, int low, int high){
		int pivot = (high + low)/2;
		int pivotValue = arr[pivot];
		
		int i = low;
		int j = high;
		while( i <= j ){
			while( arr[i] < pivotValue ){
				i++;
			}
			while( arr[j] > pivotValue ){
				j--;
			}
			if( i <= j ){
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
				i++;
				j--;
			}
		}
		return i;
	}
	
	
	public static void main(String args[]){
		int[] arr = {1, 12, 5, 26, 7, 14, 3, 7, 2};
		Quicksort qs = new Quicksort();
		qs.sort(arr, 0, arr.length-1);
		for( int i = 0; i < arr.length; i++ ){
			System.out.println(arr[i]);
		}
	}
}
