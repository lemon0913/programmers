import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        
        int m = nums.length / 2;
        
        HashSet<Integer> hs = new HashSet<>();
        for(int num : nums) {
            hs.add(num);
        }
        
        if (hs.size() > m) {
            return m;
        }
        
        return hs.size();
    }
}