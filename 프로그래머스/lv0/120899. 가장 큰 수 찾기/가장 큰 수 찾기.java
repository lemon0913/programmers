class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        
        int num = 0;
        int idx = 0;
        for (int i = 0; i < array.length; i = i + 1) {
            if (array[i] > num) {
                num = array[i];
                idx = i;
            }
        }
        
        answer[0] = num;
        answer[1] = idx;
        
        return answer;
    }
}