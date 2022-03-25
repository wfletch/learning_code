class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(lambda: [])
        for entry in prerequisites:
            courses[entry[0]].append(entry[1])
        #Let's iterate through each course in a DFS manner and backtrack as needed
        path = [False] * numCourses
        def find_cycle(current):
            if path[current] == True:
                return True
            else:
                path[current] = True
                # Backtrack
                for child in courses[current]:
                    if find_cycle(child):
                        return True
                # Remove ourselves. We are done
                path[current] = False
                return False
        for c in list(courses.keys()):
            if find_cycle(c):
                return False
        return True
        # LC # 207
        # Space: O(V + E) Each Vertex requires edge level depth.
        # Time: O(V^2 + E) It takes us E to build the graph. V is the number of course and for each one we have to do a search
        class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(lambda: [])
        for entry in prerequisites:
            courses[entry[0]].append(entry[1])
        #Let's iterate through each course in a DFS manner and backtrack as needed
        path = [False] * numCourses
        # Let's Create a check bitmap
        checked = [False] * numCourses
        # We could combine these two bitmaps into one single bitmap with multiple states.
        def find_cycle(current):
            if checked[current] == True:
                # We have been here before and valdiated it, no need to redo
                return False
            if path[current] == True:
                return True
            else:
                path[current] = True
                # Backtrack
                for child in courses[current]:
                    if find_cycle(child):
                        return True
                # Remove ourselves. We are done
                path[current] = False
                
                checked[current] = True
                return False
        for c in list(courses.keys()):
            if find_cycle(c):
                return False
        return True
        
        # Time : O(V + E) as we make sure we don't check again. This is significantly better
        # Space: O(V + E) 