
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        have = 0
        required = len(need)

        left = 0
        res = [-1, -1]
        res_len = float("inf") 

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1

                if (left_ch in need and
                    window[left_ch] < need[left_ch]):
                    have -= 1

                left += 1

        if res_len == float("inf"):
            return ""

        return s[res[0]:res[1] + 1]
