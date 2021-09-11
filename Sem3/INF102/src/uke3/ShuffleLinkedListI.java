package uke3;

import java.util.LinkedList;

public interface ShuffleLinkedListI {

    /*
    Should leave <list> in a shuffled state
     */
    public <T extends Comparable<? super T>> void shuffle(LinkedList<T> list);
}
