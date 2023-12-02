class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_map = Counter(chars)
        count = 0
        for word in words:
            flag = 0
            temp = Counter(word)
            for key in temp.keys():
                if temp[key] > chars_map[key]:
                    flag = 1
                    break
                
            if flag != 1:
                count += len(word)
        return count