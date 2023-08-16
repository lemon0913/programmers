class Solution {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length / n][n];
        
        for(int i = 0; i < (num_list.length / n); i = i + 1) {
            for(int j = 0; j < n; j = j + 1) {
                answer[i][j] = num_list[i*n+j];
            }
        }
        return answer;
    }
}