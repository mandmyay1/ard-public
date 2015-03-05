
public class KFromN {
	int[] n;
	int k;
	int[] positions;
	boolean hasMore = true;
	
	public KFromN(int[] arr, int ipK){
		n = arr;
		k = ipK;
		positions = new int[k];
		for( int i = 0; i < k; i++ ){
			positions[i] = i;
		}
	}
	
	public int[] next(){
		int[] retArray = new int[k];
		for( int i = 0; i < k; i++ ){
			retArray[i] = n[positions[i]];
		}
		
		int indexToIncrement = -1;
		for( int i = k-1; i >= 0; i-- ){
			if( positions[i] != n.length - k + i){
				indexToIncrement = i;
				break;
			}
		}
		if( -1 != indexToIncrement ){
			positions[indexToIncrement]++;
			for( int i = indexToIncrement+1; i < k; i++ ){
				positions[i] = positions[i-1]+1;
			}
		}
		else{
			hasMore = false;
		}
		
		return retArray;
	}
	
	public boolean hasNext(){
		return hasMore;
	}
	
	
	public static void main(String[] args){
		int[] arr = {0,1,2,3,4,5,6};
		int k = 3;
		KFromN kn = new KFromN(arr, k);
		while( kn.hasNext() ){
			int[] next = kn.next();
			StringBuilder sb = new StringBuilder();
			sb.append("[");
			for( int j = 0; j < next.length; j++ ){
				sb.append(next[j]);
				if( j+1 < next.length ){
					sb.append(",");
				}
			}
			sb.append("]");
			System.out.println(sb.toString());
		}
	}
}
