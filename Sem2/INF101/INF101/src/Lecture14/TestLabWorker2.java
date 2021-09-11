package Lecture14;

public class TestLabWorker2 {

	public static void main(String[] args) {

		LabWorker assistant = new LabWorker("Anna", "Eilertsen", 2323323232L);
		LabLeader leader = new LabLeader("Martin", "Vatshelle", 2356939493949L);
		Consultant help = new Consultant("Knut Anders", "Stokke", 734343444545L, 442.3);
		
		leader.addAssistant(assistant);
		
		System.out.println(assistant);
		System.out.println(leader + " with salary " + leader.getSalary(new PaymentPeriod()));
		System.out.println(help + " with salary " + help.getSalary(new PaymentPeriod()));
		
	}

}