# Article-Omission
Scripts and data employed for the paper "Explaining cross-linguistic differences in article omission through an acquisition model". This directory contains:

1. **moth\_ITA.txt** and **moth\_ENG.txt**: The mother speech in the files in the Calambrone corpus (Cipriani et al. 1989) and in the Providence corpus (Demuth and McCollough 2009). The sentences have been tagged using TreeTagger (Schmid 1994).

2. **prec\_word.py**: this is a simple Python script that has the syntax ```prec_word.py file word```. It takes a file that contains tagged text with the format of an output file of TreeTagger and returns its preceding element. The program has an inside filter than retrieves only words preceding nouns, and only if they are not tagged as adjective.

3. **tag-counter.py**: this is a simple Python script that has the syntax ```tag-counter.py input_file n```. It takes a file that contains tagged text with the format of an output file of TreeTagger and returns the most frequent nouns as determined by the parameter *n*. 

5. **Eng.txt** and **Ita.txt**: these two files contain articles and possessives count for the most 100 frequent nouns retrieved in the two files in 1. Notice that there is a third column that also contain the demonstratives count, even though it is not mentioned in the paper.

5. **Article\_Om.R**: this is the R source code for the graph presented in the paper.

