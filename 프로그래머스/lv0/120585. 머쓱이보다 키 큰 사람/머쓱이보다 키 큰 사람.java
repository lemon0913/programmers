import java.util.Arrays;

class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        
        Arrays.sort(array);
        for (int arr : array) {
            if (arr > height) {
                break;
            } else {
                answer = answer + 1;
            }
        }
        
        return array.length - answer;
    }
}