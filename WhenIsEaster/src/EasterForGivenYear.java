import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;


public class EasterForGivenYear {

	public static Calendar calculateEaster(int year){
		int a = year %19;
		int b = year /100;
		int c = year %100;
		int d = b /4;
		int e = b %4;
		int f = ((b+8)/25);
		int g = ((b-f+1)/3);
		int h = (19*a + b - d - g + 15) %30;
		int i = c /4;
		int k = c %4;
		int l = (32 + 2*e + 2*i -h -k) %7;
		int m = ((a + 11*h + 22*l) /451);
		int month = ((h+l -7*m + 114) /31) -1;	//Need the -1 at the end because GregorianCalendar is 0-based
		int day = ((h + l -7*m + 114) %31) +1;
		Calendar calendar = new GregorianCalendar(year, month, day);
		return calendar;
	}
	public static void main(String[] args) {
		SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
		for( int i = 2005; i < 2025; i++){
			System.out.println(formatter.format(EasterForGivenYear.calculateEaster(i).getTime()));
		}
	}

}
