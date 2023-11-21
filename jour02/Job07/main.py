alphabet = "abcdefghijklmnopqrstuvwxyz"

def pyramide(n):
    for i in range(n):
        print(alphabet[:i+1])

pyramide(len(alphabet))
