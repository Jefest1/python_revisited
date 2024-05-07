class Solution(object):
    def destCity(self, paths):
        """ 
        Problem Statement:
        You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
        It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
        """

        """
        :type paths: List[List[str]]
        :rtype: str
        """
        # create a set of the paths
        start_path = set()

        # variable to store the destination city
        dest_city = 'None'

        # create a loop to loop through all paths and send to the path set
        for path in paths:
            start_path.add(path[0])

        # create a second loop to compare the end of the paths to see which one does not have a match in the path set
        for path in paths:
            if path[1] not in start_path:
                dest_city = path[1]
        print(dest_city)


# Creating paths
cities = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# Calling the method
destination = Solution()
destination.destCity(cities)
