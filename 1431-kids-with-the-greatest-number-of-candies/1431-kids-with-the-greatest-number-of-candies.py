class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Step 1: get current max candies
        maxCandies = 0
        for c in candies:
            if c > maxCandies:
                maxCandies = c

        # Step 2: build result
        result = []
        for c in candies:
            if c + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)

        return result
        