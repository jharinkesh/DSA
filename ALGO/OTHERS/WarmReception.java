class WarmReception {

    public static void main(String... args){
        int[] arrival = {900, 1000, 1100, 1030, 1600};
        int[] departure = {1900, 1300, 1130, 1130, 1800};
        int flag = 0;
        for(int i=0;i<5;i++){
            int atime = arrival[i];
            int dtime = departure[i];
            int c = 0;
            for(int j=0;j<5;j++){
                int at = arrival[j];
                int dt = departure[j];
                if( (at >=atime && at<dtime) || (dt>atime && dt <=dtime)  )
                    c++ ;
            }
            if(flag<c)
                flag = c;
         }
         System.out.println(flag);
    }
}