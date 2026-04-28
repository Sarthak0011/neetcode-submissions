class Solution {

    

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs) {
            sb.append(str.length()).append('#').append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();

        int index = 0;
        int n = str.length();

        while(index < n) {
            int j = index;
            while(j < n && str.charAt(j) != '#') j++;
            int length = Integer.parseInt(str.substring(index, j));
            int startIndex = j+1;
            int endIndex = startIndex + length;
            String s = str.substring(startIndex, endIndex);
            list.add(s);
            index = endIndex;

        }
        return list;
    }
}
