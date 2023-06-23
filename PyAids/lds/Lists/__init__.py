"""
Data strucutres related to lists.

- Linked List(head)
    Create a linked list with the following methods:
        1. insert_begin(value)
            inserts the value in the beginning of the list.
        2. insert_end(value)
            inserts the value in the end of the list.
        3. insert(value, index)
            inserts the value at the given index.
        4. search(value)
            returns True if the value is in the list, False otherwise.
        5. index(value)
            retruns the index of the value if it is in the list, None otherwise.
        6. delete_begin()
            deletes the first item in the list
        7. delete_end()
            deletes the last item in the list
        8. delete_index(index)
            deletes the item at the given index
        9. delete_value(value)
            deletes the first occurence of the value in the list
        10. update(index, value, next_n)
            updates the value and next_node(default is None) of the node at the given index
        11. reverse()
            reverses the list
        12. concatenate(other)
            concatenates the other list to the current list at the end
        13. swap(index1, index2)
            swaps the values at the given indices
        14. sorted(ascending)
            returns true if the list is sorted in ascending order, false otherwise
        15. sort(ascending)
            sorts the list in ascending order if ascending is True, descending order otherwise
        
        - Custom methods to convert the list
        
        17. to_list()
            returns a list of the values in the linked list
        18. create_from_list(array)
            creates a linked list from the given array
        19. create_from_dict(dictionary)
            creates a linked list from the given dictionary with the keys as values and values as next node
        
        
- Doubly Linked List(head)

    Create a doubly linked list with the following methods:
        1. insert_end(value)
            inserts the value in the end of the list.
        2. insert_begin(value)
            
- Node

"""