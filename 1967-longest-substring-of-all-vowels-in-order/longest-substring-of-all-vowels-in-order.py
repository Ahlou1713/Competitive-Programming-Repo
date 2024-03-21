class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        longest = 0
        window = []

        for char in word:
            if not window:
                window.append(char)
            elif char >= window[-1]:
                window.append(char)
            else:
                if set(window) == vowels:
                    longest = max(longest, len(window))
                window = [char]

        if set(window) == vowels:
            longest = max(longest, len(window))

        return longest

