class Solution:
    def largestGoodInteger(self, num: str) -> str:
        uniq=set(list(num))
        res=[]
        print("uniq ",uniq)
        for n in uniq:
            if n*3 in num:
                res.append(int(n))
        print(res)
        if res: return str(max(res))*3
        else: return ""

