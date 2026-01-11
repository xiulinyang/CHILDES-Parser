from glob import glob
from pathlib import Path
silvers = glob('silver/*.conll')
child_train = Path('UD_English-CHILDES/en_childes-ud-train.conllu').read_text().strip()

with open('en_childes-ud-train.conllu', 'w', encoding='utf-8') as out_f:
    out_f.write(child_train)
    out_f.write('\n')
    for f in silvers:
        content = Path(f).read_text().strip()
        out_f.write(content)
        out_f.write('\n')