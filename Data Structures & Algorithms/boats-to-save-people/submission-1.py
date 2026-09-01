class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0 
        l, r = 0, len(people) - 1

        people.sort() 

        while l <= r: 
            # heaviest and lightest person go on boat together
            if people[l] + people[r] <= limit: 
                l += 1
                r -= 1
            # heaviest person goes on boat alone 
            else:
                r -= 1
            boats += 1

        return boats