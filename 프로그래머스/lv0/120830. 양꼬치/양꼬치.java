// 1분에 12000원, 음료수는 2000원
// 양꼬치를 10인분 먹었다면 음료수를 1개 서비스로
class Solution {
    public int solution(int n, int k) {
            
        return 12000*n + (k - n/10)*2000;
    }
}