class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_dic = Counter()
        i = 0

        for x in fruits:
            fruits_dic[x] += 1
            if len(fruits_dic) > 2:
                y = fruits[i]
                fruits_dic[y] -= 1
                if fruits_dic[y] == 0:
                    fruits_dic.pop(y)
                i+=1
        
        return len(fruits) - i