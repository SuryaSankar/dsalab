# https://leetcode.com/problems/asteroid-collision/description/


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack

if __name__ == '__main__':
    solution = Solution()
    # Test 1
    asteroids = [5, 10, -5]
    # After 5 and 10 collide, the 10 becomes 5. No more collisions are possible.
    assert solution.asteroidCollision(asteroids) == [5, 10]
    # Test 2
    asteroids = [8, -8]
    # The 8 and -8 collide and explode.
    assert solution.asteroidCollision(asteroids) == []
    # Test 3
    asteroids = [10, 2, -5]
    # The 10 and 2 collide, and 2 becomes -2.
    # The 10 and -2 collide, resulting in 10.
    assert solution.asteroidCollision(asteroids) == [10]
    # Test 4
    asteroids = [-2, -1, 1, 2]
    # The -2 and -1 are moving left, while the 1 and 2 are moving right.
    # Asteroids moving the same direction never meet, so no asteroids will meet each other.
    assert solution.asteroidCollision(asteroids) == [-2, -1, 1, 2]
    # Test 5
    asteroids = [-2, -2, 1, -2]
    # The first two asteroids will collide and become -2.
    # The second and third asteroids will collide and become -2.
    # The third and fourth asteroids will collide and become -2.
    assert solution.asteroidCollision(asteroids) == [-2, -2, -2]
    print("All test cases passed successfully.")