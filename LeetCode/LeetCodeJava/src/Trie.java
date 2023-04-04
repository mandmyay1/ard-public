// https://leetcode.com/problems/implement-trie-prefix-tree/description/
/*
 * A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 */
import java.util.HashMap;

class Trie {

    class Node {
        HashMap<Character, Node> childItems = new HashMap<Character, Node>();
        boolean isTerminus = false;
    }
    Node root;

    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node pointer = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!pointer.childItems.containsKey(c)) {
                pointer.childItems.put(c, new Node());
            }
            pointer = pointer.childItems.get(c);
        }
        pointer.isTerminus = true;
    }
    
    public boolean search(String word) {
        Node pointer = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!pointer.childItems.containsKey(c)) {
                return false;
            }
            pointer = pointer.childItems.get(c);
        }
        return pointer.isTerminus;
    }
    
    public boolean startsWith(String prefix) {
        Node pointer = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (!pointer.childItems.containsKey(c)) {
                return false;
            }
            pointer = pointer.childItems.get(c);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */