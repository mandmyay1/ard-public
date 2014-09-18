
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;


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
		for( int a = 1; a < circumference/2; a++ ){
			int b = ((circumference*circumference/2) - circumference*a)/(circumference - a);
			float bb = ((circumference*circumference/2) - circumference*a)/(circumference - a);
			//for( int b = 1; b < circumference/2; b++){
				int c = circumference - a - b;
				if( a*a + b*b == c*c ){
					ThreeNumbers t = new ThreeNumbers(a,b,c);
					if( !s.contains(t)){
						System.out.println(Integer.toString(a)+" " + Integer.toString(b) + " " + Integer.toString(c) + "="+Integer.toString(circumference) + " float b=" + Float.toString(bb));
						s.add(t); 
					}
				}
			//}
		}
		
		return s.size();
		
	}
	public static void main(String[] args) {
		int max = 1000;//250;//1500000;
		SingularIntegerRightTriangles s = new SingularIntegerRightTriangles();
		int totalNum = 0;
		for(int i = 1; i <= max; i++ ){
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
	}

}
