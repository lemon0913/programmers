class Solution {
    public int solution(int[][] sizes) {
        int answer = 1;
        int l = sizes.length;
        
        int big = 1;
        int small = 1;
        
        for (int i = 0; i < l; i++) {
            if (sizes[i][0] > sizes[i][1]) {
                big = Math.max(big,sizes[i][0]);
                small = Math.max(small,sizes[i][1]);
            } else {
                big = Math.max(big,sizes[i][1]);
                small = Math.max(small,sizes[i][0]);
            }
        }
        
        return big*small;
    }
}