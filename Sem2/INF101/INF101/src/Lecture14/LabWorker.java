package Lecture14;

public class LabWorker extends SimpleEmployee {

	double monthlySalary;
	 

	LabWorker(String first_name, String last_name, long account_number) {
		super(first_name, last_name, account_number);
		monthlySalary = 20000;
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
		if(!time.isMonth()) {
			throw new IllegalArgumentException("LabWorker can only get monthly salary.");
		}
		return monthlySalary;
	}

	@Override
	public String toString() {
		return getName() + " er en LabWorker";
	}

	@Override
	public void print() {
		System.out.println(this);
		
	}
	
	

}
