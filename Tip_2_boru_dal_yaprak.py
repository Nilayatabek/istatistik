import pandas as pd
import stemgraphic



data_2 = [192, 225, 251, 203, 173, 207, 176, 216, 259, 219,
151, 201, 191, 259 ,205, 198 ,223, 215, 185, 193,
212, 241, 219, 203, 153, 227, 214 ,155 ,218 ,194,
213, 201, 182 ,231 ,206 ,192, 206, 258 ,208, 186,
221, 213 ,257 ,204 ,184 ,161 ,209 ,219 ,157 ,197]


y2 = pd.Series(data_2)

fig2, ax = stemgraphic.stem_graphic(y2)


fig2.show()
