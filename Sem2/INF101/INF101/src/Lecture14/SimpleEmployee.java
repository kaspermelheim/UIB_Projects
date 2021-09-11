package Lecture14;

public abstract class SimpleEmployee implements Employee {
	
	String first_name;
	String last_name;
	long account_number;
	
	SimpleEmployee(String first_name, String last_name, long account_number) {
		this.first_name = first_name;
		this.last_name = last_name;
		this.account_number = account_number;
	}

	@Override
	public String getName() {
		return first_name+ " " +last_name;
	}

	@Override
	public long getBankAccountNumber() {
		return account_number;
	}
	
	public abstract void print();
	
	public String toString() {
		return this.getName();
	}
}
