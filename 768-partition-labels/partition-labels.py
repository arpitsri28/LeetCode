class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashStr = {}
        hashseen = {}
        for Str in s:
            if Str in hashStr:
                hashStr[Str] += 1
            else:
                hashStr[Str] = 1
        
        output = []
        count = 0
        for i in range(len(s)):
            count += 1
            
            if s[i] in hashseen:
                hashseen[s[i]] += 1
            else:
                hashseen[s[i]] = 1
            
            hashStr[s[i]] -= 1

            done = True
            for ch in hashseen:
                if hashStr[ch] > 0:
                    done = False
                    break
            
            if done:
                output.append(count)
                count = 0
                hashseen = {}
        
        return output

                
                
        