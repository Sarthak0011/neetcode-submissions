class Solution {
    private boolean isAlphaNumeric(char ch) {
        return (ch >= '0' && ch <= '9') || (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
    }
    private boolean isCompatible(char ch1, char ch2) {
        return Character.toLowerCase(ch1) == Character.toLowerCase(ch2);
    }
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length()-1;

        while(start < end) {
            char ch1 = s.charAt(start);
            char ch2 = s.charAt(end);
            if(!isAlphaNumeric(ch1)) {
                start++;
                continue;
            }
            if(!isAlphaNumeric(ch2)) {
                end--;
                continue;
            }

            if(ch1 != ch2 && !isCompatible(ch1, ch2)) return false;
            start++;
            end--;
        }
        return true;
    }
}
