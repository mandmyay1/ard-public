//package src;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.ArrayList;
import java.util.List;


public class SingularIntegerRightTriangles {

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
		//Next part is for problem 39
		int maxSolutions = 0;
		int max = 0;
		for(Map.Entry<Integer,Integer> entrySet : listUniques.entrySet() ){
			if( entrySet.getValue() > max ){ 
				max =  entrySet.getValue();
				maxSolutions = entrySet.getKey();
			}
		}
		System.out.println("Max is "+Integer.toString(maxSolutions)+ " with "+Integer.toString(max));
		return count;
	}
	
	public static void main(String[] args) {
		int max = 1000;//1500000;
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
