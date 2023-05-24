# Find the shortest possible route that a salesperson can take to visit a given 
# set of cities exactly once and return to the starting city. The salesperson must 
# visit every city on the list, and the distance or cost of travel between each pair 
# of cities is known.

#if you were to brute force this problem, the time complexity would be O(N!)
#optimize this with dynamic programming.

import sys

#adjacency matrix representation of graph with weights
am = [[0,10,15,20],
     [5,0,9,10],
     [6,13,0,12],
     [8,8,9,0]]
# am = [[0,10,3],[1,0,20],[15,2,0]]

n = len(am[0]) #set the number of nodes

visited = [False] * n
DP = [[-1] * n for _ in range(n)] #memoization for the dp approach

def TSP(curr_node, num_visited):
    #base case
    if num_visited == n:
        # Returns the path and distance to the starting node
        return [0], am[curr_node][0]

    if DP[curr_node][num_visited] != -1:
        #if the combination has already been done, get the result from the memoized dp table
        return DP[curr_node][num_visited]

    min_path = []
    min_distance = sys.maxsize

    for next_node in range(n):
        if not visited[next_node]:
            visited[next_node] = True #set to true to make sure that every node only gets visited once 
            path, distance = TSP(next_node, num_visited + 1) #recursively goes through the next node numerically
            new_distance = am[curr_node][next_node] + distance #gets the weight of the current node combination and adds it to the current weight

            if new_distance < min_distance: #sets new values if a new minimum is found
                min_distance = new_distance
                min_path = [curr_node] + path

            visited[next_node] = False #this step is essential for backtracking and checking other paths when the curr_node changes

    DP[curr_node][num_visited] = (min_path, min_distance) #store the values as a tuple in the dp table with (path, distance)
    return DP[curr_node][num_visited]

if __name__ == "__main__":
    visited[0] = True #mark the starting node as visited
    path, distance = TSP(0, 1) #start the function at node 0 and visisted cities = 1
    print("Optimal Path:", path)
    print("Total Distance:", distance)



#the answer should be, minimum path: 0->1->3->2->0 with a weight of 35

