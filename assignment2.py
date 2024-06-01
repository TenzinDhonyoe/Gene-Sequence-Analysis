# Reading the FASTA file and storing the sequences
with open('sequences.fasta', 'r') as file:
    lines = file.readlines()
aa = {'GGG' : 'G', 'GGA' : 'G', 'GGC' : 'G', 'GGT' : 'G', 
      'AGG' : 'R', 'AGA' : 'R', 'AGC' : 'S', 'AGT' : 'S', 
      'CGG' : 'R', 'CGA' : 'R', 'CGC' : 'R', 'CGT' : 'R', 
      'TGG' : 'W', 'TGA' : 'X', 'TGC' : 'C', 'TGT' : 'C',
      
      'GAG' : 'E', 'GAA' : 'E', 'GAC' : 'D', 'GAT' : 'D',
      'AAG' : 'K', 'AAA' : 'K', 'AAC' : 'N', 'AAT' : 'N', 
      'CAG' : 'Q', 'CAA' : 'Q', 'CAC' : 'H', 'CAT' : 'H', 
      'TAG' : 'X', 'TAA' : 'X', 'TAC' : 'Y', 'TAT' : 'Y', 
      
      'GCG' : 'A', 'GCA' : 'A', 'GCC' : 'A', 'GCT' : 'A',
      'ACG' : 'T', 'ACA' : 'T', 'ACC' : 'T', 'ACT' : 'T', 
      'CCG' : 'P', 'CCA' : 'P', 'CCC' : 'P', 'CCT' : 'P', 
      'TCG' : 'S', 'TCA' : 'S', 'TCC' : 'S', 'TCT' : 'S', 
      
      'GTG' : 'V', 'GTA' : 'V', 'GTC' : 'V', 'GTT' : 'V',
      'ATG' : 'M', 'ATA' : 'I', 'ATC' : 'I', 'ATT' : 'I', 
      'CTG' : 'L', 'CTA' : 'L', 'CTC' : 'L', 'CTT' : 'L', 
      'TTG' : 'L', 'TTA' : 'L', 'TTC' : 'F', 'TTT' : 'F', 
    }  # Amino Acids Dictionary
NCArr = []  # NC titles
ORArr = []  # OR titles
NCSeqArr = []  # NC sequences
ORSeqArr = []  # OR sequences
nucleotides = ['A', 'T', 'G', 'C']
current_seq = ''
current_title = ''

for line in lines:
    # If line is a title
    if line.startswith('>'):
        # If there's a current sequence, save it based on the last title
        if current_seq:
            if current_title.startswith('NC') or current_title.startswith('join(NC'):
                NCSeqArr.append(current_seq)
            elif current_title.startswith('OR') or current_title.startswith('join(OR'):
                ORSeqArr.append(current_seq)
            current_seq = ''
        
        current_title = line[1:].strip()  # Remove the leading '>'
        if current_title.startswith('NC') or current_title.startswith('join(NC'):
            title = current_title.split('|', 1)[1]
            title = title.split('[', 1)[0].strip()
            NCArr.append(title)
        elif current_title.startswith('OR') or current_title.startswith('join(OR'):
            title = current_title.split('|', 1)[1]
            title = title.split('[', 1)[0].strip()
            ORArr.append(title)
            
    # If line is a sequence
    else:
        for char in line:
            if char.upper() in nucleotides:
                current_seq += char

# To handle the last sequence in the file
if current_seq:
    if current_title.startswith('NC') or current_title.startswith('join(NC'):
        NCSeqArr.append(current_seq)
    elif current_title.startswith('OR') or current_title.startswith('join(OR'):
        ORSeqArr.append(current_seq)

# Comparing NC and OR sequences and finding differences
def mutation(codon1, codon2):
    a1 = aa.get(codon1)
    a2 = aa.get(codon2)
    
    if a1 == a2:
        # Silent
        return 'S'
    elif len(a1) != len(a2):
        # Nonsense
        return 'N'
    else:
        # Missense
        return 'M'
    
# Helper function to get differences between two sequences
def get_differences(seq1, seq2):
    diff = []
    diff_count = 0
    for i in range(0, min(len(seq1), len(seq2)), 3):  # Step of 3 for codons
        codon1 = seq1[i:i+3]
        codon2 = seq2[i:i+3]
        
        if codon1 != codon2:
            status = mutation(codon1, codon2)
            for j in range(3):
                if i+j < min(len(seq1), len(seq2)) and seq1[i+j] != seq2[i+j]:  # Ensure within bounds
                    diff.append(f'{seq1[i+j]}{i+j}{seq2[i+j]}_{status}')
                    diff_count += 1
    return diff, diff_count

# List to store results
results = []

for i, OR_title in enumerate(ORArr):
    OR_seq = ORSeqArr[i]
    # Find corresponding NC sequence
    NC_seq = None
    for j, NC_title in enumerate(NCArr):
        if OR_title in NC_title:
            NC_seq = NCSeqArr[j]
            break

    if NC_seq:
        diff, diff_count = get_differences(NC_seq, OR_seq)
        results.append({
            "Gene": OR_title,
            "NC length": len(NC_seq),
            "OR length": len(OR_seq),
            "Differences": diff,
            "Diff count": diff_count
        })

# Formatting the output
formatted_output = []
header = ["Gene", "NC length", "OR length", "Differences", "Diff count"]
formatted_output.append(header)

for result in results:
    row = [
        result["Gene"],
        result["NC length"],
        result["OR length"],
        result["Differences"] if len(result["Differences"]) <= 4 else result["Differences"][:4],
        result["Diff count"]
    ]
    formatted_output.append(row)

formatted_output = sorted(formatted_output)

# Printing the headers
for i in range(0, len(formatted_output[0])):
    if i == 3:
        print(f"{formatted_output[0][i]:<40}", end='\t')
    else:
        print(f"{formatted_output[0][i]:<25}", end='\t')
print('\n')  # New line after headers

# Printing the data for each gene
for i in range(1, len(formatted_output)):
    for j in range(0, len(formatted_output[i])):
        if j == 3:
            print(f"{str(formatted_output[i][j]):<40}", end='\t')
        else:
            print(f"{str(formatted_output[i][j]):<25}", end='\t')
    print('\n')  # New line after each gene's data