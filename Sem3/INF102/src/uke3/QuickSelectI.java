package uke3;

import java.util.List;

public interface QuickSelectI {

    /*
    Should return the kth smallest item in a list (1-indexed i.e 1th item is list.get(0)), f.ex
    when when ran as findKth([0,5,2,4,1,3], 3), it should return 2. When k is out of range you  	should throw the appropriate exception:
    	k < 1 -> IllegalArgumentException
    	k > list.size() -> IndexOutOfBoundsException
     */
    public <T extends Comparable<? super T>> T findKth(List<T> list, int k);
}

