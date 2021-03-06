import sys

import csv
import matplotlib.pyplot as plt

sys.path.append('..')  
import geneview as gv

xtick = ['chr'+c for c in map(str, range(1, 15) + ['16', '18', '20', '22'])]
df = gv.util.load_dataset('GOYA_preview')
gv.gwas.manhattanplot(df[['chrID','position','pvalue']], 
                      hline_kws={'y': 3, 'color': 'b', 'lw': 1},
                      xlabel="Chromosome", 
                      ylabel="-Log10(P-value)",
                      xticklabel_kws={'rotation': 'vertical'},
                      xtick_label_set = set(xtick))
plt.savefig('manhattan.png')
plt.show()
