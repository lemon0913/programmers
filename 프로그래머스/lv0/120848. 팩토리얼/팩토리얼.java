class Solution {
    public int solution(int n) {
        // int answer = 0;
        
        int num = 1;
        int fac = 1;
        while (true) {
            if (fac > n) {
                return num - 1;
            } else {
                num = num + 1;
                fac = fac * num;
            }
            
        }

    }
}