class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish.
        # single-threaded CPU that can process at most one task at a time 
        # If the CPU is idle and there are available tasks, choose the one with the shortest processing time or smallest index. then process without stopping
        # return order processing tasks
        # time starts at 1

        # greedy
        # shorted job first
        tasks = sorted([[t,i,d] for i,(t,d) in enumerate(tasks)]) # time, index, duration
        cur = 1
        i = 0
        pq = []
        res = []
        while i < len(tasks) or pq: # while 
            if i<len(tasks) and cur < tasks[i][0] and not pq: # not pq: cpu is idle
                cur = tasks[i][0]
            while i < len(tasks) and cur >= tasks[i][0]:
                heappush(pq, [tasks[i][2], tasks[i][1]]) 
                i += 1
            d,j = heappop(pq) # duration, index
            cur += d
            res.append(j)
        return res