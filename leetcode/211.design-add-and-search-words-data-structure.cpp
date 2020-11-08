//
// Created by anhtn on 16/09/2023.
//
/*
 * @lc app=leetcode id=211 lang=cpp
 *
 * [211] Design Add and Search Words Data Structure
 */
#include <iostream>
#include <vector>
#include <stack>
#include <tuple>

using namespace std;

// @lc code=start
class TrieNode {
public:
    TrieNode(): children(vector<TrieNode*>(26, nullptr)) {
    }

    ~TrieNode() {
        while (!children.empty()) {
            delete children.back();
            children.pop_back();
        }
    }

    vector<TrieNode*> children;
    bool matched = false;
};

class WordDictionary {
public:
    WordDictionary() = default;

    void addWord(const string& word) {
        TrieNode* node = &this->root;
        for (auto &ch : word) {
            int idx = ch - 'a';
            if (node->children[idx] == nullptr) {
                auto child = new TrieNode();
                node->children[idx] = child;
                node = child;
            } else {
                node = node->children[idx];
            }
        }
        node->matched = true;
    }

    bool search(const string& word) {
        return searchRecursive(&this->root, word, 0);
    }

    bool searchRecursive(TrieNode* node, const string& word, int idx) {
        if (idx == word.length()) return false;
        if (word[idx] == '.') {
           for (auto c : node->children) {
                if (c == nullptr) continue;
                if (c->matched && idx == word.length() - 1) return true;
                else if (searchRecursive(c, word, idx+1)) return true;
            } 
        } else {
            auto c = node->children[word[idx] - 'a'];
            if (c != nullptr) {
                if (c->matched && idx == word.length()-1) return true;
                else return searchRecursive(c, word, idx+1);
            }
        }
        return false;
    }
    
    bool searchIterative(const string& word) {
        stack<tuple<TrieNode*, int>> st;
        st.push(make_tuple(&this->root, 0));

        TrieNode* node;
        int idx;
        bool ok = false;
        while (!st.empty() && !ok) {
            tie(node, idx) = st.top();
            st.pop();
            if (idx == word.length()) continue;
            if (word[idx] == '.') {
                for (auto c : node->children) {
                    if (c == nullptr) continue;
                    if (c->matched && idx == word.length() - 1) {
                        ok = true;
                        break;
                    } else {
                        st.push(make_tuple(c, idx + 1));
                    }
                }
            } else {
                auto c = node->children[word[idx] - 'a'];
                if (c != nullptr) {
                    if (c->matched && idx == word.length()-1) {
                        ok = true;
                    } else {
                        st.push(make_tuple(c, idx+1));
                    }
                }
            }
        }
        return ok;
    }

    TrieNode root;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end
int main() {
    WordDictionary wordDictionary;
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.addWord("ba");

    cout << wordDictionary.search("pad") << endl; // return False
    cout << wordDictionary.search("bad") << endl; // return True
    cout << wordDictionary.search(".ad") << endl; // return True
    cout << wordDictionary.search("b..") << endl; // return True
    cout << wordDictionary.search("ba") << endl; // return False
}

