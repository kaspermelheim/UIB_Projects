package Lecture14;

public class Consultant extends SimpleEmployee {
	
	double hourlySalary;
	
	
	Consultant(String first_name, String last_name, long account_number, double hourlySalary) {
		super(first_name, last_name, account_number);
		this.hourlySalary = hourlySalary;
	}

	@Override
	public String getName() {
		return first_name+ " " +last_name;
	}

	@Override
	public long getBankAccountNumber() {
		return account_number;
	}

	@Override
	public double getSalary(PaymentPeriod time) {
		return hourlySalary * getNumberOfHours(time);
	}
	
	private int getNumberOfHours(PaymentPeriod time) {
		//TODO Not implemented properly
		return 10;
	}

	@Override
	public void print() {
		System.out.println(this);
		
	}

	public String toString() {
		return super.toString() + " er en Consultant";
	}
}
