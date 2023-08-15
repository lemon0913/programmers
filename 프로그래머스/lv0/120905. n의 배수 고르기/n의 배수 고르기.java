
class Solution {
    public int[] solution(int n, int[] numlist) {
       
        int cnt = 0;
        for (int num : numlist) {
            if (num % n == 0) {
                cnt = cnt + 1;
            }
        }
        
        int[] answer = new int[cnt];
        int c = 0;
        for (int i = 0; i < numlist.length; i = i + 1) {
            if (numlist[i] % n == 0) {
                answer[c] = numlist[i];
                c = c + 1;
            }
        }
        
        return answer;
        
    }
}