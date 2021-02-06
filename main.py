import math 
import time
from bisect import bisect_left

class search:
  my_array = []
  start_time = time.time()
  # getter method 
  def get_my_array(self): 
    return self.my_array 
  # setter method 
  def set_my_array(self, x): 
    self.my_array = x 
  
  def get_start_time(self): 
    return self.start_time
  def set_start_time(self, x): 
    self.start_time = x 
  
  #LINEAR SEARCH
  def linear_search(self, the_array, x):
    is_not_inside = True
    for i in range(0, len(the_array)):
      if the_array[i] == x:
        is_not_inside = False
        print("Element is present at index", i)  
        break      
    if is_not_inside == True:
        print("Element is not presesnt")

  def linear_search2(self, the_array, x):
    is_not_inside = True
    for i in range(0, len(the_array)):
      if the_array[i] == x:
        is_not_inside = False
        return i
    if is_not_inside == True:
        return -1
  #BINARY SEARCH
  def binary_search(self, the_array, l, r, x):
    
    #l == left     
    #r == right
    #x == key

    #l usually equal to 0
    #r equal to n-1

    #make sure furthest right num location is bigger then eariest left number location in array
    if r >= l:

      #find index middle index location
      mid = l + (r-l)//2
      #//divides and rounds down to the nearest whole number

      #if the number in the mid location of the array is equal to the key
      if the_array[mid] == x:
        #returns mid bc value in middle is the key we are searching for
        return mid
      
      #if num in mid location of array is greater then the key we are searching for
      elif the_array[mid] > x:
        #using recursion to return and call the binarysearch function
        #r(the right index) is now 1 less from half of the original array
        new_r = mid-1
        return self.binary_search(the_array, l, new_r, x)
      
      #elif the_array[mid] < x
      #if num in mid location is less then the key
      else:
        #l is now the value greater from the mid location
        new_l = mid + 1
        return self.binary_search(the_array, new_l, r, x)
    #key is not present in the array
    else:
      return -1
    
  #JUMP SEARCH
  def jump_search(self, the_array, x, n):
    #n = size
    #most efficent wat to find stepping block size 
    #The value of the function ((n/m) + m-1) will be minimum when m = √n.
    #will usually be at the end of testing block
    step = math.sqrt(n)
    
    #Testing block parameters (prev, step)
    #start index of testing block
    prev = 0
    #while is finding block where x is present by testing the end of the JUMP BLOCK
    while the_array[int(min(step, n) - 1)] < x:
      #prev will be start location of jump block bc array[step-1] is less then x
      prev = step
      #step will be the 
      step += math.sqrt(n)

      #making sure prev index is before list size
      if prev >= n:
        return -1
    
    #runs first if value at mid index of array is bigger  then x. so array[prev=0] < x is tested
    #runs second after correct jump block is found in first while loop above
    #using linear-search to test for x where JUMP BLOCK begins through prev index location
    while the_array[int(prev)] < x:
      #incrementing prev with 1 for linear search in current while loop
      prev += 1

      #if incremented prev var reaches:
        #-the next block 
        #-or the end of list. 
      #Then x element is not present in the array
      if prev == min(step, n):
        return -1
    
    #if x element is found
    if the_array[int(prev)] == x:
      return prev
    return -1

  #INTERPOLATION SEARCH
  def interpolation_search(self, the_array, x, n):
    #find index of two corners of section serching
    #left corner will be low
    #right corner will be high
    lo = 0
    hi = (n - 1)

    #while lo less or equal to hi 
    #AND x is larger then or equal to array value @ low index
    #AND x is smaller then or equal to array value @ high index
    while lo <= hi and x >= the_array[lo] and x <= the_array[hi]:
      if lo == hi:
        if the_array[lo] == x:
          return lo
        return -1 

      #pos is mid point that wil be checked
      pos = lo + int(((float(hi - lo) / (the_array[hi] - the_array[lo])) * (x - the_array[lo])))

      #if index position in array is equal to x
      if the_array[pos] == x:
        # print("x == array[pos]")
        return pos
      
      #if x is larger then index pos, then x is in upper part
      if the_array[pos] < x:
        # print("x is bigger then array[pos]")
        lo = pos + 1
      
      #if x is smaller then index pos, then x is in lower part
      else:
        hi = pos - 1
        # print("x is bigger then array[pos]")

    return -1

  #EXPONENTIAL SEARCH
  def exponential_search(self, the_array, x, n):
    #checks if first item in array is equal to x
    if the_array[0] == x:
      return 0
    
    #INDEX var. Already checked index at 0
    i = 1

    #WHile loop used to find the range we will be iterating through
    #while I less then size
    #AND while array at index i is less then and equal to x
    #if both are true, i value is doubled
    while i < n and the_array[i] <= x:
      i = i * 2

    #do binary search with new l and r values from range
    return self.binary_search(the_array, int(i/2), min(i, n-1), x)
  
  def fibonacci_search(self, the_array, x, n):
    #fibMonaccianSearch
    fib2 = 0  #(m-2)'th
    fib1 = 1 #(M-1)'th
    fibM = fib2 + fib1  #m'th fib num

    #fibM will store smallest Fibonacci num greater or equal to n
    while fibM < n:
      fib2 = fib1
      fib1 = fibM
      fibM = fib2 + fib1

    offset = -1

    while fibM > 1:
      i = min(offset + fib2, n-1)

      if the_array[i] < x:
        fibM = fib1
        fib1 = fib2
        fib2 = fibM - fib1
        offset = i
      
      elif the_array[i] > x:
        fibM = fib2
        fib1 = fib1 - fib2
        fib2 = fibM - fib1
      
      else: 
        return i
    
    if fib1 and the_array[offset+1] == x:
      return offset+1
    
    return -1




  def time_test(self, the_array, x, n, l, r):
    #x == key
    #n == array size
    #l == most left index
    #r == most right index
     
    #LINEAR SEARCH TEST
    self.set_start_time(time.time())
    time_start_linear = self.get_start_time()
    linear_r = self.linear_search2(the_array, x)
    time_finish_linear = time.time()

    time_total_linear = time_finish_linear - time_start_linear

    local_start = time.asctime( time.localtime(time_start_linear) )
    local_finish = time.asctime( time.localtime(time_finish_linear) )

    print("Linear Search Algorithm found x at index {} in {:f} seconds".format(linear_r, time_total_linear))
    # print("Start Time:", time_start_linear)#local_start_cesar_lopez
    # print("Finish Time:", time_finish_linear)

    #BINARY SEARCH TEST
    self.set_start_time(time.time())
    time_start_binary = self.get_start_time()    
    bin_r = self.binary_search(the_array, l, r, x)
    time_finish_binary = time.time()

    time_total_binary = time_finish_binary - time_start_binary

    print("Binary Search Algorithm found x at index {} in {:f} seconds".format(bin_r, time_total_binary))

    #JUMP SEARCH TEST
    self.set_start_time(time.time())
    time_start_jump = self.get_start_time()    
    jump_r = self.jump_search(the_array,x, len(the_array))
    time_finish_jump = time.time()

    time_total_jump = time_finish_jump - time_start_jump

    print("Jump Search Algorithm found x at index {} in {:f} seconds".format(jump_r, time_total_jump))

    #INTERPOLATION SEARCH TEST
    self.set_start_time(time.time())
    time_start_interp = self.get_start_time()    
    interp_r = self.interpolation_search(the_array, x, len(the_array))
    time_finish_interp = time.time()

    time_total_interp = time_finish_interp - time_start_interp

    print("Interpolation Search Algorithm found x at index {} in {:f} seconds".format(interp_r, time_total_interp))

    #EXPONENTIAL SEARCH TEST
    self.set_start_time(time.time())
    time_start_expon = self.get_start_time()    
    expon_r = self.exponential_search(the_array, x, len(the_array))
    time_finish_expon = time.time()

    time_total_expon = time_finish_expon - time_start_expon

    print("Exponential Search Algorithm found x at index {} in {:f} seconds".format(expon_r, time_total_expon))

    #FIBONACCI SEARCH
    self.set_start_time(time.time())
    time_start_fib = self.get_start_time()    
    fib_r = self.fibonacci_search(the_array, x, len(the_array))
    time_finish_fib = time.time()

    time_total_fib = time_finish_fib - time_start_fib

    print("Fibonacci Search Algorithm found x at index {} in {:f} seconds".format(fib_r, time_total_fib))


    



    

#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------



#to print index result for individual search algorithms
def print_find_result(index_retuned):
  if index_retuned != -1:
    print("Element is present at index % d" % index_retuned)
  else: 
    print ("Element is not present in array")

#public static void main
def main():
  array1 = [0,10,12,15,19,20,25,200,50,55,30,22,202,111]
  
  array2 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30, 33, 35, 38, 40]
  #array1 = array2
  #in order for binary search to work, arraylist must be sorted.
  array1.sort()
  print(array1)

  print("\nWhat type of searching algorithm do you want to use?")
  print("1) Linear Search\t\tO(n)\n2) Binary Search\t\tO(log(n))\n3) Jump Search\t\t\tO(sprt(n)\n4) Interpolation Search\tBest: 1\tAvg: log(log(n))\tWorst: O(n)\n5) Exponential Search\tO(Log n)\n6) Fibonacci Search\t\tO(log(n))\n7+) Time Test")

  choice = input("Search Type Choice: ")
  choice = int(choice)

  x = input("\nNumber to Search: ")
  x = int(x)
  search1 = search()

  #LINEAR SEARCH CHOICE
  if choice == 1:
    search1.set_start_time(time.time())
    time_start = search1.get_start_time()

    #search1.linear_search(array1, x)
    linear_r = search1.linear_search2(array1, x)

    print_find_result(linear_r)

    time_finish = time.time()
    time_total = time_finish - time_start
    print("Time:", time_total)
  #BINARY SEARCH CHOICE
  elif choice == 2:
    search1.set_start_time(time.time())
    time_start = search1.get_start_time()
    
    l = 0
    r = len(array1)-1
    bin_r = search1.binary_search(array1, l, r, x)

    print_find_result(bin_r)

    time_finish = time.time()
    time_total = time_finish - time_start
    print("Time:", time_total)
  #JUMP SEARCH CHOICE
  elif choice == 3:
    search1.set_start_time(time.time())
    time_start = search1.get_start_time()
    print(time_start)

    jump_r = search1.jump_search(array1,x, len(array1))
    
    print_find_result(jump_r)
    
    time_finish = time.time()
    time_total = time_finish - time_start
    #is timeaffacted
    print("Start:", time_start, " Finish: ", time_finish)
    print("Time:", time_total)
  #INTERPOLATION SEARCH CHOICE
  elif choice == 4:
    interp_r = search1.interpolation_search(array1, x, len(array1))

    print_find_result(interp_r)
  #EXPONENTIAL SEARCH CHOICE
  elif choice == 5:
    expon_r = search1.exponential_search(array1, x, len(array1))

    print_find_result(expon_r)
  elif choice == 6:
    fib_r = search1.fibonacci_search(array1, x, len(array1))

    print_find_result(fib_r)
  #TIME TEST
  else:
    print("\nTime Test:\n")
    l = 0
    r = len(array1)-1

    search1.time_test(array1, x, len(array1), l, r )



    

  

main()
