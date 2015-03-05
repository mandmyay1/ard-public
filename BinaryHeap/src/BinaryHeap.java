import static org.junit.Assert.*;

import org.junit.Test;




public class BinaryHeap {
	int[] impl = new int[1];
	int countEntries = 0;
	int depth = 1;
	
	public int length(){
		return countEntries;
	}
	
	public void add(int number){
		if( countEntries >= impl.length ){
			int[] newImpl = new int[(int)Math.pow(2, depth) + impl.length];
			for( int i = 0; i < impl.length; i++ ){
				newImpl[i] = impl[i];
			}
			impl = newImpl;
			depth++;
		}
		impl[countEntries] = number;
		heapifyUp(countEntries);
		countEntries++;
	}
	
	public void heapifyUp(int position){
		int insertedVal = impl[position];
		int parentPosition = parent(position);
		int parent = impl[parentPosition];
		if( parent > insertedVal ){
			swap(parentPosition, position);
			heapifyUp(parentPosition);
		}
	}
	
	public int peek(){
		return impl[0];
	}
	
	public int pop(){
		int retVal = impl[0];
		swap(0, countEntries-1);
		countEntries--;
		heapifyDown(0);
		
		return retVal;
	}

	public void heapifyDown(int position){
		int leftPos = left(position);
		int rightPos = right(position);
		int smallest = position;
		
		if( leftPos < countEntries && impl[leftPos] < impl[smallest] ){
			smallest = leftPos;
		}
		if( rightPos < countEntries && impl[rightPos] < impl[smallest]){
			smallest = rightPos;
		}

		if( smallest != position ){
			swap(position, smallest);
			heapifyDown(smallest);
		}
	}
	
	private void swap(int pos1, int pos2){
		int temp = impl[pos1];
		impl[pos1] = impl[pos2];
		impl[pos2] = temp;
	}
	
	private int parent(int number){
		return (number -1)/2;
	}
	private int left(int number){
		return 2*number + 1;
	}
	private int right(int number){
		return 2*number + 2;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	@Test
	public void test(){
		BinaryHeap b = new BinaryHeap();
		assertEquals(0, b.length());
		
		b.add(60);
		b.add(50);
		b.add(20);
		b.add(10);
		b.add(30);
		b.add(0);
		b.add(40);
		
		assertEquals(0, b.peek());
		assertEquals(7, b.length());
		assertEquals(0, b.pop());
		assertEquals(10, b.pop());
		assertEquals(20, b.pop());
		assertEquals(30, b.pop());
		assertEquals(3, b.length());
	}

}
