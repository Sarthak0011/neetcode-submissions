class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, List<String>> mpp = new HashMap<>();
        for(String s : strs) {
            int[] hash = new int[26];
            for(int i = 0; i < s.length(); i++) {
                int hashIndex = s.charAt(i) - 'a';
                hash[hashIndex]++;
            }
            String hashKey = generateHashKey(hash);
            if(mpp.containsKey(hashKey)) {
                mpp.get(hashKey).add(s);
            }
            else {
                mpp.put(hashKey, new ArrayList<>(List.of(s)));
            }
        }
        
        for(Map.Entry<String, List<String>> entry: mpp.entrySet()) {
            ans.add(entry.getValue());
        }
        return ans;
    }

    private String generateHashKey(int[] hash) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < hash.length; i++) {
            char ch = (char) (hash[i] + '0');
            sb.append(ch);
        }
        return sb.toString();
    }
}
