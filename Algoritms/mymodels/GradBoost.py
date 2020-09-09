from sklearn.tree import DecisionTreeRegressor
import numpy as np


class GradBoost:

    def __init__(self, n_trees=10, max_depth=5, eta=0.1):
        self.eta = eta
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.coefs = [1] * self.n_trees
        self.trees = None
        self.train_errors = None
        self.test_errors = None

    def fit(self, X_train, X_test, y_train, y_test):

        # Деревья будем записывать в список
        self.trees = []

        # Будем записывать ошибки на обучающей и тестовой выборке на каждой итерации в список
        self.train_errors = []
        self.test_errors = []

        for i in range(self.n_trees):
            tree = DecisionTreeRegressor(max_depth=self.max_depth, random_state=42)

            # инициализируем бустинг начальным алгоритмом, возвращающим ноль,
            # поэтому первый алгоритм просто обучаем на выборке и добавляем в список
            if len(self.trees) == 0:
                # обучаем первое дерево на обучающей выборке
                tree.fit(X_train, y_train)

                self.train_errors.append(self.mean_squared_error(y_train, self.predict(X_train)))
                self.test_errors.append(self.mean_squared_error(y_test, self.predict(X_test)))
            else:
                # Получим ответы на текущей композиции
                target = self.predict(X_train)

                # алгоритмы начиная со второго обучаем на сдвиг
                tree.fit(X_train, self.bias(y_train, target))

                self.train_errors.append(self.mean_squared_error(y_train, self.predict(X_train)))
                self.test_errors.append(self.mean_squared_error(y_test, self.predict(X_test)))

            self.trees.append(tree)

        if self.trees and self.train_errors and self.test_errors:
            return 0
        else:
            return -1

    @staticmethod
    def mean_squared_error(y_real, prediction):
        return (sum((y_real - prediction) ** 2)) / len(y_real)

    @staticmethod
    def bias(y, z):
        return y - z

    def predict(self, X):
        # Реализуемый алгоритм градиентного бустинга будет инициализироваться нулевыми значениями,
        # поэтому все деревья из списка trees_list уже являются дополнительными и при предсказании
        # прибавляются с шагом eta
        return np.array(
            [sum([self.eta * coef * alg.predict([x])[0] for alg, coef in zip(self.trees, self.coefs)]) for x in X])
