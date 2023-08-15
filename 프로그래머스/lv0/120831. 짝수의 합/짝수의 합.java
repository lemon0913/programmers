class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i = i + 1) {
            if (i % 2 == 0) {
                answer += i;
            }
        }
        return answer;
    }
}