import matplotlib.pyplot as plt
gene_dict = {
    "TP53": 12.4,
    "BRCA1": 8.2,
    "EGFR": 15.1,
    "PTEN": 5.3,
    "ESR1": 10.7}
gene_dict["MYC"] = 11.6
print(gene_dict)
target_gene =input("Type in your gene of interest:")
if target_gene in gene_dict:
   print(f"\n the expression of {target_gene}：{gene_dict[target_gene]}")
else:
    print(f"\n{target_gene}is not found, error")
mean=sum(gene_dict.values())/len(gene_dict)
print("The mean is",mean)
genes=list(gene_dict.keys())
values=list(gene_dict.values())
plt.bar(genes,values,color="skyblue")
plt.xlabel("Genes")
plt.ylabel("Expression Vable")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()