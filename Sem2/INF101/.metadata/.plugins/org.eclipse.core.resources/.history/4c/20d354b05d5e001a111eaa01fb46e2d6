package inf101.v20.rogue101.objects;

import inf101.v20.grid.GridDirection;
import inf101.v20.grid.ILocation;
import inf101.v20.rogue101.game.Game;
import inf101.v20.rogue101.game.ItemFactory;
import inf101.v20.rogue101.map.MapReader;
import javafx.scene.input.KeyCode;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.List;

class PlayerTest {

    private Game board;
    private IPlayer player;
    private ILocation loc;

    @BeforeEach
    void beforeEach() {
        board = new Game(MapReader.TEST_MAP);
        player = (IPlayer) board.setCurrent(3, 2);
        loc = board.getLocation();
    }

    @Test
    void PlayerDoesMoves() {
        player.keyPressed(board, KeyCode.UP);
        assertEquals(loc.go(GridDirection.NORTH), board.getLocation());
    }

    @Test
    void PlayerTakesDamage() {
        var hp = player.getCurrentHealth();
        player.handleDamage(10);
        assertNotEquals(hp, player.getCurrentHealth());
    }

    @Test
    void PlayerCanPickUpAndDropItem() {
        loc = board.getMap().getLocation(3, 1);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.UP);
        assertEquals(2, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.P);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.D);
        assertEquals(2, board.getMap().getAll(loc).size());
    }
    
    @Test
    void PlayerPickUpHasItem() {
        loc = board.getMap().getLocation(3, 1);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.UP);
        assertEquals(2, board.getMap().getAll(loc).size());

        List<IItem> localNonActorItemList = board.getLocalNonActorItems();
		assertFalse(localNonActorItemList.isEmpty(), "Something is wrong with the test object, there are no items to pick up.");

		IItem localItem = localNonActorItemList.get(0);
		
        player.keyPressed(board, KeyCode.P);
        assertTrue(player.hasItem(localItem), "Player should have picked up the item: " + localItem);
    }

    @Test
    void PlayerPickUpDropHasItem() {
        loc = board.getMap().getLocation(3, 1);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.UP);
        assertEquals(2, board.getMap().getAll(loc).size());

        List<IItem> localNonActorItemList = board.getLocalNonActorItems();
		assertFalse(localNonActorItemList.isEmpty(), "Something is wrong with the test object, there are no items to pick up.");

		IItem localItem = localNonActorItemList.get(0);
		
        player.keyPressed(board, KeyCode.P);
        assertTrue(player.hasItem(localItem), "Player should have picked up the item: " + localItem);
        player.keyPressed(board, KeyCode.D);
        assertFalse(player.hasItem(localItem), "Player should have dropped the item: " + localItem);
    }
    
    @Test
    void PlayerPickUpHasItemReferenceEqualityItem() {
        loc = board.getMap().getLocation(3, 1);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.UP);
        assertEquals(2, board.getMap().getAll(loc).size());

        List<IItem> localNonActorItemList = board.getLocalNonActorItems();
		assertFalse(localNonActorItemList.isEmpty(), "Something is wrong with the test object, there are no items to pick up.");

		IItem localItem = localNonActorItemList.get(0);
		IItem notLocalItem = ItemFactory.createItem(localItem.getSymbol());
        player.keyPressed(board, KeyCode.P);
        assertTrue(player.hasItem(localItem), "Player should have picked up the item: " + localItem);
        assertFalse(player.hasItem(notLocalItem), "Wrong item equality.");
    }
    
    @Test
    void PlayerCanPickUpAndDropMoreItems() {
        loc = board.getMap().getLocation(3, 1);

        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.UP);
        assertEquals(2, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.P);
        assertEquals(1, board.getMap().getAll(loc).size());

        board.doTurn();
        player.keyPressed(board, KeyCode.RIGHT);
        loc = board.getLocation();
        assertEquals(2, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.P);
        assertEquals(1, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.D);
        assertEquals(2, board.getMap().getAll(loc).size());

        player.keyPressed(board, KeyCode.D);
        assertEquals(3, board.getMap().getAll(loc).size());
    }
}
