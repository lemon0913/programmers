import java.util.HashMap;
import java.util.Map;
import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < clothes.length; i++) {
            if (map.containsKey(clothes[i][1])) {
                map.put(clothes[i][1], map.get(clothes[i][1])+1);
            } else {
                map.put(clothes[i][1], 2);
            }
        }
        
        Set<String> keyset = map.keySet();
        for (String key : keyset) {
            answer = answer * map.get(key);
            // System.out.println(key);
            // System.out.println(map.get(key));
        }
        
        return answer-1;
    }
}