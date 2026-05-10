#amino acid mass dictionary
aa_mass={
    'G':57.02,
    'A':71.04,
    'S':87.03,
    'P':97.05,
    'V':99.07,
    'T':101.05,
    'C':103.01,
    'I':113.08,
    'L':113.08,
    'N':114.04,
    'D':115.03,
    'Q':128.06,
    'K':128.09,
    'E':129.04,
    'M':131.04,
    'H':137.06,
    'F':147.07,
    'R':156.10,
    'Y':163.06,
    'W':186.08
    }
#define the fuction
def calculate_protein_mass(aa_sequence):
    total_mass=0.0
    for aa in aa_sequence:
        if aa not in aa_mass:
           print(f"Error. {aa} is an unknown amino acid. The mass cannot be calculated.")
           return None
        total_mass+=aa_mass[aa]
    print(f"The total mass of sequence {aa_sequence} is: {total_mass} amu")
    return total_mass
#example
if __name__ == "__main__":
    print("\n---Example---")
    print("Please enter your own sequence:GAV")
    test_sequence="GAV"
    calculate_protein_mass(test_sequence)
#user input
    while True:
        user_input=input("\nPlease enter your own sequence:")
        result=calculate_protein_mass(user_input)
        if result is not None:
            break