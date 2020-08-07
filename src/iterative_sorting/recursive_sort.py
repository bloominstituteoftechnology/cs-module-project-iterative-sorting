

def countdown(n):
    # base case note - basecase is not always first
    if n == 0: #basecase 
        return
    print(n)
    countdown(n-1)
    countdown(n-1)

countdown(3)