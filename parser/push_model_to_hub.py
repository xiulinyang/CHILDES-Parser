import stanza
import spacy
from conllu import parse_incr
from collections import defaultdict
from pathlib import Path
from tqdm import tqdm
import re

nlp_childes = stanza.Pipeline(
        lang='en',
        processors='tokenize,pos,lemma,depparse',
        use_gpu=True,
        depparse_model_path='fpadovani/childes_stanza_parser'
    )

print(nlp_childes)