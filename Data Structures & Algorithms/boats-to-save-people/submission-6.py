class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        boats = 0
        lightest, heaviest = 0, len(people) - 1

        while lightest <= heaviest:
            if people[lightest] + people[heaviest] <= limit:
                lightest += 1
                heaviest -= 1
            else:
                heaviest -= 1
            boats += 1

        return boats

