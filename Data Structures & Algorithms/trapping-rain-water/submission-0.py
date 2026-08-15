class Solution:
    def trap(self, height: List[int]) -> int:
        def get_max_neighbour_height(index, direction):
            if direction == "left":
                return max(height[:index])
            if direction == "right":
                return max(height[index+1:])

        trapped = 0

        for i in range(1, len(height)-1):
            max_left_height = get_max_neighbour_height(i, "left")
            max_right_height = get_max_neighbour_height(i, "right")
            # print(f"max_left_height {max_left_height}, max right height {max_right_height}")
            t = min(max_left_height, max_right_height) - height[i]
            # print(f"index {i} trapped {t}")
            if t > 0:
                trapped += t
        return trapped



