import java.util.Scanner;
import java.util.ArrayList;
class RemoveDuplicateChars {
    public static void main(String... srgs){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String output = "";
        ArrayList<Character> ls = new ArrayList<>();
        for(int i = 0; i<s.length(); i++){
            Character ch = s.charAt(i);
            if(!ls.contains(ch)){
                ls.add(ch);
                output = output + ch;
            }
        }
        System.out.println(output);
    }
}