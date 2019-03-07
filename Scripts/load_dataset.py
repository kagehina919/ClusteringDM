def load_dataset():
    """
    Function to load the dataset from given file and return
    the data as a list of tuples
    """
    with open('data/human_gene.txt') as f:
        rows = f.readlines()

    to_append = []
    for _ in rows:
        if _[0] == '>':
            _ = _ + str(':')
        to_append.append(_)

    processed = ''.join(to_append)
    rows = processed.split('>')

    sequences = []
    for _ in rows[1:]:
        name, seq = _.split(':')
        name = name.replace('\n', '')
        seq = seq.replace('\n', '')
        sequences.append((name, seq))

    return sequences