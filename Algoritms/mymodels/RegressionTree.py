import numpy as np
from DesisionTree import Node


class RegressionLeaf:

    INSTANCE = 0

    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.prediction = self.predict()
        RegressionLeaf.INSTANCE += 1

    def __del__(self):
        RegressionLeaf.INSTANCE -= 1

    def predict(self):
        prediction = np.mean(self.labels)
        return prediction


class RegressionTree:
    def __init__(self, max_leaf=100):
        self.max_leaf = max_leaf
        self.Node = None

    @staticmethod
    def variance(labels: np.array) -> float:
        return float(np.mean((labels - np.mean(labels)) ** 2))

    def quality(self, left_labels, right_labels, current_informations):

        # доля выбоки, ушедшая в левое поддерево
        p = float(left_labels.shape[0]) / (left_labels.shape[0] + right_labels.shape[0])

        return current_informations - p * self.variance(left_labels) - (1 - p) * self.variance(right_labels)

    @staticmethod
    def split(data, labels, index, t):

        left = np.where(data[:, index] <= t)
        right = np.where(data[:, index] > t)

        true_data = data[left]
        false_data = data[right]
        true_labels = labels[left]
        false_labels = labels[right]

        return true_data, false_data, true_labels, false_labels

    def find_best_split(self, data, labels):

        #  обозначим минимальное количество объектов в узле
        min_leaf = 5

        current_informations = self.variance(labels)

        best_quality = 0
        best_t = None
        best_index = None

        n_features = data.shape[1]

        for index in range(n_features):
            # будем проверять только уникальные значения признака, исключая повторения
            t_values = np.unique([row[index] for row in data])

            for t in t_values:
                true_data, false_data, true_labels, false_labels = self.split(data, labels, index, t)
                #  пропускаем разбиения, в которых в узле остается менее 5 объектов
                if len(true_data) < min_leaf or len(false_data) < min_leaf:
                    continue

                current_quality = self.quality(true_labels, false_labels, current_informations)

                #  выбираем порог, на котором получается максимальный прирост качества
                if current_quality > best_quality:
                    best_quality, best_t, best_index = current_quality, t, index

        return best_quality, best_t, best_index

    def build_tree(self, data, labels):

        quality, t, index = self.find_best_split(data, labels)

        #  Базовый случай - прекращаем рекурсию, когда нет прироста в качества
        if quality == 0:
            return RegressionLeaf(data, labels)

        # Если достигли ограничения по количеству листьев - прекращаем рекурсию
        if RegressionLeaf.INSTANCE >= self.max_leaf:
            return RegressionLeaf(data, labels)

        true_data, false_data, true_labels, false_labels = self.split(data, labels, index, t)

        # Рекурсивно строим два поддерева
        true_branch = self.build_tree(true_data, true_labels)
        false_branch = self.build_tree(false_data, false_labels)

        # Возвращаем класс узла со всеми поддеревьями, то есть целого дерева
        return Node(index, t, true_branch, false_branch)

    def classify_object(self, obj, node):

        #  Останавливаем рекурсию, если достигли листа
        if isinstance(node, RegressionLeaf):
            answer = node.prediction
            return answer

        if obj[node.index] <= node.t:
            return self.classify_object(obj, node.true_branch)
        else:
            return self.classify_object(obj, node.false_branch)

    def predict(self, data):
        """
        Выполнить предсказание
        """
        classes = []
        for obj in data:
            prediction = self.classify_object(obj, self.Node)
            classes.append(prediction)
        return np.array(classes)

    def fit(self, train_data, train_labels):
        self.Node = self.build_tree(train_data, train_labels)


def R2(act, pred):
    S_total = ((act - np.mean(act))**2).sum()
    S_res = ((act - pred)**2).sum()
    return 1 - S_res / S_total
