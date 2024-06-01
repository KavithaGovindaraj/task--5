

# problem -using python filter( function)


data =[10, 501, 22, 37, 100, 999, 87, 351] 
  
result = filter (lambda x:x>=4, data)
 
print(list(result))

[10, 501, 22, 37, 100, 999, 87, 351]

 




# programe -using lambda function
def check_elements (lst) :
    result = all(map(lambda x:isinstance(x, (int,str)),lst))
    print(result)

list1 = [1,'banana', 10,'apple', 3.14]
list2 = [11,'banana', 10,'apple']

check_elements(list1)
check_elements(list2)









                 


# programe -using Genarator function:


fibonacci = lambda n: [0, 1] + [0] * (n - 2)
fib_series = fibonacci(50) 

# Fill in the Fibonacci series
for i in range(2, 50):
    fib_series[i] = fib_series[i - 1] + fib_series[i - 2]

# Print the series
print(fib_series)










import re
def validation():
    email ="tester@gmail.com"
    email_pat = r"^[a-zA-Z0-9._%-+]+(\.[a-zA-Z0-9._%-+]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pat, email):
        print(f"{email} is  valid")
validation()





import re
def validation():  
    Bangladesh = "+8801760123128"  
    Bangladesh_pat =  r"^(?:\+?88)?01[3-9]\d{8}$"
    if re.match (Bangladesh_pat, Bangladesh):
        print(f"{Bangladesh} is  valid")
validation()






import re
def validation():  
    USA = "+1-(123)-526-4589"
    USA_pat = r"^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$" 
    if re.match (USA_pat, USA):
       print(f"{USA} is  valid")
validation()






import re
def validation():  
    Password = "K1TNBGRsdUv3ytjF"
    Password_pat =  r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()-_+=])[A-Za-z0-9!@#$%^&*()-_+=]{16}$"
    if re. match (Password_pat, Password):
        print(f"{Password} is  valid")
validation()
   









































