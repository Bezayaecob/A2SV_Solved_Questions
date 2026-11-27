class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res= title.split()
        for i in range(len(res)):
            if len(res[i])>2:
                res[i]= res[i][0].upper() + res[i][1:].lower()
            else:
                res[i]=res[i].lower()
        return " ".join(res)

        