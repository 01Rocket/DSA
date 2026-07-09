class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        # Sort cars by their starting position
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            # Time taken to reach the target
            time = (target - pos) / spd

            # New fleet if this car cannot catch the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)