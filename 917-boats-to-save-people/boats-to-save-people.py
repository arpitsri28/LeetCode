class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        r = len(people) - 1
        l = 0
        boats = 0
        people.sort()
        while l <= r:
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            boats += 1
        return boats

        