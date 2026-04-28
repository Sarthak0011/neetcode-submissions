class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n != m) return false;

        Map<Character, Integer> freq = new HashMap<>();
        for(int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if(!freq.containsKey(ch)) freq.put(ch, 1);
            else freq.put(ch, freq.get(ch)+1);
        }
        
        for(int i = 0; i < n; i++) {
            char ch = t.charAt(i);
            if(!freq.containsKey(ch) || freq.get(ch) <= 0) return false;
            freq.put(ch, freq.get(ch)-1);
        }

        for(Map.Entry<Character, Integer> entry : freq.entrySet()) {
            if(entry.getValue() != 0) return false;
        }
        return true;
    }
}
