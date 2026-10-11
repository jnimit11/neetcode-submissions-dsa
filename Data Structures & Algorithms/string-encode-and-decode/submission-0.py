class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter
            j = s.find("#", i)

            # Extract the length
            length = int(s[i:j])

            # Move past the delimiter
            i = j + 1

            # Extract the original word
            word = s[i:i + length]
            result.append(word)

            # Move past the extracted word
            i += length

        return result
