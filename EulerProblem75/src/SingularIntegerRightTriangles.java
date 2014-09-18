package src;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.ArrayList;
import java.util.List;


public class SingularIntegerRightTriangles {
	class ThreeNumbers implements Comparable{
		public int _a, _b, _c;
		public ThreeNumbers(int a, int b, int c){
			_a = a;
			_b = b;
			_c = c;
		}
		
		@Override
		public boolean equals(Object other){
			//System.out.println(compareTo(other));
			return 0 == compareTo(other);
		}

		@Override
		public int compareTo(Object other) {
			if(!(other instanceof ThreeNumbers)){ return 1; }
			if( other == this ){ return 0; }
			ThreeNumbers t = (ThreeNumbers)other;
			//System.out.println("HEY THERE ARE "+Integer.toString(t._a)+" " + Integer.toString(t._b) + " " + Integer.toString(t._c));
			if( t._a == this._a && 
				t._b == this._b &&
				t._c == this._c){ return 0; }
			else if( t._a == this._b && 
				t._b == this._a &&
				t._c == this._c){ return 0; }
			else if(  t._a == this._c && 
				t._b == this._b &&
				t._c == this._a){ return 0; }
			else{ return 1; }
		}
	}
	
	int numberIntegerRightTriangles(int circumference){
		Set<ThreeNumbers> s = new TreeSet<ThreeNumbers>();
		int count = 0;
		for( int a = 1; a < circumference/2; a++ ){
			int b = ((circumference*circumference/2) - circumference*a)/(circumference - a);
<<<<<<< HEAD
			float bb = (((float)(circumference*circumference)/2) - circumference *a)/((float)(circumference -a));
=======
			float bb = ((circumference*circumference/2) - circumference*a)/(circumference - a);
>>>>>>> 4f1a4c4916bd3feaf35e1ea1566020dc4679902b
			//for( int b = 1; b < circumference/2; b++){
				int c = circumference - a - b;
				if( a*a + b*b == c*c ){
					ThreeNumbers t = new ThreeNumbers(a,b,c);
					if( !s.contains(t)){
<<<<<<< HEAD
						//System.out.println(Integer.toString(a)+" " + Integer.toString(b) + " " + Integer.toString(c) + "="+Integer.toString(circumference) + " float bb=" + Float.toString(bb));
=======
						System.out.println(Integer.toString(a)+" " + Integer.toString(b) + " " + Integer.toString(c) + "="+Integer.toString(circumference) + " float b=" + Float.toString(bb));
>>>>>>> 4f1a4c4916bd3feaf35e1ea1566020dc4679902b
						s.add(t); 
						count++;
						if( count > 1 ){ return count; }
					}
				}
			//}
		}
		
		return s.size();
		
	}
	
	public int gcd(int a, int b){
		if( b == 0 ){
			return a;
		}
		return gcd( b, a % b );
	}
	
	public int calculatePythagoreanTriples(int maxCircumference){
		Map<Integer, Integer> listUniques = new TreeMap<Integer,Integer>();
		for( int n = 1; n < maxCircumference/2; n++ ){
			for( int m = n+1; m < maxCircumference/2; m++ ){
				if( 1 == (m-n)%2 &&  1 == gcd(m, n)){
					int a = m*m - n*n;
					int b = 2*m*n;
					int c = m*m + n*n;
					for( int k = 1; k < maxCircumference/2; k++ ){
						int circumference = k*a+k*b+k*c;
						if( circumference > maxCircumference ){ break; }
						//System.out.println(Integer.toString(a)+" " + Integer.toString(b) + " " + Integer.toString(c) + "="+Integer.toString(circumference) + " m="+Integer.toString(m) + " n=" + Integer.toString(n));
						if( listUniques.containsKey(circumference)){
							//int current = ;
							listUniques.put(circumference, listUniques.get(circumference)+1);
							//System.out.println("removing " + Integer.toString(circumference));
						}
						else{
							//System.out.println("Adding " + Integer.toString(circumference));
							listUniques.put(circumference, 1);
						}
					}
				}
			}
		}
		int count = 0;
		for(Map.Entry<Integer,Integer> entrySet : listUniques.entrySet() ){
			if( entrySet.getValue() == 1 ){ 
				//System.out.println(""+Integer.toString(entrySet.getKey()));
				count++; }
		}
		return count;
	}
	
	public static void main(String[] args) {
<<<<<<< HEAD
		int max = 1500000;
=======
		int max = 1000;//250;//1500000;
>>>>>>> 4f1a4c4916bd3feaf35e1ea1566020dc4679902b
		SingularIntegerRightTriangles s = new SingularIntegerRightTriangles();
		int totalNum = 0;
		System.out.println("Wiki way = " + Integer.toString(s.calculatePythagoreanTriples(max)));
		/*for(int i = 1; i <= max; i++ ){
			if( i % 10000 == 0 ){
				System.out.println("Up to " + Integer.toString(i) + " with "+ Integer.toString(totalNum)+ " matches ");
			}
			int count = s.numberIntegerRightTriangles(i);
			//System.out.println(Integer.toString(i)+" has " + Integer.toString(count) + " integer-right triangles" );
			if( count == 1 ){
				totalNum ++;
			}
		}
		System.out.println("There are " + Integer.toString(totalNum) + " numbers less than " + Integer.toString(max) + " that solve the numberIntegerRightTriangles exactly once ");
		*/
	}

}
