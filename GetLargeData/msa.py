from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
#Read in unfiltered data
unfiltered = SeqIO.parse("SARS-CoV-2.gbk", "genbank")
#Drop data without (close to) full length sequences
full_length_records = []
for record in unfiltered:
    if len(record.seq) > 29000:
        full_length_records.append(record)
#Write filtered data to file
SeqIO.write(full_length_records, "SARS-CoV-2.fasta", "fasta")
#Align sequences with MUSCLE (using parameters to make the alignment
#process as fast as possible)
muscle_cline = MuscleCommandline(input="SARS-CoV-2.fasta", 
                                 out="SARS-CoV-2_aligned.fasta", 
                                 diags = True, 
                                 maxiters = 1, 
                                 log="../../data/raw/align_log.txt")
muscle_cline()