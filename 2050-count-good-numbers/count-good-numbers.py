class Solution:
    def countGoodNumbers(self, n: int) -> int:
        nb_y = n // 2
        nb_x = n - nb_y

        count_x = pow(5, nb_x, 10 ** 9 + 7)  
        count_y = pow(4, nb_y, 10 ** 9 + 7)  

        return (count_x * count_y) % (10 ** 9 + 7)
