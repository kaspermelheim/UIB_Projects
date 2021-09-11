package uke2;

import java.util.List;

public interface BinarySearchI {
    <T extends Comparable<T>> int search(List<T> list, T item);
}
