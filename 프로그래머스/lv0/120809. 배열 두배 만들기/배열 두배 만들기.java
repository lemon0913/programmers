class Solution {
    public int[] solution(int[] numbers) {
        int l = numbers.length;
        int[] answer = new int[l];
        
        for (int i = 0; i < l; i = i + 1) {
            answer[i] = numbers[i] * 2;
        }
        
        return answer;
    }
}