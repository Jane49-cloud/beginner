# names = ['jane', 'john', 'james', 'pauline']
# print(names)
#
# numbers = [2, 4, 5, 6, 9, 33]
# max = numbers[0]
# for number in numbers :
#     if number>max:
#         max = number
# print(number)
# nums = [8, 40, 8, 4, 8, 3, 2]
# min = nums[0]
# for n in nums:
#     if n< min:
#         min = n
#         print(min)
#
#

numbers = [4, 5, 6, 4, 6, 4, 5, 8]
uniques = []
for number in numbers:
    if number not in uniques:
      uniques .append(number)
print(uniques)
