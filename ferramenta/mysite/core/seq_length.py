def seq_len(qual_seq):
    #converte()
    fasta = []
    seq = []
    with open('/home/livanski/Music/seq_maior/servidor_apresentacao/ferramenta/resultado_cuda_sankoff.txt') as file:
        for line in file:
            fasta.append(line)

    for x in fasta:
        item = x
        for y in ['\n', '\t', '/', 'seq', ':', '[', ']', ' ']:
            item = item.replace(y, "")

        seq.append(item)

    if qual_seq == 1:
        exibe = seq[1]
    elif qual_seq == 2:
        exibe = seq[3]

    return len(exibe)
#print(seq_len(1))

def confere():
    fasta = []
    seq = []
    with open('/home/livanski/Music/seq_maior/cuda_sankoff/seqs/008.fasta') as file:
        for line in file:
            fasta.append(line)

    for x in fasta:
        item = x
        for y in ['\n', '\t', '/', 'seq', ':', '[', ']', ' ']:
            item = item.replace(y, "")

        seq.append(item)

        