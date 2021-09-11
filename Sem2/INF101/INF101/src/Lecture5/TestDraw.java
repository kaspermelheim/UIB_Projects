package Lecture5;

import javafx.application.Application;

public class TestDraw {

	public static void main(String[] args) {
		Application.launch(Painter.class, new String[0]);
	}

	public static void draw(Painter painter)
	{
		painter.draw(new Circle(100, 100, 30));
	}
}
