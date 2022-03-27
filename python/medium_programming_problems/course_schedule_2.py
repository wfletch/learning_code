class Solution:
    NOT_CHECKED = 1
    CHECKING = 2
    CHECKED = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Let's build our adj matrix
        adj_matrix = defaultdict(list)
        # A Pair [a,b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_matrix[src].append(dest)
        # Create our topological sorted order. This is a stack implemented via a list
        topological = []
        
        # Initial Conditions. All state is NOT_CHECKED
        state = {n: Solution.NOT_CHECKED for n in range(numCourses)}
        
        # Variable to maintain throughout dfs check of if this is possible or not
        is_possible = True
        def dfs(node):
            nonlocal is_possible
            
            #Fail if this is not possible
            if not is_possible:
                return
            
            # Now we start the recursive Process. i.e we check
            state[node] = Solution.CHECKING
            
            # Check if we have dependencies
            if node in adj_matrix:
                for neighbor in adj_matrix[node]:
                    if state[neighbor] == Solution.NOT_CHECKED:
                        # Check
                        dfs(neighbor)
                    elif state[neighbor] == Solution.CHECKING:
                        # We have a loop
                        is_possible = False
                # We have checked
            state[node] = Solution.CHECKED
            topological.append(node)
        
        # Now iterate through the pre-requsities
        for course in range(numCourses):
            if state[course] == Solution.NOT_CHECKED:
                dfs(course)
        return topological[::-1] if is_possible else []

        #LC # 210
        #Time: O(V+E)
        #Space: O(V+E) 