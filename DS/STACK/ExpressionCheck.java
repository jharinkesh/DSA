import java.util.Scanner;
import java.util.Stack;
class ExpressionCheck {

    public static void main(String[] arf){
        Scanner s = new Scanner(System.in);
        String s1 = s.nextLine();
        System.out.println(isValid(s1));
    }

    static boolean isValid(String s){
       Stack<Character> st = new Stack<>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c == '(' || c == '{' || c == '[')
                st.push(c);
            else if( c==')' || c == ']' || c == '}'){
                if(st.size() == 0)
                    return false;
                else{
                   char ch =(char) st.pop();
                   if(!(ch == '(' || ch == '{' || ch == '['))
                    return  false;
                }
            }
        }

        return true;
    }

}