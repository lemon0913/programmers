import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
        List<String> strList = new ArrayList<>(Arrays.asList(s2));
        
        for (String s : s1) {
            if (strList.contains(s)) {
                answer = answer + 1;
            }
        } 
        
        return answer;
    }
}