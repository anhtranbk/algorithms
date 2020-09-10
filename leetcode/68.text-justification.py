#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
from common import BaseTestCase, unittest
# @lc code=start
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, t = 0, 0
        ans = []
        for j, word in enumerate(words):
            n = j - i - 1 #  minimum number of spaces needed
            if len(word) + t + n < maxWidth:
                t += len(word)
                continue

            if n > 0:
                avg = (maxWidth - t) // n # average number of spaces for each slot
                remain = (maxWidth - t) % n
            else:
                avg, remain = 0, 0

            # fill line with words
            buf = words[i:j]
            spaces = [avg+1 if k < remain else avg for k in range(n)]
            line = buf[0]
            for k in range(1, len(buf)):
                line += ' '*spaces[k-1]
                line += buf[k]

            # line contains one word then fill right slot with spaces
            if len(line) < maxWidth:
                line += ' '*(maxWidth-len(line))

            ans.append(line)
            t = len(word)
            i = j

        # process all the rest of words
        if i < len(words):
            line = ' '.join(words[i:])
            if len(line) < maxWidth:
                line += ' '*(maxWidth-len(line))
            ans.append(line)

        return ans
        
        
# @lc code=end
class P68TestCase(BaseTestCase):
    def test_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        actual = Solution().fullJustify(words, maxWidth)
        self.assertArrayEquals(expected, actual)

    def test_2(self):
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        actual = Solution().fullJustify(words, maxWidth)
        self.assertArrayEquals(actual, expected)

    def test_3(self):
        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        actual = Solution().fullJustify(words, maxWidth)
        self.assertArrayEquals(actual, expected)


if __name__ == "__main__":
    unittest.main()