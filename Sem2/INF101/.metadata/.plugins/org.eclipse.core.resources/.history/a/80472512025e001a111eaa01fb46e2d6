package inf101.v20.rogue101.map;

import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

import inf101.v20.grid.IGrid;
import inf101.v20.grid.Grid;

/**
 * A class to read a map from a file. After the file is read, the map is stored
 * as an {@link #IGrid} whose entries are characters. This can then be used to
 * be passed to the constructor in {@link #BDMap}.
 *
 * The first line of the file should could contain two numbers. First the width
 * and then the height of the map. After that follows a matrix of characters
 * describing which object goes where in the map. '*' for wall, ' ' for empty,
 * 'P' for the player, 'b' for a bug, 'r' for a rock, and '#' for sand. For
 * example
 *
 * <pre>
 * {@code
 * 5 6
 * *## p
 * * rr#
 * *####
 * *   *
 * *   d
 *    b
 * }
 * </pre>
 *
 * @author larsjaffke (original boulderdash version, 2017)
 * @author anya (Rogue101 update, 2018)
 */
public class MapReader {

	public static String BUILTIN_MAP = "40 20\n" //
			+ "########################################\n" //
			+ "#...... ..C.R ......R.R......... ..R...#\n" //
			+ "#.R@R...... ..........RC..R...... ... .#\n" //
			+ "#.......... ..R......R.R..R........R...#\n" //
			+ "#R. R......... R..R.........R......R.RR#\n" //
			+ "#... ..R........R......R. R........R.RR#\n" //
			+ "###############################....R..R#\n" //
			+ "#. ...R..C. ..R.R..........C.RC....... #\n" //
			+ "#..C.....R..... ........RR R..R.....R..#\n" //
			+ "#...R..R.R....G.........R .R..R........#\n" //
			+ "#.R.....R........RRR.......R.. .C....R.#\n" //
			+ "#.C.. ..R.  ..G..R.RC..C....R...R..C. .#\n" //
			+ "#. R..............R R..R........C.....R#\n" //
			+ "#........###############################\n" //
			+ "# R.........R...C....R.....R...R.......#\n" //
			+ "# R......... R..R.G......R......R.RR..*#\n" //
			+ "#. ..R........R.....R.  ....C...R.RR...#\n" //
			+ "#....RC..R........R......R.RCA.....R...#\n" //
			+ "#.C.... ..... ......... .R..R....R...R.#\n" //
			+ "########################################\n" //
	;
	public static String mapTrap(Character sym) {
		return "3 3\n" //
			 + "###\n" //
			 + "#"+ sym+"#\n" //
			 + "###\n";
	}

	public static String playerTrapWith(Character sym) {
		return "5 5\n" //
				+ "#####\n" //
				+ "#   #\n" //
				+ "# @ #\n" //
				+ "#"+sym+"  #\n" //
				+ "#####\n" //
		;
	}

	public static String TEST_MAP = "40 5\n" //
			+ "########################################\n" //
			+ "#...... ..C.R ......R.R......... ..R...#\n" //
			+ "#.R@R...... ..........RC..R...... ... .#\n" //
			+ "#... ..R........R......R. R........R.RR#\n" //
			+ "########################################\n" //
	;

	
	public static String CARROT_HUNT = "40 10\n" //
			+ "########################################\n" //
			+ "#...... ..C.. ......C.C....#.... ..CCCC#\n" //
			+ "#.  RC   .. ....   .####..C#..... .CCCC#\n" //
			+ "#       ...........  #.C. C#.......CCCC#\n" //
			+ "#      C..........C###.C.###.......CCCC#\n" //
			+ "#      C...#....C..#C# ............CCCC#\n" //
			+ "#      C...#....C..###.C..##.......CCCC#\n" //
			+ "#      C ..#....C..  #.C. C#C......CCCC#\n" //
			+ "#        .. ....C..  #.C. C#.......CCCC#\n" //
			+ "########################################\n" //
	;	
	/**
	 * This method fills the previously initialized {@link #symbolMap} with the
	 * characters read from the file.
	 */
	private static void fillMap(IGrid<String> symbolMap, Scanner in) {
		// we need to store x and y in an object (array) rather than as variables,
		// otherwise the foreach and lambda below won't work.
		int[] xy = new int[2]; // xy[0] is x, xy[1] is y
		xy[1] = 0;
		while (in.hasNextLine()) {
			xy[0] = 0;
			in.nextLine().codePoints().forEach((codePoint) -> {
				if (xy[0] < symbolMap.getWidth())
					symbolMap.set(xy[0]++, xy[1], String.valueOf(Character.toChars(codePoint)));
			});
			xy[1]++;
		}
	}

	/**
	 * Load map from file.
	 * <p>
	 * Files are search for relative to the folder containing the MapReader class.
	 *
	 * @return the dungeon map as a grid of characters read from the file, or null
	 *         if it failed
	 */
	public static IGrid<String> readFile(String path) {
		IGrid<String> symbolMap = null;
		InputStream stream = MapReader.class.getResourceAsStream(path);
		if (stream == null)
			return null;
		try (Scanner in = new Scanner(stream, "UTF-8")) {
			int width = in.nextInt();
			int height = in.nextInt();
			// System.out.println(width + " " + height);
			symbolMap = new Grid<String>(width, height, " ");
			in.nextLine();
			fillMap(symbolMap, in);
		}
		try {
			stream.close();
		} catch (IOException e) {
		}
		return symbolMap;
	}

	/**
	 * @return the dungeon map as a grid of characters read from the input string,
	 *         or null if it failed
	 */
	public static IGrid<String> readString(String input) {
		IGrid<String> symbolMap = null;
		try (Scanner in = new Scanner(input)) {
			int width = in.nextInt();
			int height = in.nextInt();
			symbolMap = new Grid<String>(width, height, " ");
			in.nextLine();
			fillMap(symbolMap, in);
		}
		return symbolMap;
	}
}
