import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] numbers) {
        
        int l = numbers.length;
        Arrays.sort(numbers);
        // Arrays.sort(numbers, Collections.reverseOrder());
        
        
        return numbers[l-1] * numbers[l-2];
    }
}