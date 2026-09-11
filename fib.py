import sys

def fibonacci(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

if __name__ == "__main__":
    if len(sys.argv) != 2:
        n = int(input("How many Fibonacci numbers should I generate: "))
    else:
        n = int(sys.argv[1])
    print(*fibonacci(n))

#model: gpt-5.6-sol
#----USAGE----
#Input tokens: 56
#Output tokens: 185
#Reasoning tokens: 38
#Estimated cost: $0.00392400
