class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        mydict = {
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
        }
        if mydict[coordinates[0]] % 2 == 0 and int(coordinates[1]) % 2 == 0:
            return False
        elif mydict[coordinates[0]] % 2 == 1 and int(coordinates[1]) % 2 == 1:
            return False
        elif mydict[coordinates[0]] % 2 == 1 and int(coordinates[1]) % 2 == 0:
            return True
        elif mydict[coordinates[0]] % 2 == 0 and int(coordinates[1]) % 2 == 1:
            return True