class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();
        if(n > m) return false;
        int[] freq = new int[26];
        int[] temp = new int[26];
        for(int i = 0; i < n; i++) {
            freq[s1.charAt(i) - 'a']++;
            temp[s2.charAt(i) - 'a']++;
        }

        int start = 0;
        int end = n-1;

        while(end < m) {
            boolean flag = true;
            for(int i = 0; i < 26; i++) {
                if(freq[i] != temp[i]) {
                    flag = false;
                    break;
                }
            }
            if(flag) return true;

            temp[s2.charAt(start) - 'a']--;
            start++;
            end++;
            if(end < m) {
                temp[s2.charAt(end) - 'a']++;
            }
        }
        return false;
    }
}
