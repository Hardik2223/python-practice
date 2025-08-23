# nums=[1,2,3,4,5,6]
# sq=lambda a: a**2
# squares=[]
# for i in nums:
#     squares.append(i**2)
# print(squares)
# squares2=[sq(i) for i in nums]
# print(squares2)
# squares3= list(map(sq, nums))
# print(squares3)
# def is_even(n):
#    return n%2 == 0
# nums=[1,2,3,4,5,6,7,8,9,10]
# evens=[i for i in nums if i%2==0]
# print(evens)
# evens1= filter(is_even,nums)
# print(evens1)
# l = [1, 2, 3, 6, 5, 8]
# odds = list(filter(lambda x: x % 2 != 0,1))
# cubes = list(map(lambda x: x ** 3, odds))
# result = list(zip(odds, cubes))
# print(result)  # Output: [(1, 1), (3, 27),    
t=(1,2,3,5,8,4,43)
# m=sorted(t, reverse=True)
# print(m)
print(max(t))