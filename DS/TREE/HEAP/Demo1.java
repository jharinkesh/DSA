import java.util.*;
class Demo1 {
    static int[] a = {0, 30,20,15,5,10,12,6,0,0,0};
    static int n = 7;

    public static void main(String[] args) {
        System.out.println(Arrays.toString(a));
        // insert(40);
        // insert(50);
        delete();
        System.out.println("size: "+n+"\n"+Arrays.toString(a));
    }

    static void insert(int e){
      int i = n +1;
      while(i>1 && a[i/2] < e){
        a[i] = a[i/2];
        i = i/2;
      }
      a[i] = e;
      n++;
    }

    static void delete(){
        a[1] = a[n];
        a[n] = 0;
        int i = 1, j = 2;
        while(j<n-1){
            if(a[j+1] > a[j]){
                j = j+1;
            }
            if(a[i]<a[j]){
                swap(i,j);
                i = j;
                j = i*2;
            }else{
                break;
            }
        }
        n--;
    }

    static void swap(int i, int j){
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
    }

}