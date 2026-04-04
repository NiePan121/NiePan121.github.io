seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop_codons = ['UAA', 'UAG', 'UGA']
start_codon='AUG'
orfs=[]
for i in range(len(seq)-2):
    current=seq[i:i+3]
    if current==start_codon:
        for j in range(i+3,len(seq)-2,3):
            codon=seq[j:j+3]
            if codon in stop_codons:
                orf_sequence=seq[i:j+3]
                orfs.append(orf_sequence)
                break
if len(orfs)==0:
    print("ORF NOT FOUND")
else:
    longest=max(orfs,key=len)
    print("The Longest ORF:",longest)
    print("length:",len(longest))