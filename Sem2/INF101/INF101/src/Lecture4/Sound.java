package Lecture4;

import java.io.File;
import javax.sound.sampled.*;

public class Sound
{
	public static void play(String filename)
	{
		File sound = new File(filename);
		try{
			Clip clip = AudioSystem.getClip();
			clip.open(AudioSystem.getAudioInputStream(sound));
			clip.start();
			Thread.sleep(clip.getMicrosecondLength()/1000);
		}catch(Exception e)
		{
			System.out.println("Could not play sound");
		}
	}
}