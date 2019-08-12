public class StackDemo{

    public static void main(String[] x){
        
        Stack s = new Stack();
        //s.disp();
        s.push(4);
        s.push(3);
        s.push(2);
        s.push(1);
        // s.push(5);
        // s.push(224);
        // s.disp();
        
        // s.pop();
        // s.pop();
        // s.pop();
        // s.pop();
        // s.pop();
        // s.pop();
        s.disp();
        s.reverse();
        System.out.println("\nafter reverse");
        s.disp();
        
    }

}

class Stack{
    int top = -1;
    final int CAPACITY = 5;
    int A[] = new int[CAPACITY];
    
    
    void push(int item){
        if(top == CAPACITY-1){
            System.out.println("Stack is Full");
        }else{
            top++;
            A[top] = item;
        }
    }
    
    int pop(){
       int el = 0;
      if(top == -1){
            System.out.println("Stack is Empty");
            return -1;
        }else{
            el = A[top];
            A[top] = 0;
            top--;
        }
        return el;
    }
    
    void disp(){
    System.out.println("Stack elements");
     for(int i=top;i>-1;i--){
         System.out.println(A[i]);
     }
    }
    
    void reverse(){
        if(top == -1)
            return;
        int temp = pop();
        reverse();
        insertAtBottom(temp);
    }

    void insertAtBottom(int data){
        if(top == -1){
            push(data);
            return;
        }
        int temp = pop();
        insertAtBottom(data);
        push(temp);
    }

}