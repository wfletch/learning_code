class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Let's get hour angle and minute angle
        minute_angle = (minutes * 6)
        hour_angle = ((hour % 12) + minutes/60) * 30
        # We set our lowest one to be the origin
        diff = abs(minute_angle -  hour_angle)
        return min(diff, 360 -  diff)
        