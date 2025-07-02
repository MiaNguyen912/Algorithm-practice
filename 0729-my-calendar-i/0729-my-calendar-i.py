class MyCalendar:
    # can add new event if doesn't cause a double booking
    # double booking: 2 events have some non-empty intersection
    # event: [startTime, endTime)

    # plan: queue

    def __init__(self): # Initializes the calendar object.
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool: # Returns true if event can be added and add, or false
        # check if current event overlap with any event in calendar

        # -------plan 1: O(n)
        # for s,e in self.calendar:
        #     if endTime>s and startTime<e: # |---s-----------|----e
        #         return False
        # self.calendar.add([startTime, endTime])
        # return True

        # -------plan 2: use bisect_right() to find the 2 closest events in calendar and check if they overlap
        closest_e = self.calendar.bisect_right([startTime, endTime]) # this event has start time > curr startTime
        
        # if calendar is empty, closest_e_index==0
        # check left and right of current event to see overlap
        if closest_e-1 >= 0 and startTime < self.calendar[closest_e-1][1]: # if exist the closest left and overlap
            return False
        if closest_e < len(self.calendar) and endTime > self.calendar[closest_e][0]: #if exist closest right and overlap
            return False
        self.calendar.add([startTime, endTime])
        return True


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)