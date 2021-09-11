package Innlogging_Prosjekt;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Log implements ILog{

	private ArrayList<String> passordList;
	private ArrayList<String> navnList;
	private Scanner input = new Scanner(System.in);
	private boolean login_ = false;
	private boolean register_ = false;
	
	String navnfile_cd = "C:\\Users\\Kasper\\Documents\\UIB\\INF101\\Hobby\\brukernavn_fil.txt";
	String passfile_cd = "C:\\Users\\Kasper\\Documents\\UIB\\INF101\\Hobby\\passord_fil.txt";
	
	public Log() throws IOException {
		
		passordList = new ArrayList<String>();
		navnList = new ArrayList<String>();
		
		readFile(navnfile_cd, navnList);
		readFile(passfile_cd, passordList);
	}
	
	@Override
	public void register() throws Exception {
		while(!register_) {
			System.out.println("Registrer et brukernavn på minst 6 bokstaver: ");
			String reg_brukernavn = input.next();
			
			checkStop(reg_brukernavn);
			
			if(inputLengde(reg_brukernavn)) {
				if(navnList.contains(reg_brukernavn)) {
					System.out.println("Brukernavn finnes allerede!");
					continue;
				}
				else {
					writeFile(reg_brukernavn, navnfile_cd);
				}
			}
			else {
				System.out.println("Input må være minst 6 bokstaver langt.");
			}
			
			System.out.println("Registrer et passord på minst 6 bokstaver: ");
			String reg_passord = input.next();
			
			checkStop(reg_passord);
			
			if(inputLengde(reg_passord)) {
				if(passordList.contains(reg_passord)) {
					//Do nothing
				}
				else {
					writeFile(reg_passord, passfile_cd);
				}
			}
			else {
				System.out.println("Input må være minst 6 bokstaver langt.");
			}
			register_ = true;
		}
		
		if(register_) {
			System.out.println("Registrering vellykket.");
		}
		else {
			System.out.println("Registrering feilet");
		}
	}
	
	@Override
	public void login() throws Exception {
		while(!login_) {
			
			System.out.print("Skriv inn brukernavn: ");
			String brukernavn = input.next();
			
			checkStop(brukernavn);
			
			if (inputLengde(brukernavn)) {
				if(navnList.contains(brukernavn)) {
					//Do nothing
					login_ = false;
				}
				else {
					System.out.println("Input finnes ikke i database.");
					continue;
				}
			}
			else {
				System.out.println("Input må være minst 6 bokstaver langt.");
				continue;
			}
			
			System.out.println("Skriv inn passord: ");
			String passord = input.next();	
			
			checkStop(passord);
			
			if (inputLengde(passord)) {
				if(passordList.contains(passord)) {
					//Do nothing
					login_ = false;
				}
				else {
					System.out.println("Input finnes ikke i database.");
					continue;
				}
			}
			else {
				System.out.println("Input må være minst 6 bokstaver langt.");
				continue;
			}
			login_ = true;
		}
		
		if(login_) {
			System.out.println("Innlogging godkjent.");
		}
		else {
			System.out.println("Innlogging feilet.");
		}
	}	
	
	public void checkStop(String input) throws Exception {
		if("stop".equals(input)) {
			throw new Exception("User stopped program.");
		}
	}

	/**
	 * Skal sjekke om passord er minst 6 bokstaver langt og inneholder 1 tall
	 * @param input
	 * @throws Exception 
	 */
	@Override
	public boolean inputLengde(String input) {
		
		if(input.length() >= 6) {
			return true;
		}
		return false;
	}

	@Override
	public void addEl(String input, ArrayList<String> liste) {
		if(!liste.contains(input)) {
			liste.add(input);
		}
		else {
			System.out.println(input + " finnes allerde i " + liste + ".");
		}	
	}

	@Override
	public void delEl(String input, ArrayList<String> liste) {
		if(liste.contains(input)) {
			liste.remove(input);
		}
		else {
			System.out.println(input + " finnes ikke i " + liste + ".");
		}
	}

	@Override
	public void readFile(String file, ArrayList<String> liste) throws IOException {
		BufferedReader reader = new BufferedReader(new FileReader(file));	
	    String line = reader.readLine();
	    while (line != null) {
	    	liste.add(line);
	    	line = reader.readLine();
	    }
	    reader.close();	
	}
	
	@Override
	public void writeFile(String input, String file) {
		try {
			//FileWriter writer = new FileWriter(file);
		
			PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(file, true)));
		    writer.write(input + "\n");
		    writer.close();
		} 
		catch (IOException e) {
		    System.out.println("An error occurred.");
		    e.printStackTrace();
		}
	}
}

