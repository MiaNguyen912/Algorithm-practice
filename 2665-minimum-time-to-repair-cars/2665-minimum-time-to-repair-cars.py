class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # A mechanic with a rank r can repair n cars in r * n^2 minutes. => n = sqrt(time/r)
        #   ex: rank 4 -> repair 4 cars in 16min; 2 cars in 4mins
        # find min time taken to repair all cars.
        # Note: All the mechanics can repair the cars simultaneously.


        def check(mid):
            count_cars = 0
            for r in ranks:
                count_cars += floor(sqrt(mid/r))
            return count_cars >= cars

        l,r = 1, min(ranks) * cars**2 # (max(ranks) * cars**2) is the worst case if the slowest mechanic has to repair n cars
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l