#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:
    def __init__(self) -> None:
        self.cnt = 0
        self.d = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.d[self.cnt] = longUrl
        self.cnt += 1
        return str(self.cnt - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.d.get(int(shortUrl))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
