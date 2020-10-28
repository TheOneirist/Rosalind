# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def nucleotideCounter():

    a = 0
    c = 0
    g = 0
    t = 0
    dnaString = input("Enter DNA string: ")

    for nucleotide in dnaString:
        if nucleotide == "A":
            a += 1
        elif nucleotide == "C":
            c += 1
        elif nucleotide == "G":
            g += 1
        elif nucleotide == "T":
            t += 1

    print("{} {} {} {}".format(a, c, g, t))

nucleotideCounter()