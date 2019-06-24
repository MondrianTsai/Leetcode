# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:53:39 2019

@author: cheryl.cai

https://leetcode.com/problems/remove-duplicates-from-sorted-array

Description: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
             Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

#Use dictionary (not meet the case)
def removeDuplicates(nums):
    dic = dict()
    if len(nums) == 0:
        return
    else:
        for i in range(0, len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = 0 
    print(list(dic.keys()))
    return len(list(dic.keys()))
    

#Use set (not meet the case)
def removeDuplicates2(nums):
    nums = list(set(nums))
    nums.sort()
    print(nums)
    return len(nums)


def removeDuplicates3(nums): #Accepted
    dif_num = 1
    if len(nums) == 0:
        return 0 
    else:
        for i in range(0, len(nums)):
            if (i+1) < len(nums):
                if nums[i] < nums[i+1]:
                    nums[dif_num] = nums[i+1]
                    dif_num += 1
    print(nums)
    return dif_num

