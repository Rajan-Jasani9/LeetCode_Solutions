class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') %2 != 0 or corridor.count('S') == 0:
            return 0
        j = 0
        while corridor[j] == 'P':
            j+=1 
        corridor = corridor[j:]
        p_array = []
        second = 0
        count = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S' and second == 0:
                second = 1
                if count!= 0:
                    p_array.append(count+1)
                    count = 0     
            elif corridor[i] == 'P' and second == 0:
                count += 1
            elif corridor[i] == 'S' and second == 1:
                second = 0
            elif corridor[i] == 'P' and second == 1:
                print('eh')
                continue
        count = 1
        for i in range(len(p_array)):
            count *= p_array[i]

        return count % (10**9 + 7)