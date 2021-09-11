import java.time.Instant;

import java.util.ArrayList;

import java.util.List;

import java.util.logging.Level;



public class Test {

	public String createMessage(Instant time, String name, Level level, String message, Exception exception) {
		StringBuilder result = new StringBuilder();
		if (time == null) {
			time = Instant.now();
		}
		if (name == null) {
			name = "";
		}
		if (message == null) {
			message = "";
		}

		result.append(String.format("%s - %s -- %s Content: %s. ", time.toString(), level.getName().toUpperCase(), name, message));

		if ((level.equals(Level.SEVERE) || level.equals(Level.WARNING)) && exception != null) {
			result.append(String.format("Exception message: %s. \n", exception.getMessage()));
			result.append(String.format("Stack trace: %s", formatStackTrace(exception.getStackTrace())));

		}
		else if (exception != null) {
			result.append(exception.getMessage());
		}

		return result.toString();
	}

	private List<String> formatStackTrace(StackTraceElement[] trace) {
		List<String> result = new ArrayList<>();
		// iterate over stacktrace and create readable strings with correct indentation
		return result;
	}

	public static void main(String[] args) {
		Exception t1 = new Exception();
		Test t = new Test();
		System.out.print(t.createMessage(null, "TestName", Level.SEVERE, "Something wrong happened", null));
	}

}