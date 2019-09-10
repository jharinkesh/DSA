class SumArray {
    public static void main(String[] args){
        int[] a = {3,5,2,7,8};
        System.out.println(sum(0, 0, a));
    }
    static int sum(int start, int sum, int[] a){
        if(start == a.length)
            return 0;
        return a[start] + sum(start+1,sum, a);
    }
}