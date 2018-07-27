n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    for numbers2 in numbers:
        results.append(numbers2) 
  return results
print (flatten(n))
