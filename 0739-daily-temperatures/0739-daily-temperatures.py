class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return an array answer such that answer[i]is the number of days to wait after the ith day to get a warmer temperature or 0
        # plan: use decreasing monostack to find range of subarr for each item s.t the item is max
        
        """
        We use a monotonic decreasing stack to keep track of days that haven't yet found a warmer day.

        Here's the reasoning:
        We scan from left to right (i.e., from day 0 to day N-1).
        At any index i, compare the current temp with the temperature at the top of the stack:  
            If temperatures[i] > temperatures[stack[-1]], it means we found a warmer day for stack[-1].
            So we pop from the stack, and calculate i - popped_index as the number of days waited.
        We only store indices of temps that haven’t yet found a warmer future day, which are candidates for comparison.

        By keeping the stack monotonically decreasing, we ensure:
        The first time we find a warmer day, it’s the closest warmer day 
        Every item in stack is colder than the one above, so once we find a warmer temperature, all colder days above it can be resolved.

        \U0001f525 Why not an increasing stack?
        An increasing stack would store temps that get warmer as you go down the stack. That wouldn’t help because:
        We’re not interested in how temperatures increase, we want to know when the next higher one comes.
        With an increasing stack, we'd not find the next warmer day efficiently because you’d have to scan back or search
        """


        ans = [0] * len(temperatures)
        monostack = []   # Monotonic decreasing stack to store indices

        for i, temp in enumerate(temperatures):
            # While curr temp > the temp at the top index of stack
            while monostack and temperatures[i] > temperatures[monostack[-1]]:
                prev_index = monostack.pop()  # Index of the previous colder day
                ans[prev_index] = i - prev_index  # Days to wait for warmer temperature
            monostack.append(i) # Add current day's index to stack
        return ans

