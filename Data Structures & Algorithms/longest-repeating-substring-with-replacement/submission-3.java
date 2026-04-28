class Solution {
    public int characterReplacement(String s, int k) {
        int maxLen = 0;
        int maxFreq = 0;
        int start = 0;
        Map<Character, Integer> freq = new HashMap<>();

        for(int end = 0; end < s.length(); end++) {
            char endChar = s.charAt(end);
            freq.put(endChar, freq.getOrDefault(endChar, 0) + 1);
            maxFreq = Math.max(maxFreq, freq.get(endChar));

            int totalConversions = (end - start + 1) - maxFreq;
            if(totalConversions > k) {
                char startChar = s.charAt(start);
                freq.put(startChar, freq.get(startChar)-1);
                start++;
            }

            maxLen = Math.max(maxLen, (end - start + 1));
        }
        return maxLen;
    }
}
