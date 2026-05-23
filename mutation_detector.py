y= list(input("Enter the original DNA sequence: "))
m= list(input("Enter the Changed DNA sequence: "))      
def Upp(y):
    x=[]
    for i in y:
        x.append(i.upper())
    return x
Y=Upp(y)
M=Upp(m)
mutation= False 

purines = ["A", "G"]
pyrimidines = ["C", "T"]

if len(Y) == len(M):
    for i in range(len(Y)):
        if Y[i] != M[i]:
            mutation= True
            print("Mutation detected at position",i+1)
            print(Y[i],"changed to",M[i])
            print("Type of mutation: Substitution")
            if ((Y[i] in purines and M[i] in purines) or (Y[i] in pyrimidines and M[i] in pyrimidines)):
                print("Type of mutation: Transition mutation")
            else:
                print("Type of mutation: Transversion mutation")

elif len(Y) > len(M):
    mutation= True
    print("Mutation detected: Original DNA sequence is longer than the changed DNA sequence.")
    print("Type of mutation: Deletion")
    for i in range(len(M)):
        if Y[i] != M[i]:
            print("Deleted base:", Y[i],
                  "from position", i+1)
            break

elif len(Y) < len(M):
    mutation= True
    print("Mutation detected: Original DNA sequence is shorter than the changed DNA sequence.")
    print("Type of mutation: Insertion")
    for i in range(len(M)):
        if Y[i] != M[i]:
            print("Inserted base:", M[i],
                  "at position", i+1)
            break

if mutation == False:
        print("No mutation detected") 