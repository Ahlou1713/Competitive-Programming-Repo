class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        output = i = 0
        for pAbility in players:
            while i < len(trainers) and trainers[i] < pAbility:
                i += 1
            if i < len(trainers):
                output += 1
                i += 1
        
        return output