class Solution {
    public int[] solution(int n) {
        
        int tmp = 0;
        if (n % 2 == 0) {
            tmp = n / 2;
        } else {
            tmp = n / 2 + 1;
        }
        
        int[] answer = new int[tmp];
        
        for (int i = 1; i <= n; i = i + 1) {
            if (i % 2 == 1) {
                answer[i/2] = i;
            }
        }
        
        return answer;
    }
}