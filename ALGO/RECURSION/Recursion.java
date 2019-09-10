class Recursion {

    public static void main(String[] args){
        Recursion r = new Recursion();
        // System.out.println(r.fact(4));
        System.out.println(r.power(4,3));
    }

    int power(int x,int y){
        if(y == 0){
            return 1;
        }
        return x * power(x, y-1);
    }

    int fact(int n){
        if(n == 0){
            return 1;
        }
        int result1 = fact(n-1);
        return n * result1;
    }
}