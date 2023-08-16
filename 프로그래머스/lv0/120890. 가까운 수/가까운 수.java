import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int gap = 1000;
        Arrays.sort(array);
        
        for (int a : array) {
            if (Math.abs(a-n) < gap) {
                answer = a;
                gap = Math.abs(a-n);
            }
        }
        return answer;
    }
}