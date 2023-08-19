import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        // int[] answer = {};
        
        Stack<Integer> stk = new Stack<> ();
        
        stk.push(arr[0]);
        for (int i = 1; i < arr.length; i++ ) {
            if (stk.peek() != arr[i]) {
                stk.push(arr[i]);
            }
        }
        
        int[] answer = new int[stk.size()];
        for ( int i = 0; i < stk.size(); i++) {
            answer[i] = stk.elementAt(i);
        }

        return answer;
    }
}