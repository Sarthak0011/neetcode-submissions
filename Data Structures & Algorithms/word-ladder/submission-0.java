class Node {
    String word;
    int level;
    Node(String word, int level) {
        this.word = word;
        this.level = level;
    }
}
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> set = new HashSet<>();
        for(String word: wordList) set.add(word);
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(beginWord, 1));
        if(set.contains(beginWord)) set.remove(beginWord);

        while(!q.isEmpty()) {
            Node node = q.poll();
            if(node.word.equals(endWord)) return node.level;

            for(int i = 0; i < node.word.length(); i++) {
                StringBuilder sb = new StringBuilder(node.word);
                for(char ch = 'a'; ch <= 'z'; ch++) {
                    sb.setCharAt(i, ch);
                    if(set.contains(sb.toString())) {
                        q.offer(new Node(sb.toString(), node.level+1));
                        set.remove(sb.toString());
                    }
                }
            }
        }
        return 0;
    }
}
