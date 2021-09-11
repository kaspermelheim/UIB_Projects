package Lecture14;

import java.util.ArrayList;
import java.util.List;

public class LabLeader extends LabWorker {
	
	List<Employee> assistants;
	 

	public LabLeader(String first_name, String last_name, long account_number) {
		super(first_name, last_name, account_number);
		assistants = new ArrayList<Employee>(2);
		monthlySalary *= 2;
	}

	@Override
	public long getBankAccountNumber() {
		return account_number;
	}

	@Override
	public double getSalary(PaymentPeriod time) {
		if(!time.isMonth()) {
			throw new IllegalArgumentException("LabLeader can only get monthly salary.");
		}
		return monthlySalary + getBonus();
	}
	
	public double getBonus() {
		return 1000*getLabAssistants().size();
	}
	
	public void addAssistant(LabWorker assistant) {
		assistants.add(assistant);
	}

	public List<Employee> getLabAssistants() {
		return assistants;
	}
	
	public String toString() {
		return super.getName() + " er en LabLeader";
	}
	
	public void print() {
		System.out.println(super.toString());
	}
}
