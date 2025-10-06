class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        useful_triplets = []
        for triplet in triplets:
            a = triplet[0]
            b = triplet[1]
            c = triplet[2]
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0] or b == target[1] or c == target[2]:
                    useful_triplets.append(triplet)
        
        if len(useful_triplets) == 0:
            return False
        
        a_flag, b_flag, c_flag = False, False, False

        for triplet in useful_triplets:
            if triplet[0] == target[0]:
                a_flag = True
            if triplet[1] == target[1]:
                b_flag = True
            if triplet[2] == target[2]:
                c_flag = True
        
        return a_flag and b_flag and c_flag

        
        