package uke3;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;

public class SortVisual extends Frame{
	
	public static void main(String[] args) {
		SortVisual sv = new SortVisual();
		sv.setSize(400, 400);
		numbers = new ArrayList<>();
		
		
	}

	ArrayList<Integer> numbers;
	
	BufferedImage buffer;
	Graphics bufferGraphics;
	
	public void update(Graphics g) {
		if (buffer == null) {
			buffer = new BufferedImage(this.getWidth(), this.getHeight(), BufferedImage.TYPE_INT_ARGB);
			bufferGraphics = buffer.createGraphics();
		}
		paint(bufferGraphics);
		g.drawImage(buffer, 0, 0, null);
	}
	
	public void paint(Graphics g) {
		g.setColor(Color.BLACK);
		g.drawRect(0, 0, this.getWidth(), this.getHeight());
		g.setColor(Color.WHITE);
		for (int i = 0; i < numbers.size(); i++) {
			g.drawLine(i,  this.getHeight()-1, i, this.getHeight()-1-numbers.get(i));
		}
	}
}
