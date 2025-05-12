class RecentCounter:
    def __init__(self):
        # use either minheap (O(logn)), or stack (O(n)), or deque(O(1)) to keep track of the current requests within 3000ms
        self.requests = deque([])
        

    def ping(self, t: int) -> int:
        # Adds new request at time t (milliseconds,) returns the number of requests happened in the past 3000ms 
        # (including the new request) (inclusive range [t - 3000, t])
        self.requests.append(t)
        earliest_request = self.requests[0] # front element, added firstly
        while t - 3000 > earliest_request and self.requests:
            self.requests.popleft() # remove from queue
            earliest_request = self.requests[0] 
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)