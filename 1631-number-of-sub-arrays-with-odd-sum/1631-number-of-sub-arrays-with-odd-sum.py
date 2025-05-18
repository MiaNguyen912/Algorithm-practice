class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Since the answer can be very large, return it modulo 10^9 + 7.
        # for example, result = (result + x)% m = (result%m + x%m) % m -> we reduce the number at each step, instead of calculate the final result and then % m, avoid result getting to large
        # P: prefix sum
        # - generate pre[] with pre[i] = sum of items in arr upto index i
        # - for each i, we'd want to find number of indices x s.t pre[i] - pre[x] is an odd number
        #   => pre[i] and pre[x] are 1 odd and 1 even
        #   => use a map to count number of odd/even numbers in pre upto i at each i

        pre = [0]*len(arr)
        pre[0] = arr[0]
        for i in range(1, len(arr)):
            pre[i] = pre[i-1] + arr[i]
        mp = defaultdict(int)
        MOD = (10**9 + 7)
        mp[0] = 1 # sum of ([] %2) = 1
        count = 0
        for i in range(len(arr)):
            count = (count + mp[(pre[i]%2 + 1)%2]) % MOD
            mp[pre[i]%2] += 1
        return count 
