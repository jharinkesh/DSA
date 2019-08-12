import java.util.*;

class Problems {

    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        //1<=n<=10^5
        if(n>=1 && n<=100000){

            int a[] = new int[n];
            for(int i=0;i<n;i++){
                a[i] = sc.nextInt();
                if(!(a[i]>=1 && a[i]<=1000000))
                    return;
            }

            int sumE= 0, sumO= 0;
            for(int i =0;i<n;i++){
                if(a[i]%2 == 0 && i%2 ==0){
                    sumE+= a[i];
                }else if(a[i]%2 != 0 && i%2 !=0){
                    sumO+= a[i];
                }
            }

            System.out.println(sumE+" "+sumO);
        }

    }

}