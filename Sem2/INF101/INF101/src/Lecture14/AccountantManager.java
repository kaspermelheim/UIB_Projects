package Lecture14;

import java.util.List;

public class AccountantManager extends Accountant {
	
	List<Employee> assistants;

	AccountantManager(String first_name, String last_name, long account_number) {
		super(first_name, last_name, account_number);
	}

	public double getBonus() {
		return 1000*getAssistants().size();
	}
	
	public void addAssistant(LabWorker assistant) {
		assistants.add(assistant);
	}

	public List<Employee> getLabAssistants() {
		return assistants;
	}
}
