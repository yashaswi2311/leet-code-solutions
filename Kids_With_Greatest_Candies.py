def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    result = []
    for i in range(len(candies)):
        if (candies[i] + extraCandies >= max_candy):
            result.append(True)
        else:
            result.append(False)
    return result

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

