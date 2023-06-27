import pandas as pd
import stemgraphic



x= [182, 193,184,201,212,209,213,199,207,234,202,219,225,228,209,187,203,228,205,236,225,194,214,209,218,219,213,198,229,198,202,219,227,201,219,227,201,219,188,203,188,205,238,223,209,194,216,195,208,189,204,197,208]

#Tip 2 için çalışan kod Tip 1'in grafiğini bir türlü çıkarmadı, bozuk bir görüntü veriyor. 

y = pd.Series(x)

fig, ax = stemgraphic.stem_graphic(y)

fig.show()
