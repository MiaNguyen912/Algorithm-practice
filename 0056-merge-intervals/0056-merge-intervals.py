class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by increasing start_i
        """
            ---------------
            ------------
                ----
                       ---------   
                            ---------------------- 

        """
        intervals.sort(key=lambda pair:pair[0])
        start_interval, last_ending = intervals[0][0], intervals[0][1]
        output = []
        for i in range(len(intervals)):

            if intervals[i][0] <= last_ending: # overlap
                last_ending = max(last_ending, intervals[i][1])
            else: # no overlap -> append the old interval to list, start new interval
                output.append([start_interval,last_ending])
                # print(output)
                start_interval, last_ending = intervals[i][0], intervals[i][1]
        # append the last interval
        output.append([start_interval,last_ending])
        return output
        