import random

def printMaxActivities(s , f ): 
    n = len(f) 
    print ("The following activities are selected index")
    i = 0
    count = 0
    print (i), 
    for j in range(n): 
        if s[j] >= f[i]: 
            print (j), 
            i = j
            count += f[i]
            if (count > 24):
                break

def main():
    
    s = [] 
    f = []
    n = int(input("how many task do you enter : "))
    for i in range(n):
        st = random.randint(1,24)
        l = random.randint(1,5)
        fin = st + l
        if (fin > 24):
            fin = fin - 24
        s.append(st)
        f.append(fin)
        
    print("finish times")
    print(f)
    print("start time ")
    print(s)
    printMaxActivities(s , f)

    
if __name__ == "__main__":
    main()
