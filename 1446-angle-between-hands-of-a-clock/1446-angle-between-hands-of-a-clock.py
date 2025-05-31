class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_diff_1_hour = 360 / 12
        angle_diff_1_minute = angle_diff_1_hour / 60
        hour_arm = (hour%12)*angle_diff_1_hour + angle_diff_1_minute * minutes
        minute_arm = (360/60) * minutes
        # print(hour_arm, minute_arm)
        gap = abs(hour_arm-minute_arm)
        return min(gap, 360-gap)
        