package Lecture5;


import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.CycleMethod;
import javafx.scene.paint.Paint;
import javafx.scene.paint.RadialGradient;
import javafx.scene.paint.Stop;
import javafx.stage.Stage;

/**
 * This class draws balls on a 2D plane.
 * All balls move and are affected by gravity.
 * When balls hit the floor they bounce back up.
 * New balls are generated at regular time intervals.
 *
 */
/**
 * @author mva021
 *
 */
public class Painter extends Application {

	private Canvas canvas;

	public static void main(String[] args) {
		Application.launch(new String[0]);
	}

	@Override
	public void start(Stage stage) throws Exception {
		// create a canvas to draw balls on
		double width = 640;
		double height = 480;
		Group root = new Group();
		Scene scene = new Scene(root, width, height, Color.BLACK);
		stage.setScene(scene);
		canvas = new Canvas(width, height);
		canvas.widthProperty().bind(scene.widthProperty());
		canvas.heightProperty().bind(scene.heightProperty());

		// turn on the graphics
		root.getChildren().add(canvas);
		stage.show();
		
		TestDraw.draw(this);
	}

	/**
	 * Returns a random color
	 * @return
	 */
	private static Paint getRandomColor() {
		Color color = Color.RED.deriveColor(128 * Math.random(), 1.0, 1.0, .7);
		Color white = color.deriveColor(0.0, .33, 3.0, 2.0);
		Paint paint = new RadialGradient(0.0, 0.0, 0.3, 0.3, .6, true, CycleMethod.NO_CYCLE, new Stop(0.0, white),
				new Stop(1.0, (Color) color));
		return paint;
	}

	/**
	 * Draws on a canvas
	 */
	public void draw(Drawable item) {
		item.draw(this);
	}
	
	public void drawCircle(double x, double y, double width, double height){
		GraphicsContext context = canvas.getGraphicsContext2D();
//		context.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
//		context.save();
		context.setFill(getRandomColor());
		context.fillOval(x, y, width, height);
		context.restore();
	}
}
