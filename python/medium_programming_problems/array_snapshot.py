class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[[-1,0]] for _ in range(length)]
        self.snapshot_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append([self.snapshot_id, val])
        

    def snap(self) -> int:
        self.snapshot_id +=1
        return self.snapshot_id -1
        

    def get(self, index: int, snap_id: int) -> int:
        # Binary search
        i = bisect.bisect_left(self.snapshots[index], [snap_id +1]) -1
        return self.snapshots[index][i][1]
        

    # LC 1146
    # Time: O(NLgN)
    # Space: O(n)
    # We don't need to store all edits for the same snapshot_id, we can hold only the most recent, if needs be
