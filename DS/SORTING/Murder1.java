class Murder1{

    public static void main(String... args){
        int[] stairs = {1,5,3,6,4};
        int total = 0;
        for(int i = 1;i<stairs.length;i++){
            int j = i-1;
            int sum = 0;
            while(j>=0){
                if(stairs[j]<stairs[i]){
                    sum+=stairs[j];
                }
                j--;
            }
            total+=sum;
            System.out.println("sum at stair: "+i+" is "+sum);
        }
        System.out.println("Final result: "+total);
    }

}