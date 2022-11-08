#  Write a Python program to returns sum of all divisors of a number
def sum_div(num):
    divisors=[1]
    for i in range(2,num):
    
        if(num%i)==0:
            divisors.append(i)
    return sum(divisors)        
print(sum_div(8))        