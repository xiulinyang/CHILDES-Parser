# CHILDES-Parser
Training of a Dependency Parser on golden UD annotation on English CHILDES 

## STANZA 

1. Test the accuracy of a Stanza model trained on gold UD_English-CHILDES annotations taken from the dev branch of [Xiulin's paper repository](https://github.com/UniversalDependencies/UD_English-CHILDES), which I added as well in this repo.

### Instruction for the training of Stanza model [documentation](https://stanfordnlp.github.io/stanza/training_and_evaluation.html)

- First create a folder called **data**, under which you create other two subfolders [depparse, pos]. Whithin these two subfolders you copy paste the conllu files and you rename them like this:
    - en_childes.train.in.conllu
    - en_childes.dev.in.conllu
    - en_childes.test.in.conllu

To train the tokenizer you run this command:
`python -m stanza.utils.training.run_tokenize UD_English-EWT`

To train the parser you run this command:
`python -m stanza.utils.training.run_depparse UD_English-EWT`

Create also the output folder for your trained models **save_models**.

In order to load the trained model and evaluate it, I use this:

```
stanza_childes_en = stanza.Pipeline(
        lang='en',
        processors='tokenize,pos,depparse',
        use_gpu=True,
        pos_model_path='./saved_models/pos/en_childes_charlm_tagger.pt',
        depparse_model_path='./saved_models/depparse/en_childes_charlm_parser.pt')
```


2. Test the accuracy of Stanza Dependency Parser off the shelf trained on combined UD. 

`stanza_en = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', use_gpu=True)`


## SUPAR 

3. Test a Supar model trained on Combined English Dataset

4. Test a Supar model trained on first Combined English + CHILDES(silver) + CHILDES(gold)

5. Test a Supar model trained on CHILDES (gold)





