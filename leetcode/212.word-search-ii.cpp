/*
 * @lc app=leetcode id=212 lang=cpp
 *
 * [212] Word Search II
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// @lc code=start
class TrieNode {
   public:
    string word;
    vector<TrieNode*> children;

    ~TrieNode() {
        for (auto child : children) {
            if (child != nullptr) {
                delete child;
            }
        }
    }

    TrieNode* addChild(const char& val) {
        int i = val - 'a';
        if (children[i] == nullptr) {
            children[i] = new TrieNode();
        }
        return children[i];
    }

    TrieNode* findChild(const char& val) {
        int i = val - 'a';
        return children[i];
    }
};

class Solution {
   public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = buildTrie(words);
        vector<string> ans;
        int m = board.size(), n = board[0].size();

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                dfs(board, i, j, root, ans);
            }
        }

        delete root;
        return ans;
    }

    TrieNode* buildTrie(const vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (auto& word : words) {
            TrieNode* node = root;
            for (const char& c : word) {
                node = node->addChild(c);
            }
            node->word = word;
        }
        return root;
    }

    void dfs(
        vector<vector<char>>& board,
        int i,
        int j,
        TrieNode* node,
        vector<string>& ans) {
        if (i < 0 || i == board.size()) return;
        if (j < 0 || j == board[0].size()) return;
        if (board[i][j] == '#') return;

        char c = board[i][j];
        node = node->findChild(c);
        if (node == nullptr) return;

        if (!node->word.empty()) {
            ans.push_back(node->word);
            node->word = "";
        }

        board[i][j] = '#';

        dfs(board, i - 1, j, node, ans);
        dfs(board, i + 1, j, node, ans);
        dfs(board, i, j - 1, node, ans);
        dfs(board, i, j + 1, node, ans);

        board[i][j] = c;
    }
};
// @lc code=end
