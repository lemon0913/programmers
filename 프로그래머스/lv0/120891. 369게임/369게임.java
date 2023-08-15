class Solution {
    public int solution(int order) {
        
        int answer = 0;
        String str_order = order + "";
        
        for (int i = 0; i < str_order.length(); i = i + 1) {
            if (str_order.charAt(i) == '3' || str_order.charAt(i) == '6' || str_order.charAt(i) == '9') {
                answer = answer + 1;
            }
        }
        
        return answer;
    }
}