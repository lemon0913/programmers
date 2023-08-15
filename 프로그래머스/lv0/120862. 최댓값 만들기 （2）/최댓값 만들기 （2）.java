import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        
        int answer = 0;
        int l = numbers.length;
        
        Arrays.sort(numbers);
        answer = Math.max(numbers[0]*numbers[1], numbers[l-1]*numbers[l-2]);
        
        return answer;
    }
}