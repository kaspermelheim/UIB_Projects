package inf101.v20.sem2.GUI;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.MouseListener;

import javax.swing.BorderFactory;
import javax.swing.JPanel;

/**
 * A class for clickable panels with x,y-coordinates
 * This is basically a Jpanel with a mouse listener and a color.
 * When this panel is clicked a call to the MouseListener will be made
 * 
 * @author Anna Eilertsen - anna.eilertsen@uib.no 
 * @author Martin Vatshelle - martin.vatshelle@uib.no
 *
 */
public class GamePanel extends JPanel{
	private Color color;
	
	private static final long serialVersionUID = 1L;

	public GamePanel(MouseListener listener) {
		this.color = Color.WHITE;
		//use methods in JPanel to set initial style
		setEnabled(true);
		setBorder(BorderFactory.createLineBorder(Color.GRAY));
		//add mouse listener which calls click method 
		addMouseListener(listener); 
	}

	@Override
	public Dimension getPreferredSize() {
		return new Dimension(3, 3);
	}
	
	@Override
	public Color getBackground() {
		return color;
	}

	/**
	 * Sets the color of this panel.
	 * When the updateUI function is called the color 
	 * will be changed to this color
	 * 
	 * @param color
	 */
	public void setColor(Color color) {
		this.color = color;		
	}
}