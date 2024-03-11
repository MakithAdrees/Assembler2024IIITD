# Assembler2024IIITD
Members : Arhan, Arnesh, Arush, Dev

Explanation for Assembler Code:
There are two Python files: One file includes the data for all the instructions, the Other one includes the function to import the data and export the output and a function to convert the given instruction from assembly to binary.
The first file, named **assembler.py**, imports the data from the txt file, and then a function is executed that checks the string in each line for errors. If there is an error, it prints the error and line number in the terminal, or if there is no error, it simply executes the following function, which is imported from another Python file named **instructions.py**, which checks which instruction is being called and then executes that function.
It also checks whether there is a label in the given line or not and then after checking that if any register is not in the register list, it prints an error. Otherwise, it stores the binary value of the instruction, and once all lines are finished, it exports the binary data to a Txt file(if there are no errors)
also, if the inst(virtual halt)[**beq zero,zero,0**] is not present at the last of the given instructions, it prints the error that virtual halt is not present.
