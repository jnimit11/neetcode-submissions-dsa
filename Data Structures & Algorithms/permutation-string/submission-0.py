class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = {}
        window_freq = {}

        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        window_size = len(s1)

        for i in range(len(s1)):
            ch = s2[i]
            window_freq[ch] = window_freq.get(ch, 0) + 1

        if freq == window_freq:
            return True
        
        left = 0

        for right in range(window_size, len(s2)):
            outgoing = s2[left]
            window_freq[outgoing] -= 1 

            if window_freq[outgoing] == 0:
                del window_freq[outgoing]

            incoming = s2[right]
            window_freq[incoming] = window_freq.get(incoming, 0) + 1

            left += 1

            if freq == window_freq:
                return True

        return False