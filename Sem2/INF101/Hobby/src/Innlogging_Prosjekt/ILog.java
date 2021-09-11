package Innlogging_Prosjekt;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

public interface ILog {

	boolean inputLengde(String input);
	
	void register() throws Exception;
	
	void login() throws Exception;

	void addEl(String input, ArrayList<String> liste);

	void delEl(String input, ArrayList<String> liste);
	
	void readFile(String file, ArrayList<String> liste) throws FileNotFoundException, IOException, Exception;

	void writeFile(String input, String file);
}
