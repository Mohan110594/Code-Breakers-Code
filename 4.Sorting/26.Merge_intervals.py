#Time comp --> o(n log n)
#space comp --> o(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        out=[]
        for i in range(len(intervals)):
            if i==0:
                out.append(intervals[i])
            else:
                last=out.pop()
                interval=intervals[i]
                if last[1]>=interval[0]:
                    out.append([last[0],max(last[1],interval[1])])
                else:
                    out.append(last)
                    out.append(interval)
        return out
            