import java.util.*;

class HeapSort {

    static int a[] = {0, 9, 4, 5, 8, 6, 3 };

    public static void main(String[] args) {
        System.out.println(Arrays.toString(a));
        insert(2);
        insert(3);
        insert(4);
        System.out.println(Arrays.toString(a));
        //delete(6);
        //System.out.println(Arrays.toString(a));
        for(int i = 6;i>1;i--)
            delete(i);
        System.out.println(Arrays.toString(a));
    }

    static void insert(int i){
        int temp = a[i];
        while(i>1 && a[i/2] < temp){
          a[i] = a[i/2];
          i = i/2;
        }
        a[i] = temp;
      }

    static void delete(int n){
        int val = a[1];
        a[1] = a[n];
        a[n] = val;
        int i = 1, j = i*2;
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
    }

    static void swap(int i, int j){
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
    }

}