"""
Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так, чтобы их сумма составлялаtarget .

Вы можете предположить, что каждый вход будет иметь ровно одно решение , и вы не можете использовать один и тот же элемент дважды.

Вы можете вернуть ответ в любом порядке.



Пример 1:

Ввод: nums = [2,7,11,15], target = 9
 Выход: [0,1]
 Объяснение: поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].
Пример 2:

Ввод: nums = [3,2,4], цель = 6
 Вывод: [1,2]
Пример 3:

Ввод: nums = [3,3], цель = 6
 Вывод: [0,1]


Ограничения:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Существует только один действительный ответ.


Продолжение:  Можете ли вы придумать алгоритм, сложность которого меньше временной?O(n2)
"""

class Solution(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        used = {}

        for i, x in enumerate(nums):
            print(f"i: {i}, x: {x}")
            diff = target - x
            if diff in used:
                return [used[diff], i]
            else:
                used[x] = i
        return

my_nums = [2,11,15,7]
my_target = 9
my_result = Solution.twoSum(my_nums, my_target)
print(my_result)