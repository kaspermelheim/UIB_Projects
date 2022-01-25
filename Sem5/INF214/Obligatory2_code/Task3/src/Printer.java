class Printer {

	private static Sem a1; private static Sem a2; private static Sem a3;

	public static void main(String[] args) {

		a1 = new Sem(1);
		a2 = new Sem(0);
		a3 = new Sem(0);

		Thread t1 = new Thread(() -> {
			while (true){
				try {
					a1.acquire();
					System.out.println("1");
					System.out.println("2");
					a2.release();
				}
				catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});

		Thread t2 = new Thread(() -> {
			while (true){
				try {
					a2.acquire();
					System.out.println("3");
					System.out.println("4");
					a3.release();
				}
				catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});

		Thread t3 = new Thread(() -> {
			while (true){
				try {
					a3.acquire();
					System.out.println("5");
					System.out.println("6");
					a1.release();
				}
				catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});

		try {
			t1.start();
			t2.start();
			t3.start();
			t1.join();
			t2.join();
			t3.join();
		}
		catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}