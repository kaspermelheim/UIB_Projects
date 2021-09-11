package inf101.v20.gfx;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.IdentityHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Predicate;

import inf101.v20.gfx.gfxmode.BrushPainter;
import inf101.v20.gfx.textmode.Printer;
import inf101.v20.rogue101.AppInfo;
import javafx.beans.value.ObservableValue;
import javafx.geometry.Bounds;
import javafx.scene.Cursor;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.SubScene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.stage.Window;

public class Screen {
	private static final double STD_CANVAS_WIDTH = 1280;
	private static final List<Double> STD_ASPECTS = Arrays.asList(16.0 / 9.0, 16.0 / 10.0, 4.0 / 3.0);
	/** 16:9 */
	public static final int ASPECT_WIDE = 0;
	/** 16:10 */
	public static final int ASPECT_MEDIUM = 1;
	/** 4:3 */
	public static final int ASPECT_CLASSIC = 2;
	public static final int ASPECT_NATIVE = 2;
	private static final int CONFIG_ASPECT_SHIFT = 0;
	/** Screen's initial aspect ratio should be 16:9 */
	public static final int CONFIG_ASPECT_WIDE = 0 << CONFIG_ASPECT_SHIFT;
	/** Screen's initial aspect ratio should be 16:10 */
	public static final int CONFIG_ASPECT_MEDIUM = 1 << CONFIG_ASPECT_SHIFT;
	/** Screen's initial aspect ratio should be 4:3 */
	public static final int CONFIG_ASPECT_CLASSIC = 2 << CONFIG_ASPECT_SHIFT;
	/** Screen's initial aspect ratio should be the same as the device display. */
	public static final int CONFIG_ASPECT_DEVICE = 3 << CONFIG_ASPECT_SHIFT;
	private static final int CONFIG_ASPECT_MASK = 3 << CONFIG_ASPECT_SHIFT;

	private static final int CONFIG_SCREEN_SHIFT = 2;
	/** Screen should start in a window. */
	public static final int CONFIG_SCREEN_WINDOWED = 0 << CONFIG_SCREEN_SHIFT;
	/** Screen should start in a borderless window. */
	public static final int CONFIG_SCREEN_BORDERLESS = 1 << CONFIG_SCREEN_SHIFT;
	/** Screen should start in a transparent window. */
	public static final int CONFIG_SCREEN_TRANSPARENT = 2 << CONFIG_SCREEN_SHIFT;
	/** Screen should start fullscreen. */
	public static final int CONFIG_SCREEN_FULLSCREEN = 3 << CONFIG_SCREEN_SHIFT;
	/**
	 * Screen should start fullscreen, without showing a "Press ESC to exit
	 * fullscreen" hint.
	 */
	public static final int CONFIG_SCREEN_FULLSCREEN_NO_HINT = 4 << CONFIG_SCREEN_SHIFT;
	private static final int CONFIG_SCREEN_MASK = 7 << CONFIG_SCREEN_SHIFT;

	private static final int CONFIG_PIXELS_SHIFT = 5;
	/**
	 * Canvas size / number of pixels should be determined the default way.
	 *
	 * The default is {@link #CONFIG_PIXELS_DEVICE} for
	 * {@link #CONFIG_SCREEN_FULLSCREEN} and {@link #CONFIG_COORDS_DEVICE}, and
	 * {@link #CONFIG_PIXELS_STEP_SCALED} otherwise.
	 */
	public static final int CONFIG_PIXELS_DEFAULT = 0 << CONFIG_PIXELS_SHIFT;
	/**
	 * Canvas size / number of pixels will be an integer multiple or fraction of the
	 * logical canvas size that fits the native display size.
	 *
	 * Scaling by whole integers makes it less likely that we get artifacts from
	 * rounding errors or JavaFX's antialiasing (e.g., fuzzy lines).
	 */
	public static final int CONFIG_PIXELS_STEP_SCALED = 1 << CONFIG_PIXELS_SHIFT;
	/** Canvas size / number of pixels will the same as the native display size. */
	public static final int CONFIG_PIXELS_DEVICE = 2 << CONFIG_PIXELS_SHIFT;
	/**
	 * Canvas size / number of pixels will the same as the logical canvas size
	 * (typically 1280x960).
	 */
	public static final int CONFIG_PIXELS_LOGICAL = 3 << CONFIG_PIXELS_SHIFT;
	/**
	 * Canvas size / number of pixels will be scaled to fit the native display size.
	 */
	public static final int CONFIG_PIXELS_SCALED = 4 << CONFIG_PIXELS_SHIFT;
	private static final int CONFIG_PIXELS_MASK = 7 << CONFIG_PIXELS_SHIFT;

	private static final int CONFIG_COORDS_SHIFT = 8;
	/**
	 * The logical canvas coordinate system will be in logical units (i.e., 1280
	 * pixels wide regardless of how many pixels wide the screen actually is)
	 */
	public static final int CONFIG_COORDS_LOGICAL = 0 << CONFIG_COORDS_SHIFT;
	/** The logical canvas coordinate system will match the display. */
	public static final int CONFIG_COORDS_DEVICE = 1 << CONFIG_COORDS_SHIFT;
	private static final int CONFIG_COORDS_MASK = 1 << CONFIG_COORDS_SHIFT;

	private static final int CONFIG_FLAG_SHIFT = 9;
	public static final int CONFIG_FLAG_HIDE_MOUSE = 1 << CONFIG_FLAG_SHIFT;
	public static final int CONFIG_FLAG_NO_AUTOHIDE_MOUSE = 2 << CONFIG_FLAG_SHIFT;
	public static final int CONFIG_FLAG_DEBUG = 4 << CONFIG_FLAG_SHIFT;
	private static final int CONFIG_FLAG_MASK = 7;

	/**
	 * Get the resolution of this screen, in DPI (pixels per inch).
	 *
	 * @return The primary display's DPI
	 * @see javafx.stage.Screen#getDpi()
	 */
	public static double getDisplayDpi() {
		return javafx.stage.Screen.getPrimary().getDpi();
	}

	/**
	 * Get the height of the display, in pixels.
	 *
	 * <p>
	 * This takes into account such things as toolbars, menus and such (on a
	 * desktop), and pixel density (e.g., on high resolution mobile devices).
	 *
	 * @return Height of the display
	 * @see javafx.stage.Screen#getVisualBounds()
	 */
	public static double getDisplayHeight() {
		return javafx.stage.Screen.getPrimary().getVisualBounds().getHeight();
	}

	/**
	 * Get the width of the display, in pixels.
	 *
	 * <p>
	 * This takes into account such things as toolbars, menus and such (on a
	 * desktop), and pixel density (e.g., on high resolution mobile devices).
	 *
	 * @return Width of the display
	 * @see javafx.stage.Screen#getVisualBounds()
	 */
	public static double getDisplayWidth() {
		return javafx.stage.Screen.getPrimary().getVisualBounds().getWidth();
	}

	/**
	 * Get the native physical height of the screen, in pixels.
	 *
	 * <p>
	 * This will not include such things as toolbars, menus and such (on a desktop),
	 * or take pixel density into account (e.g., on high resolution mobile devices).
	 *
	 * @return Raw width of the display
	 * @see javafx.stage.Screen#getBounds()
	 */
	public static double getRawDisplayHeight() {
		return javafx.stage.Screen.getPrimary().getBounds().getHeight();
	}

	/**
	 * Get the native physical width of the screen, in pixels.
	 *
	 * <p>
	 * This will not include such things as toolbars, menus and such (on a desktop),
	 * or take pixel density into account (e.g., on high resolution mobile devices).
	 *
	 * @return Raw width of the display
	 * @see javafx.stage.Screen#getBounds()
	 */
	public static double getRawDisplayWidth() {
		return javafx.stage.Screen.getPrimary().getBounds().getWidth();
	}

	/**
	 * Start the paint display system.
	 *
	 * This will open a window on the screen, and set up background, text and paint
	 * layers, and listener to handle keyboard input.
	 *
	 * @param stage A JavaFX {@link javafx.stage.Stage}, typically obtained from the
	 *              {@link javafx.application.Application#start(Stage)} method
	 * @return A screen for drawing on
	 */
	public static Screen startPaintScene(Stage stage) {
		return startPaintScene(stage, CONFIG_SCREEN_FULLSCREEN_NO_HINT);
	}

	/**
	 * Start the paint display system.
	 *
	 * This will open a window on the screen, and set up background, text and paint
	 * layers, and listener to handle keyboard input.
	 *
	 * @param stage A JavaFX {@link javafx.stage.Stage}, typically obtained from the
	 *              {@link javafx.application.Application#start(Stage)} method
	 * @return A screen for drawing on
	 */
	public static Screen startPaintScene(Stage stage, int configuration) {
		int configAspect = (configuration & CONFIG_ASPECT_MASK);
		int configScreen = (configuration & CONFIG_SCREEN_MASK);
		int configPixels = (configuration & CONFIG_PIXELS_MASK);
		int configCoords = (configuration & CONFIG_COORDS_MASK);
		int configFlags = (configuration & CONFIG_FLAG_MASK);
		boolean debug = (configFlags & CONFIG_FLAG_DEBUG) != 0;
		if (configPixels == CONFIG_PIXELS_DEFAULT) {
			if (configCoords == CONFIG_COORDS_DEVICE || configScreen == CONFIG_SCREEN_FULLSCREEN)
				configPixels = CONFIG_PIXELS_DEVICE;
			else
				configPixels = CONFIG_PIXELS_STEP_SCALED;
		}
		double rawWidth = getRawDisplayWidth();
		double rawHeight = getRawDisplayHeight();
		double width = getDisplayWidth() - 40;
		double height = getDisplayHeight() - 100;
		double canvasAspect = configAspect == CONFIG_ASPECT_DEVICE ? rawWidth / rawHeight
				: STD_ASPECTS.get(configAspect);
		double xScale = (height * canvasAspect) / Screen.STD_CANVAS_WIDTH;
		double yScale = (width / canvasAspect) / (Screen.STD_CANVAS_WIDTH / canvasAspect);
		double scale = Math.min(xScale, yScale);
		if (configPixels == CONFIG_PIXELS_STEP_SCALED) {
			if (scale > 1.0)
				scale = Math.max(1, Math.floor(scale));
			else if (scale < 1.0)
				scale = 1 / Math.max(1, Math.floor(1 / scale));
		}
		double winWidth = Math.floor(Screen.STD_CANVAS_WIDTH * scale);
		double winHeight = Math.floor((Screen.STD_CANVAS_WIDTH / canvasAspect) * scale);
		double canvasWidth = Screen.STD_CANVAS_WIDTH;
		double canvasHeight = Math.floor(3 * Screen.STD_CANVAS_WIDTH / 4);
		double pixWidth = canvasWidth;
		double pixHeight = canvasHeight;
		if (configPixels == CONFIG_PIXELS_SCALED || configPixels == CONFIG_PIXELS_STEP_SCALED) {
			pixWidth *= scale;
			pixHeight *= scale;
		} else if (configPixels == CONFIG_PIXELS_DEVICE) {
			pixWidth = rawWidth;
			pixHeight = rawHeight;
		}
		if (configCoords == CONFIG_COORDS_DEVICE) {
			canvasWidth = pixWidth;
			canvasHeight = pixHeight;
		}
		if (debug) {
			System.out.printf("Screen setup:%n");
			System.out.printf("  Display: %.0fx%.0f (raw %.0fx%.0f)%n", width, height, rawWidth, rawHeight);
			System.out.printf("  Window:  %.0fx%.0f%n", winWidth, winHeight);
			System.out.printf("  Canvas:  physical %.0fx%.0f, logical %.0fx%.0f%n", pixWidth, pixHeight, canvasWidth,
					canvasHeight);
			System.out.printf("  Aspect:  %.5f   Scale: %.5f%n", canvasAspect, scale);
		}
		Group root = new Group();
		Scene scene = new Scene(root, winWidth, winHeight, Color.BLACK);
		stage.setScene(scene);
		stage.setTitle(AppInfo.APP_NAME);
		if ((configFlags & CONFIG_FLAG_HIDE_MOUSE) != 0) {
			scene.setCursor(Cursor.NONE);
		}

		Screen pScene = new Screen(scene.getWidth(), scene.getHeight(), //
				pixWidth, pixHeight, //
				canvasWidth, canvasHeight);
		pScene.subScene.widthProperty().bind(scene.widthProperty());
		pScene.subScene.heightProperty().bind(scene.heightProperty());
		pScene.debug = debug;
		pScene.hideFullScreenMouseCursor = (configFlags & CONFIG_FLAG_NO_AUTOHIDE_MOUSE) == 0;
		root.getChildren().add(pScene.subScene);

		boolean[] suppressKeyTyped = { false };

		switch (configScreen) {
		case CONFIG_SCREEN_WINDOWED:
			break;
		case CONFIG_SCREEN_BORDERLESS:
			stage.initStyle(StageStyle.UNDECORATED);
			break;
		case CONFIG_SCREEN_TRANSPARENT:
			stage.initStyle(StageStyle.TRANSPARENT);
			break;
		case CONFIG_SCREEN_FULLSCREEN_NO_HINT:
			stage.setFullScreenExitHint("");
			// fall-through
		case CONFIG_SCREEN_FULLSCREEN:
			stage.setFullScreen(true);
			break;
		}
		scene.setOnKeyPressed((KeyEvent event) -> {
			if (!event.isConsumed() && pScene.keyOverride != null && pScene.keyOverride.test(event)) {
				event.consume();
			}
			if (!event.isConsumed() && pScene.minimalKeyHandler(event)) {
				event.consume();
			}
			if (!event.isConsumed() && pScene.keyPressedHandler != null && pScene.keyPressedHandler.test(event)) {
				event.consume();
			}
			if (pScene.logKeyEvents)
				System.err.println(event);
			suppressKeyTyped[0] = event.isConsumed();
		});
		scene.setOnKeyTyped((KeyEvent event) -> {
			if (suppressKeyTyped[0]) {
				suppressKeyTyped[0] = false;
				event.consume();
			}
			if (!event.isConsumed() && pScene.keyTypedHandler != null && pScene.keyTypedHandler.test(event)) {
				event.consume();
			}
			if (pScene.logKeyEvents)
				System.err.println(event);
		});
		scene.setOnKeyReleased((KeyEvent event) -> {
			suppressKeyTyped[0] = false;
			if (!event.isConsumed() && pScene.keyReleasedHandler != null && pScene.keyReleasedHandler.test(event)) {
				event.consume();
			}
			if (pScene.logKeyEvents)
				System.err.println(event);
		});
		return pScene;
	}

	private final double rawCanvasWidth;
	private final double rawCanvasHeight;
	private boolean logKeyEvents = false;
	private final SubScene subScene;
	private final List<Canvas> canvases = new ArrayList<>();
	private final Map<IPaintLayer, Canvas> layerCanvases = new IdentityHashMap<>();
	private final Canvas background;
	private final Group root;
	private Paint bgColor = Color.CORNFLOWERBLUE;
	private int aspect = 0;
	private double scaling = 0;
	private double currentScale = 1.0;
	private double currentFit = 1.0;
	private double resolutionScale = 1.0;
	private int maxScale = 1;
	private Predicate<KeyEvent> keyOverride = null;

	private Predicate<KeyEvent> keyPressedHandler = null;

	private Predicate<KeyEvent> keyTypedHandler = null;

	private Predicate<KeyEvent> keyReleasedHandler = null;

	private boolean debug = true;

	private List<Double> aspects;

	private boolean hideFullScreenMouseCursor = true;

	private Cursor oldCursor;

	public Screen(double width, double height, double pixWidth, double pixHeight, double canvasWidth,
			double canvasHeight) {
		root = new Group();
		subScene = new SubScene(root, Math.floor(width), Math.floor(height));
		resolutionScale = pixWidth / canvasWidth;
		this.rawCanvasWidth = Math.floor(pixWidth);
		this.rawCanvasHeight = Math.floor(pixHeight);
		double aspectRatio = width / height;
		aspect = 0;
		for (double a : STD_ASPECTS)
			if (Math.abs(aspectRatio - a) < 0.01) {
				break;
			} else {
				aspect++;
			}
		aspects = new ArrayList<>(STD_ASPECTS);
		if (aspect >= STD_ASPECTS.size()) {
			aspects.add(aspectRatio);
		}
		background = new Canvas(rawCanvasWidth, rawCanvasHeight);
		background.getGraphicsContext2D().scale(resolutionScale, resolutionScale);
		setBackground(bgColor);
		clearBackground();
		root.getChildren().add(background);
		subScene.layoutBoundsProperty()
				.addListener((ObservableValue<? extends Bounds> observable, Bounds oldBounds, Bounds bounds) -> {
					recomputeLayout(false);
				});
	}

	public void clearBackground() {
		getBackgroundContext().setFill(bgColor);
		getBackgroundContext().fillRect(0.0, 0.0, background.getWidth(), background.getHeight());
	}

	public BrushPainter createPainter() {
		Canvas canvas = new Canvas(rawCanvasWidth, rawCanvasHeight);
		canvas.getGraphicsContext2D().scale(resolutionScale, resolutionScale);
		canvases.add(canvas);
		root.getChildren().add(canvas);
		return new BrushPainter(this, canvas);
	}

	public Printer createPrinter() {
		Canvas canvas = new Canvas(rawCanvasWidth, rawCanvasHeight);
		canvas.getGraphicsContext2D().scale(resolutionScale, resolutionScale);
		canvases.add(canvas);
		root.getChildren().add(canvas);
		return new Printer(this, canvas);
	}

	public void cycleAspect() {
		aspect = (aspect + 1) % aspects.size();
		recomputeLayout(false);
	}

	public void fitScaling() {
		scaling = 0;
		recomputeLayout(true);
	}

	public int getAspect() {
		return aspect;
	}

	public GraphicsContext getBackgroundContext() {
		return background.getGraphicsContext2D();
	}

	public double getHeight() {
		return Math.floor(getRawHeight() / resolutionScale);
	}

	/** @return the keyOverride */
	public Predicate<KeyEvent> getKeyOverride() {
		return keyOverride;
	}

	/** @return the keyHandler */
	public Predicate<KeyEvent> getKeyPressedHandler() {
		return keyPressedHandler;
	}

	/** @return the keyReleasedHandler */
	public Predicate<KeyEvent> getKeyReleasedHandler() {
		return keyReleasedHandler;
	}

	/** @return the keyTypedHandler */
	public Predicate<KeyEvent> getKeyTypedHandler() {
		return keyTypedHandler;
	}

	public double getRawHeight() {
		return Math.floor(rawCanvasWidth / aspects.get(aspect));
	}

	public double getRawWidth() {
		return rawCanvasWidth;
	}

	public double getWidth() {
		return Math.floor(getRawWidth() / resolutionScale);
	}

	public void hideMouseCursor() {
		subScene.getScene().setCursor(Cursor.NONE);
	}

	public boolean isFullScreen() {
		Window window = subScene.getScene().getWindow();
		if (window instanceof Stage)
			return ((Stage) window).isFullScreen();
		else
			return false;
	}

	public boolean minimalKeyHandler(KeyEvent event) {
		KeyCode code = event.getCode();
		if (event.isShortcutDown()) {
			if (code == KeyCode.Q) {
				System.exit(0);
			} else if (code == KeyCode.PLUS) {
				zoomIn();
				return true;
			} else if (code == KeyCode.MINUS) {
				zoomOut();
				return true;
			}
		} else if (!(event.isAltDown() || event.isControlDown() || event.isMetaDown() || event.isShiftDown())) {
			if (code == KeyCode.F11) {
				setFullScreen(!isFullScreen());
				return true;
			}
		}

		return false;
	}

	public void moveToBack(IPaintLayer layer) {
		Canvas canvas = layerCanvases.get(layer);
		if (canvas != null) {
			canvas.toBack();
			background.toBack();
		}
	}

	public void moveToFront(IPaintLayer layer) {
		Canvas canvas = layerCanvases.get(layer);
		if (canvas != null) {
			canvas.toFront();
		}
	}

	private void recomputeLayout(boolean resizeWindow) {
		double xScale = subScene.getWidth() / getRawWidth();
		double yScale = subScene.getHeight() / getRawHeight();
		double xMaxScale = getDisplayWidth() / getRawWidth();
		double yMaxScale = getDisplayHeight() / getRawHeight();
		currentFit = Math.min(xScale, yScale);
		maxScale = (int) Math.max(1, Math.ceil(Math.min(xMaxScale, yMaxScale)));
		currentScale = scaling == 0 ? currentFit : scaling;

		if (resizeWindow) {
			Scene scene = subScene.getScene();
			Window window = scene.getWindow();
			double hBorder = window.getWidth() - scene.getWidth();
			double vBorder = window.getHeight() - scene.getHeight();
			double myWidth = getRawWidth() * currentScale;
			double myHeight = getRawHeight() * currentScale;
			if (debug)
				System.out.printf(
						"Resizing before: screen: %1.0fx%1.0f, screen: %1.0fx%1.0f, scene: %1.0fx%1.0f, window: %1.0fx%1.0f,%n border: %1.0fx%1.0f, new window size: %1.0fx%1.0f, canvas size: %1.0fx%1.0f%n", //
						javafx.stage.Screen.getPrimary().getVisualBounds().getWidth(),
						javafx.stage.Screen.getPrimary().getVisualBounds().getHeight(), subScene.getWidth(),
						subScene.getHeight(), scene.getWidth(), scene.getHeight(), window.getWidth(),
						window.getHeight(), hBorder, vBorder, myWidth, myHeight, getRawWidth(), getRawHeight());
			// this.setWidth(myWidth);
			// this.setHeight(myHeight);
			window.setWidth(myWidth + hBorder);
			window.setHeight(myHeight + vBorder);
			if (debug)
				System.out.printf(
						"Resizing after : screen: %1.0fx%1.0f, screen: %1.0fx%1.0f, scene: %1.0fx%1.0f, window: %1.0fx%1.0f,%n border: %1.0fx%1.0f, new window size: %1.0fx%1.0f, canvas size: %1.0fx%1.0f%n",
						javafx.stage.Screen.getPrimary().getVisualBounds().getWidth(),
						javafx.stage.Screen.getPrimary().getVisualBounds().getHeight(), subScene.getWidth(),
						subScene.getHeight(), scene.getWidth(), scene.getHeight(), window.getWidth(),
						window.getHeight(), hBorder, vBorder, myWidth, myHeight, getRawWidth(), getRawHeight());
		}

		if (debug)
			System.out.printf("Rescaling: subscene %1.2fx%1.2f, scale %1.2f, aspect %.4f (%d), canvas %1.0fx%1.0f%n",
					subScene.getWidth(), subScene.getHeight(), currentScale, aspects.get(aspect), aspect, getRawWidth(),
					getRawHeight());
		for (Node n : root.getChildren()) {
			n.relocate(Math.floor(subScene.getWidth() / 2),
					Math.floor(subScene.getHeight() / 2 + (rawCanvasHeight - getRawHeight()) * currentScale / 2));
			n.setTranslateX(-Math.floor(rawCanvasWidth / 2));
			n.setTranslateY(-Math.floor(rawCanvasHeight / 2));
			if (debug)
				System.out.printf(" *  layout %1.2fx%1.2f, translate %1.2fx%1.2f%n", n.getLayoutX(), n.getLayoutY(),
						n.getTranslateX(), n.getTranslateY());
			n.setScaleX(currentScale);
			n.setScaleY(currentScale);
		}
	}

	public void setAspect(int aspect) {
		this.aspect = (aspect) % aspects.size();
		recomputeLayout(false);
	}

	public void setBackground(Paint bgColor) {
		this.bgColor = bgColor;
		subScene.setFill(bgColor instanceof Color ? ((Color) bgColor).darker() : bgColor);
	}

	public void setFullScreen(boolean fullScreen) {
		Window window = subScene.getScene().getWindow();
		if (window instanceof Stage) {
			((Stage) window).setFullScreenExitHint("");
			((Stage) window).setFullScreen(fullScreen);
			if (hideFullScreenMouseCursor) {
				if (fullScreen) {
					oldCursor = subScene.getScene().getCursor();
					subScene.getScene().setCursor(Cursor.NONE);
				} else if (oldCursor != null) {
					subScene.getScene().setCursor(oldCursor);
					oldCursor = null;
				} else {
					subScene.getScene().setCursor(Cursor.DEFAULT);
				}
			}
		}
	}

	public void setHideFullScreenMouseCursor(boolean hideIt) {
		if (hideIt != hideFullScreenMouseCursor && isFullScreen()) {
			if (hideIt) {
				oldCursor = subScene.getScene().getCursor();
				subScene.getScene().setCursor(Cursor.NONE);
			} else if (oldCursor != null) {
				subScene.getScene().setCursor(oldCursor);
				oldCursor = null;
			} else {
				subScene.getScene().setCursor(Cursor.DEFAULT);
			}
		}
		hideFullScreenMouseCursor = hideIt;
	}

	/**
	 * @param keyOverride the keyOverride to set
	 */
	public void setKeyOverride(Predicate<KeyEvent> keyOverride) {
		this.keyOverride = keyOverride;
	}

	/**
	 * @param keyHandler the keyHandler to set
	 */
	public void setKeyPressedHandler(Predicate<KeyEvent> keyHandler) {
		this.keyPressedHandler = keyHandler;
	}

	/**
	 * @param keyReleasedHandler the keyReleasedHandler to set
	 */
	public void setKeyReleasedHandler(Predicate<KeyEvent> keyReleasedHandler) {
		this.keyReleasedHandler = keyReleasedHandler;
	}

	/**
	 * @param keyTypedHandler the keyTypedHandler to set
	 */
	public void setKeyTypedHandler(Predicate<KeyEvent> keyTypedHandler) {
		this.keyTypedHandler = keyTypedHandler;
	}

	public void setMouseCursor(Cursor cursor) {
		subScene.getScene().setCursor(cursor);
	}

	public void showMouseCursor() {
		subScene.getScene().setCursor(Cursor.DEFAULT);
	}

	public void zoomCycle() {
		scaling++;
		if (scaling > maxScale)
			scaling = ((int) scaling) % maxScale;
		recomputeLayout(true);
	}

	public void zoomFit() {
		scaling = 0;
		recomputeLayout(false);
	}

	public void zoomIn() {
		scaling = Math.min(10, currentScale + 0.2);
		recomputeLayout(false);
	}

	public void zoomOne() {
		scaling = 1;
		recomputeLayout(false);
	}

	public void zoomOut() {
		scaling = Math.max(0.1, currentScale - 0.2);
		recomputeLayout(false);
	}
}
