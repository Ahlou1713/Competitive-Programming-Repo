class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        output = 0
        window = []

        for e in word:
            if not window:
                window.append(e)
            elif e >= window[-1]:
                window.append(e)
            else:
                if set(window) == vowel_set:
                    output = max(output, len(window))
                window = [e]

        if set(window) == vowel_set:
            output = max(output, len(window))
            
        return output

