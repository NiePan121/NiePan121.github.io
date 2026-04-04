import os
from Bio import SeqIO
script_folder = os.path.dirname(os.path.abspath(__file__))
input_file  = os.path.join(script_folder, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output_file = os.path.join(script_folder, "stop_genes.fa")
start_codon="ATG"
stop_codons=["TAA","TAG","TGA"]
def has_valid_orf(sequence):
    if not sequence.startswith(start_codon):
        return False, None
    for i in range(3,len(sequence)-2,3):
        codon=sequence[i:i+3]
        if codon in stop_codons:
            return True, codon
    return False, None
def get_gene_name(header):
    parts=header.split()
    for part in parts:
        if part.startswith("gene:"):
            return part.split(":")[1]
    return header.split()[0]
with open(output_file,"w") as out:
    for record in SeqIO.parse(input_file,"fasta"):
        seq=str(record.seq).strip()
        valid,stop_type=has_valid_orf(seq)
        if valid:
            gene_name=get_gene_name(record.description)
            out.write(f">{gene_name}{stop_type}\n")
            out.write(seq+"\n")
print("Done!Saved to stop_genes.fa")
