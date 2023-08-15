class Solution {
    public int solution(int n) {
        
        double x = Math.sqrt(n);
        
        if (x == (int)x) {
            return 1;
        } else {
            return 2;
        }
        
    }
}