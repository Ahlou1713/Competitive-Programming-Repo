class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        skills = []
        left = 0
        right = n-1
        s = 0
        while left<right:
            curr_sum = skill[left]+skill[right]
            if(s==0):
                s = curr_sum
                skills.append([skill[left], skill[right]])
            elif(s == curr_sum):
                skills.append([skill[left], skill[right]])
            left+=1
            right-=1

        if(len(skills) != n/2):
            return -1
        else:
            output = 0
            for sk in skills:
                output+= sk[0]*sk[1] 
            return output
