import java.util.*;

public class AdjacencyList {

    List<GNode> list[]; 
    int size;

    AdjacencyList(int size){
        list = new List[this.size = size];
        for(int i = 0;i<size;i++){
            list[i] = new LinkedList<GNode>();
        }
    }

    void insert(int a, int b) {
        list[a].add(new GNode(b));
    }

    void disp(){
     for(int i=0;i<size;i++){
         List<GNode> list1 = list[i];
         System.out.print("\n"+i+" : ");
        for(int j = 0;j<list1.size();j++){
            System.out.print(" -> "+list1.get(j).key);
        }
     }
    }

    public static void main(String[] args) {
        AdjacencyList al = new AdjacencyList(5);
        al.insert(0,1);
        al.insert(1, 2);
        al.insert(3, 5);
        al.insert(3, 4);

        al.disp();
    }




}

class GNode  {
    int key;
    int weight;
    GNode(int key){
        this.key = key;
    }
}