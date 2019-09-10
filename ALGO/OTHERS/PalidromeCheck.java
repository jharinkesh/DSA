import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
class PalindromeCheck{

    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        HashMap<Character,Integer> map = new HashMap<>();
        for(int i=0;i<s.length();i++){
            Character ch = s.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) + 1);
            }else{
                map.put(ch, 1);
            }
        } 

        int oddCount = 0;
        for(Character ch : map.keySet()){
            if(map.get(ch)%2!=0)
                oddCount++;
        }

        // System.out.println(oddCount);
        if(oddCount >1){
            System.out.println(-1);
            return;
        }

        char[] output = new char[s.length()];

        int start = 0;
        int end = s.length()-1;
        for(Character ch : map.keySet()){
            int count = map.get(ch);
            if(count%2 == 0){
                for(int i = 0;i<count/2;i++){
                    output[start] = ch;
                    output[end] = ch;
                    start++; end--;
                }
            }else{
                int st = s.length()/2;
                int en = st + 1;
                for(int k = 0;k<count;k++){
                    if(k%2 == 0){
                        output[st] = ch;
                        st--;
                    }else{
                        output[en] = ch;
                        en++;
                    }
                }
            }
        }

        System.out.println(output);
            
    }

}