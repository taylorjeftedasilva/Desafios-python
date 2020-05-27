def DNA_strand(dna):
    d={'A':'T','T':'A','C':'G','G':'C'}
    b=''
    for i in dna:
        b=b+(d[i.upper()])
    return(b)
