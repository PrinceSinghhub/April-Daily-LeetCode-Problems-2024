class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        n = len(tickets)
        time = 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if i == k and tickets[k] == 0:
                        return time
        return time