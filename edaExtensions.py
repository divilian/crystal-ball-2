
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.DataFrame({
    'name':['Jane Eyre','The Brothers Karamazov','Anna Karenina',
        'The Inferno','Huck Finn'],
    'lang':['English','Russian','Russian','Italian','English'],
    'year':[1847,1879,1877,1320,1884],
    'gender':['F','M','M','M','M'],
    'words':[183858,364153,349736,45750,109571],
    'chaps':[38,92,219,34,43]
}).set_index('name')

NUM_MORE = 1000
more_genders = np.random.choice(['M','F'],p=[.8,.2],size=NUM_MORE)
more_langs = np.where(more_genders=='M',
    np.random.choice(['English','French','Russian','Italian','Spanish'],
            p=[.25,.25,.15,.1,.25],size=NUM_MORE),
    np.random.choice(['English','French','Russian','Italian','Spanish'],
            p=[.3,.4,.05,.1,.15],size=NUM_MORE))
more_years = np.where(more_genders=='M',
    np.round(np.random.uniform(1600,2000,NUM_MORE)),
    np.round(np.random.uniform(1800,2000,NUM_MORE)))
more_words = np.where(more_langs=="Russian",
    800000 - (more_years-1600) * 200 + np.random.normal(0,200000,NUM_MORE),
    1000000 - (more_years-1600) * 2000 + np.random.normal(0,90000,NUM_MORE))
more_words = more_words.clip(20000,np.Inf)
more_chaps = more_words / 10000 + np.random.normal(0,30,NUM_MORE)
more_chaps = more_chaps.clip(0,np.Inf)

books = pd.DataFrame({
    'name':np.concatenate([books.index,['NA']*NUM_MORE]),
    'gender':np.concatenate([books.gender,more_genders]),
    'year':np.concatenate([books.year,more_years]).astype(int),
    'lang':np.concatenate([books.lang,more_langs]),
    'words':np.concatenate([books.words,more_words]).astype(int),
    'chaps':np.concatenate([books.chaps,more_chaps]).astype(int)
}).set_index('name')[['gender','year','lang','words','chaps']]

print(books.lang.value_counts())

#plt.figure()
#books.lang.value_counts().plot.bar()
#plt.savefig('barplot.png')
#
#print(books.words.mean())
#print(books.words.std())
#print(books.words.quantile([0,.25,.5,.75,1]))
#
#plt.figure()
#books.words.plot.hist(bins=30)
#plt.savefig('histogram.png')
#
#print(books.groupby('gender')['lang'].value_counts())
#
#gender_lang_m = pd.crosstab(books['lang'], columns=books['gender'], margins=True)
#print(gender_lang_m / gender_lang_m.loc['All']['All'] * 100)
#print(np.round(gender_lang_m / gender_lang_m.loc['All'] * 100,2))
#print(np.round(gender_lang_m.div(gender_lang_m['All'],axis=0) * 100,2))
#
#gender_lang = pd.crosstab(books['gender'], books['lang'], margins=False)
#plt.figure()
#sns.heatmap(gender_lang)
#plt.savefig('heatmap.png')
#
#plt.figure()
#books.boxplot(column='words',by='lang')
#plt.savefig('boxplot.png')
#
#plt.figure()
#books.boxplot(column='words',by='lang',notch=True)
#plt.savefig('notchedboxplot.png')
#
#plt.figure()
#books.plot.scatter(x='year',y='words',xlim=(1600,2018))
#plt.savefig('scatterplot.png')

books = books[books.year > 1500]

# Need to use "tight layout," but I couldn't make it stick without doing it
# manually in the interactive image GUI.
#plt.figure()
#plt.tight_layout()
#pd.plotting.scatter_matrix(books[['year','words','chaps']], alpha=1,
#    figsize=(5,5))
#plt.savefig('scatterplotmatrix.png')

#plt.figure()
#plot_kws={"s":30}
#facet = sns.FacetGrid(books, col='lang')
#facet.map(plt.scatter, 'year', 'words', marker=".")
#plt.savefig('scatterplotfacets.png')

#plt.figure()
#plot_kws={"s":30}
#facet = sns.FacetGrid(books, row='gender', col='lang')
#facet.map(plt.scatter, 'year', 'words', marker=".")
#plt.savefig('scatterplotfacets2d.png')

#plt.figure()
#sns.set(rc={'figure.figsize':(11,11)})
#sns.pairplot(data=books,x_vars=["year"],y_vars=["words"],hue="lang",
#    plot_kws={"s":16})
#plt.savefig('groupedscatter.png')
#plt.show()
