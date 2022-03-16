#给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
def sort(nums):#冒泡排序函数
    length=len(nums)
    while length>0:
        for i in range(length-1):
            if nums[i]>nums[i+1]:
                x=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=x
        length-=1
    return nums
def repeat(nums):#检查重复函数，对排序完成的数组相邻元素查重
    length = len(nums)
    for i in range(length-1):
        if nums[i]==nums[i+1]:
            print("true")
            break
    else:
        print("false")

if __name__ == '__main__':
    arr = input("输入一个一维数组，每个数之间使空格隔开：")
    nums = [int(n) for n in arr.split()]  # 初始化数组,命名为nums
    repeat(sort(nums))#调用函数先排序再查重
