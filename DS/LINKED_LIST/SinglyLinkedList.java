public class SinglyLinkedList {
    Node head;

    void add(int data){
        if(head == null){
            head  = new Node(data);
        }else{
            Node n1 = head;
            while(n1.next!=null){
                n1 = n1.next;
            }
            Node n2 = new Node(data);
            n1.next = n2;
        }
    }

    void disp(){
        Node n1 = head;
        while(n1!=null){
            System.out.print(n1.data + " -> ");
            n1 = n1.next;
        }
        System.out.println();
    }

    void reverse(){
        Node n1 = head, prev = null;
        while(n1!=null){
            Node nextNode = n1.next;
            n1.next = prev;
            prev = n1;
            n1 = nextNode;
        }
        head = prev;
    }

    public static void main(String[] args){
        SinglyLinkedList sl  =new SinglyLinkedList();
        sl.add(30); sl.add(40); sl.add(56); sl.add(90);
        sl.disp();
        sl.reverse();
        sl.disp();
    }
}

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
    }
}

