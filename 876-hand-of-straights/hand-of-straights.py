class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        hashHand = {}
        for num in hand:
            if num in hashHand:
                hashHand[num] += 1
            else:
                hashHand[num] = 1
        
        itr = int(len(hand) / groupSize)
        hand.sort()
        idx = 0
        for i in range(itr):
            k = groupSize
            j = 0
            for num in hand:
                if hashHand[num] == 0:
                    continue
                curr = num
                hashHand[curr] -= 1
                break
            while j < k - 1:
                if curr+1 in hashHand and hashHand[curr+1] > 0:
                    j += 1
                    hashHand[curr+1] -= 1   
                    curr = curr + 1
                else:
                    return False
            
        return True

                
            


        