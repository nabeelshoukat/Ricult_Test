'''
    Step#1  : used English to elaborate the solutions.
    Step#2  : Used Python
    Step#3  : The time complaxity of
                Q#2 is O(n^2) as it is using two for loops s
                Q#3 is O(n) as a built in method Counter() itterates over the list to find out most occuring number.

    Step#4   : 
            Q#2 :I have choosen this solution because it is the  most effective way to find out the opposite numbers, Only for required type(negative) of number are selected
            ,then the  loop runs only for that checks instead of complete list,This is it's main adwantage to choose.
            The data structure used for this method is 'list'.
            Q#3 : The selection of Counter() function , as it reduces the count of lines of code and work really efficiently,That's the main adwantage of this method.
                The data structure used for this method is also 'list'.
    Step#5 :
            Q#2 : I have choosen this method as it requirs less memory consumption and itterations. That's why is being used.
                There can be a couple of other solutions for this perticuler problem,while it seems to be one of the best ,while others may use a lot of memory than this algo. and cpu usage.
            Q#3 : I have choosen this method as it requirs less memory consumption with less count of lines  and itterations.
                There can be a couple of other solutions for this perticuler problem,while it seems to be one of the best ,while others may use a lot of memory than this algo. and cpu usage.
    Step#6 : built in methods are also used in these solutions. 
'''



# Q#2 solution:

input_data=[20,59,44,52,95,-21,-20,78] # data points to be work with
results=[]           # store the final results
for i in input_data: # itterate over the list (input_data)
    if i<0:          # check if number is less than 0 , only compare then.
        for j in input_data: # itterate over the list to check for equelence.
            if j==abs(i):    # convert the number into positive numbers for comparison
                results.extend([j,-abs(j)]) # store the results to list for final usage.
                
print(results)                # print the reqd. results

# Q 3.
 
input_data=[20,59,44,52,95,-21,20,78] # data points to be work with

from collections import Counter

def most_frquent_number(lst):
    results = Counter(lst)            # passing the list through counter
    return results.most_common(1)[0][0] # return the most occurence with number and count as(number,occurence), pickup only first so [0][0] is used

print(most_frquent_number(input_data)) # checkout the reqd. results

 
