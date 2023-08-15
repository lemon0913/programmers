class Solution {
    public int solution(int n) {
        int answer = 0;
        char tmp = '1';
        
        String str = Integer.toString(n);
        
        for (int i = 0; i < str.length(); i = i + 1) {
            
            tmp = str.charAt(i);
            answer = answer + tmp - '0';
        }
        
        return answer;
    }
}