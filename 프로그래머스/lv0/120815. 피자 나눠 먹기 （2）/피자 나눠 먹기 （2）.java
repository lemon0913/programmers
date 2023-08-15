class Solution {
    public int solution(int n) {
        // int answer = 0;
        int cnt = 1;
        
        while(true) {
            if ((cnt*6) % n == 0) {
                return cnt;
            }
            cnt = cnt + 1;
        }
        
    }
}