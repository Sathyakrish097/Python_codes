

def  zip_values(names, scores, grades): 
    for n, s,g in zip(names, scores, grades):
        print(f"{n}-{s}-{g}")
    print("---------------------------------------------------------") 
    for i in range(len(names)):
        print(f"{names[i]}-{scores[i]}-{grades[i]}")
    
    print("Only condition is all the list should be in same length.")
    print("=========================================================")

def enumerator(names):
    for i, name in enumerate(names, start=1):
        print(f"{i}-{name}")
    print("---------------------------------------------------------")
    for i in range(len(names)):
        print(f"{i+1}-{names[i]}")
    
    
def main():
    names=['Vijay','Ajith','Suriya','Jeeva']
    scores= [98, 95, 90, 80]
    grades= ['A+' , 'A+', 'A', 'B']
    
    zip_values(names, scores, grades)
    enumerator(names)

if __name__=="__main__":
    main()