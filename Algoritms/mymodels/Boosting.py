import numpy as np
import random

from sklearn.tree import DecisionTreeClassifier


random.seed(42)


class Boosting():
    def __init__(self, n_trees, min_samples_leaf=5, max_depth=6, num_leaves=64, criteria='gini'):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.num_leaves = num_leaves
        self.min_samples_leaf = min_samples_leaf
        self.criteria = criteria
        self.trees = []

    def fit(self, X, y):
        n_objects = len(X)
        self.n_classes = len(np.unique((y)))

        # Начальные веса моделей
        w = np.ones(n_objects) / n_objects

        # Деревья с весами будем записывать в список
        for n in range(self.n_trees):
            # Зададим дерево и обучим его
            tree = DecisionTreeClassifier(max_depth=self.max_depth,
                                          min_samples_leaf=self.min_samples_leaf,
                                          max_leaf_nodes=self.num_leaves,
                                          criterion=self.criteria)
            tree.fit(X, y, sample_weight=w)

            predictions = tree.predict(X)

            e = self.get_error(predictions, y)
            # отбросим дерево, если его ошибка больше 0.5
            # Запишем условие в общем виде (применимо к небинарным классификаторам)
            if e >= 1 - 1 / self.n_classes:
                break

            # Вычислим вес для дерева
            alpha = 0.5 * np.log((1 - e) / e)

            # Найдем индексы правильно классифицированных элементов
            match = predictions == y

            # Увеличим веса для неправильно классифицированных элементов
            w[~match] *= np.exp(alpha)

            # Нормализуем веса
            w /= w.sum()

            # Добавим дерево с весом в список
            self.trees.append((alpha, tree))

    def predict(self, X):
        # вначале обозначим предсказание нулевым массивом
        n_objects = X.shape[0]
        pred = np.zeros((n_objects, self.n_classes))

        for alpha, tree in self.trees:
            prediction = tree.predict(X)
            # Для каждого предсказания будем прибавлять alpha к
            # элементу с индексом предсказанного класса
            pred[range(n_objects), prediction] += alpha

            # выберем индексы с максимальными суммарными весами -
        # получим предсказанные алгоритмом классы
        # y_pred = np.argmax(pred, axis=1)
        y_pred = 1 / (1 + np.exp(-pred))

        return y_pred[:, 1]

    def get_error(self, y_pred, y):
        return sum(y_pred != y) / len(y)
