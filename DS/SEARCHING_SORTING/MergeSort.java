 import java.util.List;
 import java.util.ArrayList;
 class MergeSort{

     static void sort(int[]a, int start, int end){
         if(start<end){
             int mid = (start+ end)/2;
             sort(a,start,mid);
             sort(a,mid+1,end);
             merge(a,start,mid,end);
         }
     }

    static void merge(int[] a, int start, int mid, int end){
        int i = start, j = mid+1;
        List<Integer> ls = new ArrayList<>();
        while(i<=mid && j<=end){
            if(a[i]<=a[j]){
                ls.add(a[i]);
                i++;
            }else{
                ls.add(a[j]);
                j++;
            }
        }
        if(i<=mid){
            while(i<=mid){
                ls.add(a[i]);
                i++;
            }
        }
       if(j<=end){
            while(j<=mid){
                ls.add(a[j]);
                j++;
            }
        }
        for(Integer e:ls){
            a[start] = e;
            start++;
        }
    }

     public static void main(String args[]){
        int a[] = {7,3,4,6,7,1,2,3};
        sort(a,0,a.length-1);
        System.out.println(java.util.Arrays.toString(a));
     }


 }