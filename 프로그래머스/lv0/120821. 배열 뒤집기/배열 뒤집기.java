class Solution {
    public int[] solution(int[] num_list) {
        int l = num_list.length;
        int[] answer = new int[l];
        
        for (int i = 0; i < l; i = i + 1) {
            answer[i] = num_list[l-1-i];
        }
        
        return answer;
    }
}