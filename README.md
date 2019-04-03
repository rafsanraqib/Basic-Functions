# Basic-Functions
Simple functions developed using Python

1. cat_dog(): This function accepts a string argument and checks whether the number of times the word 'cat' mentioned 
is the same as the number of time the word 'dog' is mentioned. Returns true if they are equal or else false

2. has22(): This function takes a list as an argument and returns true if there is a 2 adjacent to another 2

3. make_chocolate(): This function returns true if the argument small and big can be combined to produce the argument goal. Small 
corresponds to 1 kilos and big corresponds to 5 kilos. 
Example make_chocolate(1,5,11) will result in true because using 2 out of the 5 from big will give (5*2) = 10 and then adding the one small 
will give 10 + 1 = 11 which is equal to the goal. 

4. repeat_chars(): This function accepts a string argument and prints the repeated chars only.

5. unique_string(): This function accepts a string argument and prints the string without any repeats. Utilized sets in python

6. close_far(a,b,c): Expects three ints and returns true if either b or c is within 1 away from a while the other is 10 or greater than a.

7.unsorted_list_sum(lst, sum): Checks every entry of the list using a loop and checks if there are two same entries adjacent
and if their sum is equal to the sum in the argument. 

8. sorted_list_sum(lst,sum): Same function as number 7 but this time the list is sorted. 

9. has_repeats(lst): Checks whether the given list has repeated elements. Does not use list, makes use of the data structure
set in python.

10. first_recuring(lst): Iterates through the list and finds the first recurring character and returns is. Uses python 
dictionary. 

* Example tests are included in the code. Uncomment and run
