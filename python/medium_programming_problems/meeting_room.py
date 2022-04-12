class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # We can use a heap to keep track of the rooms in use.
        # We will sort the heap based on the earliest end time. 
        # Whenever we look at a new meeting, we will check to see if the
        # most recent meeting has ended (and thus the room ebcomes free)
        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1]) # Push end time of first meeting
        for meeting in intervals[1:]:
            if free_rooms[0] <= meeting[0]:
                # We can use this meeting room
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, meeting[1])
        return len(free_rooms)
    
        
        