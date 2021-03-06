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

    void addSorted(int data){
        if(head == null){
            head = new Node(data);
        }else{
            Node prev = null,n1= head;
            while(n1!=null){
                if(n1.data>data)
                    break;
                prev = n1;
                n1 = n1.next;
            }
            Node n2 = new Node(data);
            n2.next = n1;
            if(prev == null){
                head = n2;
            }else{
                prev.next = n2;
            }
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

     void addFirst(int data){
        if(head == null){
            head = new Node(data);
        }else{
            Node n1 = new Node(data);
            n1.next = head;
            head = n1;
        }
    }

    void addLast(int data){
        if(head == null){
            head = new Node(data);
        }else{
            Node n1 = head;
            while(n1.next!=null){
                n1 = n1.next;
            }
            Node n2 = new Node(data);
            n1.next = n2;
        }
    }

    void createLoopedList(){
        head = new Node(23);
        head.next = new Node(76);
        head.next.next = new Node(34);
        head.next.next.next = new Node(87);
        head.next.next.next.next = new Node(39);
        head.next.next.next.next.next = head.next.next;
    }

    void detectCycle(){
        Node s = head, f = head;
        while(s!=null && f!=null && f.next!=null){
            s = s.next;
            f = f.next.next;
            if(s == f){
                System.out.println("found loop");
                return;
            }
        }
        System.out.println("no loops");
    }

    boolean search(Node n1, int data){
        boolean found = false;
        if(n1!=null){
            if(n1.data == data){
                found = true;
            }else{
                found = search(n1.next, data);
            }
        }
        return found;
    }

     Node mergeSort(Node head) {
        if(head == null || head.next == null)
            return head;
        Node mid = getMid(head), second_head = mid.next; 
        mid.next = null;
        return merge(mergeSort(head), mergeSort(second_head));
    }

    Node merge(Node head1, Node head2){
        Node result = new Node(0), current = result;
        while(head1 != null && head2 != null) {
            if(head1.data< head2.data) {
                current.next = head1;
                head1 = head1.next;
            }else {
                current.next = head2;
                head2 = head2.next;
            }
            current = current.next;
        }
        if(head1 != null) current.next = head1;
        if(head2 != null) current.next = head2;
        return result.next;
    }

    Node getMid(Node head) {
        Node slow = head, fast = head.next;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public static void main(String[] args){
        SinglyLinkedList sl  =new SinglyLinkedList();
        //sl.createLoopedList();
        //sl.detectCycle();
        sl.add(67); sl.add(21); sl.add(56); sl.add(90);
        // sl.detectCycle();
        //System.out.println(sl.search(sl.head, 98));
        // sl.addSorted(43); sl.addSorted(33); 
        // sl.addSorted(45); sl.addSorted(10);
        sl.disp();
        sl.head  = sl.mergeSort(sl.head);
        //sl.reverse();
        sl.disp();
        // sl.addFirst(10);
        //sl.addLast(99);
        //sl.addLast(102);
        //System.out.println("\n adding at last");
        //sl.disp();
    }
}

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
    }
}

