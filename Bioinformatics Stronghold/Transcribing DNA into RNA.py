# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

def transcribeDNAtoRNA():

    dnaString = input("Please input DNA string: ")
    rnaString = ""

    for nucleotide in dnaString:
        if nucleotide == "T":
            rnaString += "U"
        else:
            rnaString += nucleotide

    print(rnaString)

transcribeDNAtoRNA()