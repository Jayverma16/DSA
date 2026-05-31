
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        
        asteroids.sort()
        for asteroid in asteroids:
            if mass >= asteroid:
                mass = mass + asteroid
            else:
                return False
            

        return True
if __name__ == "__main__":
    sol = Solution()
    mass = 5
    asteroids = [4,9,23,4]
    ans = sol.asteroidsDestroyed(mass, asteroids)
    print(ans)