class LinkedStack {
    Node top = null;

    void push(int data){
        if(top ==null){
            top = new Node(data);
        }else{
            Node n1 = new Node(data);
            top.next = n1;
            n1.prev = top;
            top = n1;
        }
    }

    void disp(){
        Node n1 = top;
        while(n1 !=null){
            System.out.println(n1.data);
            n1 = n1.prev;
        }
    }

    int pop(){
        int element = -1;
        if(top == null){
            return -1;
        }else{
            element = top.data;
            Node n1 = top;
            if(n1.prev!=null){
                n1.prev.next = null;
            }
            top = n1.prev;
        }
        return element;
    }

    public static void main(String... args){
        LinkedStack ls = new LinkedStack();
        ls.push(45); ls.push(23); ls.push(87);
        ls.disp();
        System.out.println("pop : "+ls.pop());
        System.out.println("pop : "+ls.pop());
        System.out.println("pop : "+ls.pop());
        System.out.println("pop : "+ls.pop());
    }
}

class Node {
    int data;
    Node prev;
    Node next;
    Node(int data){
        this.data = data;
    }
}