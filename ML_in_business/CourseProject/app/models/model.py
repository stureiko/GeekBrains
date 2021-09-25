# imports
import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# Специальные библиотеки
from sklearn import ensemble
from sklearn.model_selection import train_test_split, cross_val_score, \
    GridSearchCV, RandomizedSearchCV

# Метрики
from sklearn.metrics import precision_score, \
    accuracy_score, \
    f1_score, \
    roc_auc_score, \
    roc_curve, \
    auc, \
    confusion_matrix, \
    mean_squared_error, \
    r2_score

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        return x[self.column]


def main():
    path = '../../dataset/'
    wine_150k = pd.read_csv(path + 'winemag-data_first150k.csv', index_col=0)
    wine_130k = pd.read_csv(path + 'winemag-data-130k-v2.csv', index_col=0)
    wine = pd.concat([wine_150k, wine_130k], axis=0)
    print('Dataset loaded')

    # feature engineering
    features = ['country', 'description', 'designation', 'points', 'price', 'province', 'region_1',
                'variety', 'winery']

    wine = wine[features]

    cnt_idx = wine['country'].value_counts().to_frame()[:12].index
    wine = wine.loc[wine['country'].isin(list(cnt_idx))]

    wine = pd.concat([wine.drop('country', axis=1),
                      pd.get_dummies(wine['country'], prefix='country')], axis=1)

    pr_idx = wine['province'].value_counts().to_frame()[:50].index
    wine = wine.loc[wine['province'].isin(list(pr_idx))]

    wine = pd.concat([wine.drop('province', axis=1),
                      pd.get_dummies(wine['province'], prefix='province')], axis=1)

    print('Feature engineering complete')
    # model
    # Можно сделать 100 000, но на обучение уходит примерно 1 час
    wine_short = wine.head(10000)
    X_train, X_test, y_train, y_test = train_test_split(wine_short.drop('points', axis=1),
                                                        wine_short['points'], test_size=0.33, random_state=42)

    classifier = Pipeline([('description_text_selector', FeatureSelector(column='description')),
                           ('description_text_tfidf', TfidfVectorizer(sublinear_tf=True,
                                                                      strip_accents='unicode',
                                                                      analyzer='word',
                                                                      token_pattern=r'\w{1,}',
                                                                      stop_words='english',
                                                                      ngram_range=(1, 1),
                                                                      max_features=10000)),
                           ('rfor_clf', ensemble.RandomForestRegressor())])

    print('Start fit')
    classifier.fit(X_train, y_train)

    print('Start prediction')
    y_score = classifier.predict(X_test)
    print(y_score)


if __name__ == '__main__':
    main()
