class QuickSort {

    public static void main(String... args){
        int[] a = {8,5,8,7,2,3,9,1};
        quicksort(a,0, a.length-1);
        System.out.println(java.util.Arrays.toString(a));
    }

    static void quicksort(int[] a, int start, int end){
        if(start<end){
            int pindex = partition(a,start,end);
            quicksort(a, start, pindex-1);
            quicksort(a, pindex+1, end);
        }
    }

    static int partition(int[] a, int start, int end){
        int pivot = a[end];
        int pindex = start;
        for(int i = start; i<end; i++){
            if(a[i]<=pivot){
                int t = a[pindex];
                a[pindex] = a[i];
                a[i] = t;
                pindex++;
            }
        }
        int t = a[pindex];
        a[pindex] = a[end];
        a[end] = t;
        return pindex;
    }
}