package Lecture14;

public class TestLabWorkers {

	public static void main(String[] args) {
		LabWorker assistant = new LabWorker("Anna", "Eilertsen");
		LabLeader leader = new LabLeader("Martin", "Vatshelle");
		leader.addAssistant(assistant);
		
		System.out.println(leader.getName() + " is the leader with salary " + leader.getSalary(new PaymentPeriod()));
		System.out.println(assistant.getName() + " is the assistant salary " + assistant.getSalary(new PaymentPeriod()));

		leader.getLabAssistants();
//		assistant.getLabAssistants(); can not do this, compile error
	}
}
