class Equilibrium:
    @staticmethod
    def equilibrium_index(array):
        prefix = [array[0]]

        for i in range(1, len(array)):
            prefix.append(prefix[i - 1] + array[i])
        n=prefix[-1]
        for i in range(1,len(prefix)):
            if prefix[i-1] == n-prefix[i]:
                return i


array = list(map(int, input().split()))
result = Equilibrium()
print(result.equilibrium_index(array))




