class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # U
        # - When Teemo attacks Ashe, Ashe gets poisoned for a duration seconds (interval: [t, t + duration - 1])
        # - If Teemo attacks again before the poison effect ends, the timer is reset
        # - timeSeries: a non-decreasing integer array, timeSeries[i]: Teemo attacks Ashe at second timeSeries[i]
        # - Return: total number of seconds Ashe is poisoned
        # 1 <= len(timeSeries) <= 104, 0 <= timeSeries[i], duration <= 107
        # ex: timeSeries = [1,4], duration = 2 -> Output: 4 (Ashe is poisoned for seconds 1 and 2, then 4 and 5)    
        # ex: timeSeries = [1,2], duration = 2 -> Output: 3 (1 and 2, 2 and 3)

        # M: 2 pointers
        # - init l,f = 0,1
        #   output = 0
        # - while l<len(timeSeries): 
        #       endPoisontime = timeSeries[l]+duration-1
        #       while timeSeries[f] <= endPoisonTime: 
        #           endPoisonTime = timeSeries[f]+duration-1
        #           f += 1
        #       output += endPoisonTime-timeSeries[l]+1
        #       update l,f to f,f++

        # output = 0
        # fast = 1
        # low = 0
        # while low < len(timeSeries):
        #     time_end_poison = timeSeries[low] + duration-1
        #     while fast < len(timeSeries) and timeSeries[fast] <= time_end_poison:
        #         time_end_poison = timeSeries[fast] + duration-1
        #         fast += 1
        #     output += (time_end_poison - timeSeries[low]) + 1
        #     low = fast
        #     fast += 1
        # return output

        # M2: 
        #return duration+sum(min(timeSeries[i+1]-timeSeries[i], duration) for i in range(len(timeSeries)-1))

        # M3:
        # ttl = 0 # total poison damage seconds
        # for i in range(len(timeSeries)-1): #Not iterating through the last one because it will have no conflictions
        #     if timeSeries[i] + duration - 1 < timeSeries[i+1]: # If no confliction, just add the duration
        #         ttl += duration
        #     else: # If confliction, only add the poison damage seconds that happened before timeSeries[i+1]
        #         ttl += timeSeries[i+1] - timeSeries[i]
        # return ttl + duration  # Return the total + the damage duration from the last time interval
        
        # M4:
        poison = 0
        start = None
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                prev_span = timeSeries[i]-timeSeries[start] if start is not None else 0
                poison += prev_span + duration 
                start = None #reset 
            else: #overlap
                if start is None:
                    start = i
                    # print("---",start)
        prev_span = timeSeries[-1] - timeSeries[start] if start is not None else 0
        poison += prev_span + duration 
        return poison