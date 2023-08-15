class Solution {
    public int[] solution(int[] num_list) {
        
        
        int[] answer = new int[2];
        
        int x = 0;
        int y = 0;
        
        for (int num : num_list) {
            if (num % 2 == 0) {
                x = x + 1;
            }
            else {
                y = y + 1;
            }
        }
        
        answer[0] = x;
        answer[1] = y;
        
        return answer;
    }
}