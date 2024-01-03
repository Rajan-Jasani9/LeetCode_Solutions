class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        res = []
        for i in range(len(bank)):
            res.append(bank[i].count('1'))
        i = 0
        j = 1
        if sum(res) == 0:
            return 0
        while j < len(res):
            print(j)
            if res[i] == 0:
                i+=1
                if i == j:
                    j+=1
                
            elif res[j] == 0:
                j+=1

            else:
                count += res[i] * res[j]
                i = j
                j+=1
        
        return count