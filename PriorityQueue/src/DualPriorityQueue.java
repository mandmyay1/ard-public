import java.util.Vector;



class Node<T> {
	T value;
	double priorityA;
	double priorityB;
	public Node(T val, double priA, double priB){
		value = val;
		priorityA = priA;
		priorityB = priB;
	}
}

public class DualPriorityQueue<T> {
	boolean isMin;	//Defaults to true
	Vector<Node<T> > impl = new Vector<Node<T> >();
	Node<T> minA = null;
	Node<T> minB = null;
	public DualPriorityQueue(){
		this.isMin = true;
	}
	public DualPriorityQueue(boolean isMin){
		this.isMin = isMin;
	}
	public void Enqueue(T val, double priorityA, double priorityB){
		Node<T> node = new Node<T>(val, priorityA, priorityB);
		impl.add(node);
		checkMins(node);
	}
	
	public Node<T> DequeueA(){
		if( null != minA ){
			impl.remove(minA);
		}
		Node<T> oldMin = minA;
		minA = null;
		minB = null;
		for( Node<T> node : impl ){
			checkMins(node);
		}
		return oldMin;
	}
	
	public Node<T> DequeueB(){
		if( null != minB ){
			impl.remove(minB);
		}
		Node<T> oldMin = minB;
		minA = null;
		minB = null;
		for( Node<T> node : impl ){
			checkMins(node);
		}
		return oldMin;
	}
	
	public int Count(){
		return impl.size();
	}
	public void Clear(){
		impl.clear();
	}
	
	private void checkMins(Node<T> node){
		if( null == minA || 
			(isMin && minA.priorityA > node.priorityA) ||
			(!isMin && minA.priorityA < node.priorityA) ){
			minA = node;
		}
		if( null == minB ||
			(isMin && minB.priorityB > node.priorityB ) || 
			(!isMin && minB.priorityB < node.priorityB) ){
			minB = node;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DualPriorityQueue<String> testQueue = new DualPriorityQueue<String>();
		testQueue.Enqueue("Hyperion Hypodermic Needle", 1.99, 3);
		testQueue.Enqueue("SuperSaver Syringe", .89, 7);
		testQueue.Enqueue("InjectXpress Platinum Plated Needle", 2.49, 2);

		System.out.println(testQueue.Count());
		System.out.println(testQueue.DequeueA().value);
		System.out.println(testQueue.Count());
		System.out.println(testQueue.DequeueA().value);
		System.out.println(testQueue.Count());
		System.out.println(testQueue.DequeueA().value);
		System.out.println(testQueue.Count());
		System.out.println(testQueue.DequeueA());
	}

}
