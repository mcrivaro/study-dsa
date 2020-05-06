from timeit import default_timer as timer

def hasPairWithSum(array, sum):
  start_time = timer()
  for item in array:
   for i in range(array.index(item)+1,len(array)):
     if int(item)+int(array[i])==sum:
      end_time = timer()
      print(end_time-start_time)
      return True
  end_time = timer()
  print(end_time-start_time)
  return False
#O(n^2) Time Complexity
#O(1) Space Complexity

def hasPairWithSum2(array, sum):
  start_time = timer()
  myset = set()
  for item in array:
    if int(item) in myset:
      end_time = timer()
      print(end_time-start_time)
      return True
    else:
      myset.add(sum-int(item))
  end_time = timer()
  print(end_time-start_time)
  return False
#O(n) Time Complexity (One loop, set has constant(=O(1)) lookup)
#O(n) Space Complexity (myset filled depending on size of array => O(n))

if __name__ == "__main__":
  arr = [i for i in range(0,1000001)]
  sum = 123456
  print(hasPairWithSum(arr,sum))
  print(hasPairWithSum2(arr,sum))