
package dsa.linked_list;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class LinkedList<T>{
    Node head;

    class Node {
        T data;
        Node next;

        Node(T d){
            data = d;
            next = null;
        }
    }

    LinkedList(Node firstNode){
        head = firstNode;
    }

    LinkedList(T value){
        head = new Node(value);
    }


    LinkedList(List<T> values){
        head = new Node(values.get(0));
        Node prevNode = head;
        for (int i=1; i < values.size(); i++) {
            prevNode.next = new Node(values.get(i));
            prevNode = prevNode.next;
        };
    }

    public void insert(T newData){
        Node newNode =new Node(newData);
        newNode.next = head;
        head = newNode;
    }

    public void insert(T newData, int position){
        /*
         * Inserts a node with given value at given position
         * 
         * @param newData The new data to be inserted
         * @param position Position of insertion. 1-indexed
         */
        if(position == 1){
            insert(newData);
            return;
        }
        Node currNode = head;
        Node prevNode = null;
        Node newNode = new Node(newData);
        for(int i=1; i < position; i++){
            prevNode = currNode;
            currNode = currNode.next;
        }
        newNode.next = currNode;
        if(prevNode != null){
            prevNode.next = newNode;
        }
    }

    public ArrayList<T> toList(){
        ArrayList<T> result = new ArrayList<>();
        Node currNode = head;
        while(currNode!=null){
            result.add(currNode.data);
            currNode = currNode.next;
        }
        return result;
    }

    public static void main(String[] args) {
        LinkedList<String> lls = new LinkedList<String>(Arrays.asList("Hello", "World"));
        lls.insert("Foo");
        lls.insert("Bar", 2);
        lls.insert("There", 5);
        System.out.println(lls.toList());
    }

}

// class LinkedList {
//     Node head; // head of the list

//     /* Linked list Node */
//     class Node {
//         int data;
//         Node next;

//         // Constructor to create a new node
//         Node(int d) {
//             data = d;
//             next = null;
//         }
//     }

//     // Method to insert a new node
//     public void push(int new_data) {
//         Node new_node = new Node(new_data);
//         new_node.next = head;
//         head = new_node;
//     }

//     // Method to print the linked list
//     public void printList() {
//         Node tnode = head;
//         while (tnode != null) {
//             System.out.print(tnode.data + " ");
//             tnode = tnode.next;
//         }
//     }

//     // Method to delete a node in the LinkedList
//     public void deleteNode(int key) {
//         Node temp = head, prev = null;

//         // If head node itself holds the key to be deleted
//         if (temp != null && temp.data == key) {
//             head = temp.next; // Changed head
//             return;
//         }

//         // Search for the key to be deleted, keep track of the
//         // previous node as we need to change 'prev.next'
//         while (temp != null && temp.data != key) {
//             prev = temp;
//             temp = temp.next;
//         }

//         // If key was not present in linked list
//         if (temp == null)
//             return;

//         // Unlink the node from linked list
//         prev.next = temp.next;
//     }

//     // Method to delete a node in the LinkedList at a given position
//     public void deleteNodeAtPosition(int position) {
//         // If linked list is empty
//         if (head == null)
//             return;

//         // Store head node
//         Node temp = head;

//         // If head needs to be removed
//         if (position == 0) {
//             head = temp.next; // Change head
//             return;
//         }

//         // Find previous node of the node to be deleted
//         for (int i = 0; temp != null && i < position - 1; i++)
//             temp = temp.next;

//         // If position is more than number of nodes
//         if (temp == null || temp.next == null)
//             return;

//         // Node temp->next is the node to be deleted
//         // Store pointer to the next of the node to be
//         // deleted
//         Node next = temp.next.next;
//     }
// }