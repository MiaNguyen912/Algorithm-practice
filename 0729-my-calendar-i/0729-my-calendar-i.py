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
        closest_e_index = self.calendar.bisect_right([startTime, endTime]) # this event has start time > curr startTime
        # |--------|    curr_event    |-------|
        print(closest_e_index, [startTime, endTime])
        if not self.calendar:
            self.calendar.add([startTime, endTime])
            return True
        if closest_e_index == 0:  # if the closest is the earliest event
            if endTime > self.calendar[closest_e_index][0]:
                return False
        elif closest_e_index == len(self.calendar):  # if the closest is the last event
            if startTime < self.calendar[closest_e_index-1][1]:
                return False
        elif endTime > self.calendar[closest_e_index][0] or startTime < self.calendar[closest_e_index-1][1]:
            return False
        self.calendar.add([startTime, endTime])
        return True




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)