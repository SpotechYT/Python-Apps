import requests

def Mile_Stone(first):
    website = "https://maker.ifttt.com/trigger/Mile_Stone/with/key/jGYsiNBKfqOrI60cCfvYWACoOg3rmyDZ-TDSdA50bVw"
    report = {}
    report["value1"] = first
    requests.post(website)

def collatz_sequence(x, y):
    num_seq = [x]
    collatz_sequence.z = 0
    saidIt = False
    z = 0
    if x < 1:
        return []

    while x > 1:
        z += 1
        if saidIt == False:
            print(str(y) + ": Working...")
            saidIt = True

        if x % 2 == 0:
                x = x / 2
        else:
                x = 3 * x + 1
        
        num_seq.append(int(x))  

    with open(r'Results.txt', 'a') as f:
        f.write("\n")
        f.write(str(int(y)) + ":")
        for item in num_seq:
            f.write(" " + str(item))
        f.close()
    
    return y

y = 2
while True:
    collatz_sequence(y, y)
    print(str(y) + ": FAILED")
    if y == 1000000 or 1000000000 or 1000000000000 or 1000000000000000 or 1000000000000000000 or 100000000000000000000 or 200000000000000000000 or 300000000000000000000 or 400000000000000000000 or 500000000000000000000 or 1000000000000000000000:
        Mile_Stone(y)
    y += 1