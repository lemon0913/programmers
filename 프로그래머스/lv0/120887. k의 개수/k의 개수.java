class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        
        String tmp = "";
        String str = k + "";
        for (int n = i; n <= j; n = n + 1) {
            tmp = n + "";
            for(int x = 0; x < tmp.length(); x = x + 1) {
                if ((tmp.charAt(x)+"").equals(str)) {
                    answer = answer + 1;
                }
            }
        }
        return answer;
    }
}