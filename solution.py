#QUESTION 1
print("---------------")
print("Question 1")
def max_num(a=0,b=0,c=0):
    return max(a,b,c)
print(max_num(1,2))
print(" ")

#QUESTION 2
print("Question 2")
def mult_list(nums):
    if len(nums) == 0:
        return 0
    nlist=nums[0]
    if len(nums) > 1:
        for i in nums[1:]:
            nlist= nlist*i
    return nlist
print(mult_list([1,2,3,4]))
print(" ")

#QUESTION 3
print("Question 3")
def rev_string(string):
    rev=string[::-1]
    return rev
print(rev_string("Test"))
print(" ")

#QUESTION 4
print("Question 4")
def num_within(a,b,c):
    if a>=b and a<=c:
        return True
    else:
        return False

print(num_within(3,1,5))
print(" ")

#QUESTION 5
print("Question 5")
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)