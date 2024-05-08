#Sarai Ayon
#4/14/2024
# CS240 Data Structures and Algorithms
# Week2_insertion_sort_algorithm.py
#resource : https://www.youtube.com/watch?v=JU767SDMDvA




# Import List from typing module
from typing import List

# Define the insertion_sort function that takes a list of integers as input and returns None as output
def insertion_sort(arr: List[int]) -> None:
    # Go through 1 to len(arr) elements. Len= length of the array , arr = array of integers 
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        # Compare the key with the elements to the left of it 
        while j >=0 and key < arr[j] :
                # Move the elements to the right 
                arr[j+1] = arr[j] 
                # Decrement the index 
                j -= 1
                # Insert the key in the right position 
        arr[j+1] = key
        # End of the function

# Specify the file path
file_path = 'C:\\Users\\Sarai Ayon\\OneDrive - Whatcom Community College\\Spring 2024\\CS240 Database Structure & Algorithms\\Week 2 Linked List\\numbers.txt.txt'

# Read the numbers from the file
with open(file_path, 'r') as f:
    # Convert the numbers to a list of integers 
    arr = [int(num) for num in f.read().split()]
  # Print the unsorted array
  
# Test the function
#insertion_sort(arr)
# Print the sorted array
#print ("Sorted array is:", arr)

#HW Test What value is in position 7586?
value_at_7586 = arr[7585]
print("Value at position 7586 is:", value_at_7586)

