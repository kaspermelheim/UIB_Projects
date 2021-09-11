package Lecture14;

public class Accountant extends SimpleEmployee {

	Accountant(String first_name, String last_name, long account_number) {
		super(first_name, last_name, account_number);
	}

	@Override
	public double getSalary(PaymentPeriod time) {
		return 100000;
	}

	@Override
	public void print() {
		System.out.println(this);
	}

}
