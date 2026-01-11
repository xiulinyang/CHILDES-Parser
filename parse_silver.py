import stanza
from glob import glob
from pathlib import Path
from tqdm import tqdm
import os
os.makedirs('silver', exist_ok=True)
nlp = stanza.Pipeline(
    lang="en",
    processors="tokenize,pos,lemma,depparse",
    tokenize_pretokenized=False,
    model_path="fpadovani/cds_parser_roberta_stanza",
    use_gpu=True,
    pos_batch_size=50000,
    lemma_batch_size=10000,
    depparse_batch_size=50000,
)

def process_in_batches(sentences, batch_size=2000):
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i+batch_size]
        doc = nlp('\n'.join(batch))
        yield doc

file_paths = glob('silver/*.txt')

for f in tqdm(file_paths):
    file_name = f.split('/')[-1].split('.')[0]
    with open(f'silver/{file_name}_parsed.txt', 'w', encoding='utf-8') as out_f:
        sents = [x for x in Path(f).read_text(encoding='utf-8').strip().split('\n')]
        out_f.write('\n'.join(sents))
        for doc in tqdm(process_in_batches(sents, batch_size=2000), total=(len(sents)//2000)+1):
            for sent in doc.sentences:
                out_f.write('# text = ' + sent.text + '\n')
                for word in sent.words:
                    out_f.write(f'{word.id}\t{word.text}\t{word.lemma}\t{word.upos}\t_\t_\t{word.head}\t{word.deprel}\t_\t_\n')
                out_f.write('\n')
