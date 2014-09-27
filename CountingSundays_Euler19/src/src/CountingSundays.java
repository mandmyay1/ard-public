package src;

import java.util.ArrayList;
import java.util.List;

public class CountingSundays {
	class year{
		int _year;
		List<month> _months = new ArrayList<month>();
		int _startDay;	//0-6
		public year(int yea, int startDay){
			_startDay = startDay;
			_year = yea;
			_months.add(new month(31));	//Jan
			_months.add(new month(28 + (isLeapYear()? 1:0)));	//feb
			_months.add(new month(31));	//mar
			_months.add(new month(30));	//apr
			_months.add(new month(31));	//may
			_months.add(new month(30));	//jun
			_months.add(new month(31));	//Jul
			_months.add(new month(31));	//aug
			_months.add(new month(30));	//sep
			_months.add(new month(31));	//oct
			_months.add(new month(30));	//nov
			_months.add(new month(31));	//dec
		}
		public boolean isLeapYear(){
			if( _year % 400 == 0 ){
				return true;
			}
			else if( _year % 100 == 0 ){
				return false;
			}
			else if( _year % 4 == 0 ){
				return true;
			}
			else{
				return false; 
			}
		}
		public int getNumberSundaysOnFirstOfMonth(){
			int total = 0;
			int firstDayOfMonth = _startDay;
			for( month m : _months ){
				//System.out.println(Integer.toString(firstDayOfMonth));
				if( firstDayOfMonth == 6 ){
					total ++;
				}
				firstDayOfMonth = firstDayOfMonth + m._numdays % 7;
				if( firstDayOfMonth > 6 ){ firstDayOfMonth -= 7; }
			}
			return total;
		}
		public int getLastDayOfYear(){	//0-6
			int totalDays = getTotalDays();
			//int numWeeks = totalDays /7;
			int daysRemaining = totalDays %7;
			//System.out.println(Integer.toString(daysRemaining));
			int lastDay = daysRemaining + _startDay;
			if( lastDay > 6 ){ lastDay -= 7; }
			//System.out.println(Integer.toString(lastDay));
			return lastDay;
		}
		public int getTotalDays(){
			int total = 0;
			for( month m : _months ){
				total += m._numdays;
			}
			return total;
		}
	}
	class month{
		int _numdays;
		public month(int days){
			_numdays = days;
		}
	}
	
	public void run(){
		int start = 1900;
		int end = 2001;
		int firstDay = 0;
		int totalSundays = 0;
		List<year> years = new ArrayList<year>();
		for( int i = start; i < end; i++ ){
			year y = new year(i,firstDay);
			years.add(y);
			if( i > 1900 ){
				totalSundays += y.getNumberSundaysOnFirstOfMonth();
			}
			firstDay = y.getLastDayOfYear();
		}

		System.out.println("Total Sundays " + Integer.toString(totalSundays));
		//year y = new year(1900,0);
		//y.getNumberSundaysOnFirstOfMonth();
	}
	
	public static void main(String[] args){
		CountingSundays counting = new CountingSundays();
		//List<year> _years = new ArrayList<year>();
		counting.run();
	}
}
