class SortedArrayCheck{
    public static void main(String[] r){
        int a[] = {3,5,6,9,11};
        int b[] = {7,11,3,4,2};
        System.out.println(isSorted(0, b));

    }

    static boolean isSorted(int start, int[] a){
        if(a.length == 0 || a.length == 1)
            return true;
        if(start == (a.length -1))
            return true;
        if(a[start]>a[start+1])
            return false;
        return isSorted(start+1,a);
    }


}