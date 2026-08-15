class Solution:
    def trap(self, height: List[int]) -> int:
        # def get_max_neighbour_height(index, direction):
        #     if direction == "left":
        #         return max(height[:index])
        #     if direction == "right":
        #         return max(height[index+1:])

        trapped = 0

        n = len(height)


        left_max = [0] * n
        right_max = [0] * n
        
        current_max = 0
        for i in range(n):
            current_max = max(current_max, height[i])
            left_max[i] = current_max

        i = n -1
        current_max = 0
        while i > -1:
            current_max = max(current_max, height[i])
            right_max[i]=current_max
            i -= 1

        # print(f"left max {left_max}")
        # print(f"right max {right_max}")

        for i in range(1, n-1):
            # max_left_height = get_max_neighbour_height(i, "left")
            # max_right_height = get_max_neighbour_height(i, "right")
            # print(f"max_left_height {max_left_height}, max right height {max_right_height}")
            max_left_height = left_max[i-1]
            max_right_height = right_max[i+1]

            # print(f"index {i} height {height[i]} max_left_height {max_left_height}, max right height {max_right_height}")
            t = min(max_left_height, max_right_height) - height[i]
            # print(f"trapped {t}")
            # print(f"index {i} trapped {t}")
            if t > 0:
                trapped += t
        return trapped



