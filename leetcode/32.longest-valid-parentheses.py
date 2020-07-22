#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                # Không cần phải check st[-1] (top-most of stack) ở đây có phải là 
                # ký tự '(' hay không vì sau khi pop stack, nếu stack không empty 
                # thì gía trị top-most chắc chắn phải là '('
                #
                # GIẢI THÍCH
                # Lý do là vì không bao giờ xảy ra trường hợp 2 ký tự ')' tồn tại liên tiếp 
                # trong stack do khi gặp ký tự ')' ta luôn pop top-most và thêm lại giá trị 
                # cuối cùng nếu stack empty, nên stack chỉ tồn tại tối đa một giá trị ')'
                st.pop()
                if st:
                    ans = max(ans, i - st[-1])
                else:
                    st.append(i)
        return ans
        
# @lc code=end

