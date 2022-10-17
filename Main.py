from typing import List

def merge_sort(data) -> None:
  # Write code here
  if len(data)>1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k]=left[i]
                i=i+1
            else:
                data[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            data[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            data[k]=right[j]
            j=j+1
            k=k+1

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
