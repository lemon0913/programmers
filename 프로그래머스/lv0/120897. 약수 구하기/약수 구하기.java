class Solution {
    public int[] solution(int n) {
        
        int cnt = 0;
        for (int i = 1; i <= n; i = i + 1) {
            if (n%i == 0) {
                cnt = cnt + 1;
            }
        }
        
        int[] answer = new int[cnt];
        int c = 0;
        for (int i = 1; i <= n; i = i + 1) {
            if (n%i == 0) {
                answer[c] = i;
                c = c + 1;
            }
        }
        
        return answer;
    }
}