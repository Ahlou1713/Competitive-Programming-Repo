class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        chemistry, s = 0, skill[0] + skill[-1]
        left = 0
        right = n-1
        while left<right:
            if(skill[left]+skill[right] == s):
                chemistry += skill[left] * skill[right]
            else:
                return -1
            left+=1
            right-=1
        return chemistry