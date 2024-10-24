# Here we define variables
Number1, Number2 = 1, 2
Answer = 0

# WE make a while the number is below 4 million which replicates the Fibonacci sequence
while Number1 <= 4000000:
    if Number1%2==0:
        Answer += Number1

    Number1, Number2 = Number2, Number1 + Number2
print(Answer)
