package Innlogging_Prosjekt;

import java.util.ArrayList;
import java.util.Scanner;

import Innlogging_Prosjekt.Log;
import Innlogging_Prosjekt.ILog;

public class LogMain {

	public static Scanner input = new Scanner(System.in);
	
	public static void main(String[] args) throws Exception {
		
		ILog log = new Log();
		
		System.out.print(
				"Velkommen til Facebook.com. \n "
				+ "Du kan når som helst stoppe innloging ved å skrive 'stop'.\n"
				+ "For å logge inn, skriv 'login', `\n"
				+ "for å registrere ny bruker skriv 'register': ");
		
		String melding = input.nextLine();
		
		if("login".equals(melding)) {
			log.login();
		}
		else if("register".equals(melding)) {
			log.register();
		}
		else if("stop".equals(melding)) {
			throw new Exception("User stopped program.");
		}
		else {
			System.out.println("Ugyldig input.");
		}
		
//		Log.addEl("passord4", Log.passordList);
//		Log.delEl("brukernavn1", Log.navnList);
		
//		System.out.println(Log.navnList);
//		System.out.println(Log.passordList);

	}

}
