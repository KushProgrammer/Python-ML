import periodictable as pt
import random as rd

compare = lambda x, y: x == y
printresult = lambda state: "Correct" if state else "Incorrect"


def main():
    restart = True
    while restart:
        randomNum = rd.randint(1, 118)
        #Gets Starting Decision
        try:
            decision = int(input("Enter 0 for getting name or 1 for getting atomic number of the element:  "))
        except ValueError:
            print("Invalid value detected!!")
            break

        #Runs the user input function
        if (decision == 0):
            by_names(randomNum)
        elif (decision == 1):
            by_numbers(randomNum)
        else:
            print("Invalid value detected!! Please restart the program")

        #Asks for the restart
        resume = input("Enter any key to close the program or 0 to restart:  ")
        try:
            if(int(resume) == 0):
                continue
        except ValueError:
            restart = False



# by_numbers -> displays number
# by_name -> displays name

def by_names(num: int):
    """
        Guess the atomic number, symbol and mass of the element with the element's name given
    """
    element = pt.elements[num]
    print(f"The element is: {element.name.capitalize()}")

    #User Inputs
    number = int(input("Enter the atomic number: "))
    sym = input("Enter the symbol:  ")
    mass = float(input("Enter the mass: "))

    name_guess = compare(number, num)
    sym_guess = compare(sym, element.symbol)
    mass_guess = compare(mass, round(element.mass, 0))
    
    print(f"""
        Name: {element.name.capitalize()}
        
        Atomic Number: {num} Guess: {printresult(name_guess)}
        Symbol: {element.symbol} Guess: {printresult(sym_guess)}
        Mass: {round(element.mass, 0)} Guess: {printresult(mass_guess)}
    """)

def by_numbers(num: int):
    """
        Guess the name, symbol and mass of the element with the atomic number given
    """
    element = pt.elements[num] # get the element of atomic number 'num'
    print(f"The atomic number is: {num}")
    name = input("Enter the name:  ").lower()
    sym = input("Enter the symbol:  ")
    mass = float(input("Enter the mass(amu):"))
    name_guess = compare(name, element.name) # Compare : return true if both are same else return false
    sym_guess = compare(sym, element.symbol)
    mass_guess = compare(mass, round(element.mass, 0))
    print(f"""
        Atomic Number: {num}
        
        Name: {element.name.capitalize()} Guess: {printresult(name_guess)}
        Symbol: {element.symbol} Guess: {printresult(sym_guess)}
        Mass: {round(element.mass, 0)} Guess: {printresult(mass_guess)}
    """)


main()





