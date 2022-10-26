def solution(numlist):
    counter = 0
    for i in range(len(numlist)): #first number
        for j in range(len(numlist)): #second number
            if numlist[j] % numlist[i] == 0: #check if divisible
                for k in range(len(numlist)): #third number
                    if numlist[k] % numlist[j] == 0: #check if divisible
                        if i < j < k: #check ranges **
                            counter += 1
    return counter
print(solution([1,2,3,4,5,6]))

#** program could be made more efficient by reducing the range of the for loop
#to incorporate the i < j < k requirement, omitted for the sake of negligibility.
