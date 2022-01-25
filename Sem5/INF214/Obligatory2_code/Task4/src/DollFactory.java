import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.BrokenBarrierException;

class DollFactory {
	List<Doll> dolls;
	private CyclicBarrier stageA, stageB, stageC;

	private void execution(int dollsNumber) throws InterruptedException {
		stageA = new CyclicBarrier(dollsNumber);
		stageB = new CyclicBarrier(dollsNumber);
		stageC = new CyclicBarrier(dollsNumber);

		dolls = new ArrayList<>(dollsNumber);

		for (int i = 0; i < dollsNumber; i++) {
			Thread t = new Thread(new Process(i));
			t.start();
		}

		try {
			this.stageC.await();
			System.out.println("Packaging process D");
			Iterator i = this.dolls.iterator();

			while(i.hasNext()) {
				Doll doll = (Doll) i.next();
				System.out.println("Doll " + doll.getId() + " is ready for packaging");
			}
			System.out.println("Dolls produced: " + this.dolls.size());
		}
		catch (BrokenBarrierException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws InterruptedException {
		DollFactory dcb = new DollFactory();
		dcb.execution(30); // Let's produce 100 dolls
	}


	// nested class Process
	class Process implements Runnable {
		int id;

		public Process(int id) {
			this.id = id;
		}

		public void run() {

			Doll doll = this.assembly();
			System.out.println("Doll " + doll.getId() + " produced");

			try {
				stageA.await();
			} catch (BrokenBarrierException | InterruptedException e) {
				e.printStackTrace();
			}

			this.painting(doll);
			System.out.println("Doll " + doll.getId() + " painted");

			try {
				stageB.await();
			} catch (BrokenBarrierException | InterruptedException e) {
				e.printStackTrace();
			}

			this.qualityControl(doll);
			if (doll.getImperfections()) {
				System.out.println("Doll " + doll.getId() + " failed inspection");
			} else {
				System.out.println("Doll " + doll.getId() + " passed inspection");
			}

			try {
				stageC.await();
			} catch (BrokenBarrierException | InterruptedException e) {
				e.printStackTrace();
			}
		}

		void painting(Doll d) {
			d.setPainted(true);
		}

		Doll assembly() {
			Random r = new Random();
			return new Doll(id, r.nextInt(4) + 7);
		}

		void qualityControl(Doll d) {
			if (d.getQualityScore() >= 9) {
				d.hasImperfections(false);
				dolls.add(d);
			}
			else {
				d.hasImperfections(true);
			}
		}
	}
}


//////////////////////////////////////////

class Doll {
	int id;
	int qualityScoreMachine;
	boolean imperfect, isPainted;

	public Doll(int id, int qualityScoreMachine) {
		this.id = id;
		this.qualityScoreMachine = qualityScoreMachine;
	}

	public int getQualityScore() {
		return this.qualityScoreMachine;
	}

	public void setQualityScore(int qualityScoreMachine) {
		this.qualityScoreMachine = qualityScoreMachine;
	}

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public boolean getImperfections() {
		return this.imperfect;
	}

	public void hasImperfections(boolean imperfect) {
		this.imperfect = imperfect;
	}

	public boolean isPainted() {
		return this.isPainted;
	}

	public void setPainted(boolean painted) {
		this.isPainted = painted;
	}
}


