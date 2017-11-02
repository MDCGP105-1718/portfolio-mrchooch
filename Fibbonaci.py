def fib(n):
    fibseq=[0,1]
    for i in range(n-1):
        fibseq.append(fibseq[i]+fibseq[i+1])
    print(fibseq[n])

fib(int(input("Find Xth Fibonacci Number: ")))
