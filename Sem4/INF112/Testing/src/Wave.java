public class Wave {

	public String txt = "";

	public String addWave() {
		txt += "x";
		return txt;
	}

	public String delWave() {
		txt.replace("x", "");
		return txt;
	}

	public void run(int times) {
		for(int i = 0; i < times/8; i++) {
			System.out.println(addWave());
		}
		for(int i = 0; i < times/8; i++) {
			System.out.println(delWave());
		}
	}

	public static void main(String[] args) {
		Wave w = new Wave();
		w.run(100);
	}
}

