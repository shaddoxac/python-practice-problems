# This problem was asked Microsoft.

# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.




def readN(n: int):
    res = ""
    while n > 0:
        if n < 8:
            res += read7()[:n]
            return res
        else:
            res += read7()
            n -= 7
        