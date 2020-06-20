#Time comp -> o(nk) n-> number of difficulty levels and k--> number of workers.
#space comp --> o(1)

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        # print(jobs)
        ans = i = best = 0
        for skill in sorted(worker):
            
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            # print(i,best)
            ans += best
        return ans
        