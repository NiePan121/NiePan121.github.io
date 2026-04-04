import re
from collections import Counter
import matplotlib.pyplot as plt

def read_fasta(filename):
    sequences = {}
    current_name = ""
    current_seq = ""
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_name:
                    sequences[current_name] = current_seq
                parts = line.split()
                current_name = parts[0][1:]
                current_seq = ""
            else:
                current_seq += line.upper()
        if current_name:
            sequences[current_name] = current_seq
    return sequences

def find_longest_orf_for_stop(seq, stop_codon):
    start_codon = "ATG"
    max_length = 0
    best_orf = ""
    for match in re.finditer(start_codon, seq):
        start_pos = match.start()
        for i in range(start_pos, len(seq), 3):
            current_codon = seq[i:i+3]
            if current_codon == stop_codon:
                orf = seq[start_pos:i+3]
                if len(orf) > max_length:
                    max_length = len(orf)
                    best_orf = orf
                break
            if len(current_codon) < 3:
                break
    return best_orf

def split_into_codons(orf):
    if len(orf) < 3:
        return []
    coding_region = orf[:-3]
    return [coding_region[i:i+3] for i in range(0, len(coding_region), 3) if len(coding_region[i:i+3]) == 3]

if __name__ == "__main__":
    stop_input = input("Enter one stop codon (TAA/TAG/TGA): ").strip().upper()
    if stop_input not in ["TAA", "TAG", "TGA"]:
        print("Error: Please enter only TAA, TAG, or TGA.")
        exit()

    # 👇 这里改成你FASTA文件的完整绝对路径，Windows必须加r
    fasta_path = r"c:\Users\lyu5\Desktop\NiePan121.github.io\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    gene_sequences = read_fasta(fasta_path)
    all_coding_codons = []

    for gene_id, dna_seq in gene_sequences.items():
        longest_orf = find_longest_orf_for_stop(dna_seq, stop_input)
        if longest_orf:
            codons = split_into_codons(longest_orf)
            all_coding_codons.extend(codons)

    codon_counts = Counter(all_coding_codons)
    print("\nCodon frequencies upstream of the selected stop codon:")
    for codon, count in codon_counts.most_common():
        print(f"{codon}: {count}")

    codon_labels = list(codon_counts.keys())
    count_values = list(codon_counts.values())

    plt.figure(figsize=(10, 7))
    plt.pie(count_values, labels=codon_labels, autopct='%1.1f%%', textprops={'fontsize': 7})
    plt.title(f"Codon Distribution for Stop Codon: {stop_input}")
    plt.savefig(f"codon_pie_{stop_input}.png", dpi=300, bbox_inches="tight")
    print(f"\nPie chart saved as: codon_pie_{stop_input}.png")
    plt.show()