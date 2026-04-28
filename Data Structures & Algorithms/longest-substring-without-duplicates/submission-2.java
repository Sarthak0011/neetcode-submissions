class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;

        Map<Character, Integer> map = new HashMap<>();
        int maxLen = 1;
        int currStart = 0;

        map.put(s.charAt(0), 0);
        for(int i = 1; i < s.length(); i++) {
            char ch = s.charAt(i);
            if(map.containsKey(ch)) {
                if(map.get(ch)+1 > currStart) currStart = map.get(ch)+1;
                map.put(ch, i);
            }
            else {
                map.put(ch, i);
            }
            maxLen = Math.max(maxLen, i - currStart + 1);
        }
        return maxLen;
    }
}
