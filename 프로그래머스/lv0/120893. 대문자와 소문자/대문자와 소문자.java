class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i = i + 1) {
            if (my_string.charAt(i) >= 'a' && my_string.charAt(i) <= 'z') {
                answer = answer + (my_string.charAt(i) + "").toUpperCase();
            } else {
                answer = answer + (my_string.charAt(i) + "").toLowerCase();
            }
        }
        return answer;
    }
}