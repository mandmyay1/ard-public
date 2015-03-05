import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;


public class SearchPassage {
	
	class FoundPassage{
		String act;
		String scene;
		int startIndex;
		int endIndex;
		List<String> speakingCharacters;
		@Override
		public String toString(){
			StringBuilder sb = new StringBuilder();
			int pos = act.indexOf(".");
			if( -1 != pos ){
				act = act.substring(0, pos);
			}
			sb.append(act);
			sb.append(System.lineSeparator());
			pos = scene.indexOf(".");
			if( -1 != pos ){
				scene = scene.substring(0, pos);
			}
			sb.append(scene);
			sb.append(System.lineSeparator());
			sb.append("Characters in scene: ");
			for( int i = 0; i < speakingCharacters.size(); i++){
				String character = speakingCharacters.get(i);
				sb.append(character);
				if( i+1 < speakingCharacters.size() ){
					sb.append(", ");
				}
			}
			sb.append(System.lineSeparator());
			for( int i = startIndex; i < endIndex; i++ ){
				sb.append(lines.get(i));
				sb.append(System.lineSeparator());
			}
			return sb.toString();
		}
	}
	
	List<String> lines = null;
	final String fourSpaces = "    ";
	final String twoSpaces = "  ";
	
	public SearchPassage(String file){
		try {
			lines = Files.readAllLines(Paths.get(file), Charset.defaultCharset());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static boolean startsWith(String one, String two){
		return one.length() > two.length() && one.substring(0, two.length()).equals( two );
	}
	
	public int searchBackwardsFor(int position, String lookingFor){
		while(position >= 0){
			if( startsWith(lines.get(position), lookingFor)){
				break;
			}
			position--;
		}
		return position;
	}
	public int findPassageStart(int position){
		while( position >= 0){
			if( !startsWith(lines.get(position), fourSpaces) && startsWith(lines.get(position), twoSpaces) ){
				break;
			}
			position--;
		}
		
		return position;
	}
	
	public int findPassageEnd(int position){
		while( position < lines.size() ){
			if( !startsWith(lines.get(position), fourSpaces) && startsWith(lines.get(position), twoSpaces) ){
				break;
			}
			position++;
		}
		return position;
	}
	
	public List<String> findSpeakingCharacters(int start, int end){
		List<String> speakingCharacters = new ArrayList<String>();
		for( int index = start; index < end; index++ ){
			String line = lines.get(index);
			if( startsWith(line, fourSpaces) ){ continue; }
			
			if( startsWith(line, twoSpaces) ){
				String formattedLine = line.trim().replaceAll("\\.", "");
				if( !speakingCharacters.contains(formattedLine)){
					speakingCharacters.add(formattedLine);
				}
			}
		}
		return speakingCharacters;
	}
	
	public List<FoundPassage> Search(String input){
		List<FoundPassage> returnList = new ArrayList<FoundPassage>();
		for( int i = 0; i < lines.size(); i++ ){
			String line = lines.get(i);
			if( startsWith(line, fourSpaces) ){
				int pos = line.indexOf(input);
				if( -1 == pos ){ continue; }
				
				int start = findPassageStart(i);
				int end = findPassageEnd(i);
				int scene = searchBackwardsFor(start, "SCENE");
				int act = searchBackwardsFor(scene, "ACT");
				List<String> speakingCharacters = findSpeakingCharacters(scene, end);
				
				FoundPassage newFound = new FoundPassage();
				newFound.startIndex = start;
				newFound.endIndex = end;
				newFound.act = lines.get(act);
				newFound.scene = lines.get(scene);
				newFound.speakingCharacters = speakingCharacters;
				returnList.add(newFound);

			}
		}
		return returnList;
	}
	
	public static void main(String[] args){
		SearchPassage sp = new SearchPassage("src/macbeth.txt");
		for( FoundPassage fp : sp.Search("rhinoceros") ){
			System.out.println(fp.toString());
		};
		
		//System.out.println(SearchPassage.startsWith("    hello", "    "));
	}
	
}
