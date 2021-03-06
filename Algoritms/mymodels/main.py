from sklearn import datasets
from sklearn import model_selection
import numpy as np

from DesisionTree import DesisionTree, accuracy_metric
from RandomForestDesign import RandomForestDesign
from RegressionTree import RegressionTree, R2
from RandomForestRegression import RandomForestRegression
from LogRegression import LogRegression, f1_score
from Boosting import Boosting


def class_tree():
    # сгенерируем и разобъем данные
    classification_data, classification_labels = datasets.make_classification(n_features=2, n_informative=2,
                                                                              n_classes=2, n_redundant=0,
                                                                              n_clusters_per_class=1, random_state=5)
    train_data, test_data, train_labels, test_labels = model_selection.train_test_split(classification_data,
                                                                                        classification_labels,
                                                                                        test_size=0.3,
                                                                                        random_state=27)

    dTree = DesisionTree(criteria='gini')
    dTree.fit(train_data, train_labels)
    train_answers = dTree.predict(train_data)
    test_answers = dTree.predict(test_data)
    print('Classification tree\n')
    print(f' Train data\n Accurance metric: { accuracy_metric(train_labels, train_answers):.6f}')
    print(f' Test data\n Accurance metric: { accuracy_metric(test_labels, test_answers):.6f}')


def reg_tree():
    X, y = datasets.make_regression(n_samples=1000, n_features=2, random_state=42)

    # Разобьем выборку на обучающую и тестовую
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                        test_size=0.3,
                                                                        random_state=1)
    tree = RegressionTree()
    tree.fit(X_train, y_train)

    y_pred_train = tree.predict(X_train)
    y_pred_test = tree.predict(X_test)

    # R2 на обучающей выборке
    r2_train = R2(y_train, y_pred_train)
    # R2 на тестовой выборке
    r2_test = R2(y_test, y_pred_test)
    print('\n\nRegression Tree\n')
    print(f' R2 train: {r2_train:.4f}')
    print(f' R2 test: {r2_test:.4f}')


def rand_forest():
    classification_data, classification_labels = datasets.make_classification(n_samples=1000,
                                                                              n_features=2, n_informative=2,
                                                                              n_classes=2, n_redundant=0,
                                                                              n_clusters_per_class=1, random_state=23)
    train_data, test_data, train_labels, test_labels = model_selection.train_test_split(classification_data,
                                                                                        classification_labels,
                                                                                        test_size=0.3,
                                                                                        random_state=1)

    n_trees = 10

    my_forest_1 = RandomForestDesign(n_trees=n_trees,
                                     max_depth=6,
                                     num_leaves=64,
                                     min_samples_leaf=5,
                                     criteria='gini')
    my_forest_1.fit(train_data, train_labels)
    train_answers = my_forest_1.tree_vote(train_data)
    test_answers = my_forest_1.tree_vote(test_data)

    # Точность на обучающей выборке
    train_accuracy = accuracy_metric(train_labels, train_answers)
    print('\n\nRandom forest\n')
    print(f' Точность случайного леса из {n_trees} деревьев на обучающей выборке: {train_accuracy:.3f}')

    # Точность на тестовой выборке
    test_accuracy = accuracy_metric(test_labels, test_answers)
    print(f' Точность случайного леса из {n_trees} деревьев на тестовой выборке: {test_accuracy:.3f}')


def reg_forest():
    X, y = datasets.make_regression(n_samples=1000, n_features=2, random_state=42)

    # Разобьем выборку на обучающую и тестовую
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                        test_size=0.3,
                                                                        random_state=1)
    n_trees = 2
    my_reg_forest = RandomForestRegression(n_trees=n_trees)
    my_reg_forest.fit(X_train, y_train)

    y_pred_train = my_reg_forest.tree_vote(X_train)
    y_pred_test = my_reg_forest.tree_vote(X_test)

    # R2 на обучающей выборке
    r2_train = R2(y_train, y_pred_train)
    # R2 на тестовой выборке
    r2_test = R2(y_test, y_pred_test)
    print('\n\nRandom Regression Forest\n')
    print(f' R2 train: {r2_train:.4f}')
    print(f' R2 test: {r2_test:.4f}')


def log_los_regression():
    loglos = LogRegression(iterations=1000, alpha=1e-4, tol=1e-5, bound=1e-5)

    # подготовка данных
    X = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 2, 1, 3, 0, 5, 10, 1, 2],
                  [500, 700, 750, 600, 1450,
                   800, 1500, 2000, 450, 1000],
                  [1, 1, 2, 1, 2,
                   1, 3, 3, 1, 2]], dtype=np.float64)

    y = np.array([0, 0, 1, 0, 1, 0, 1, 0, 1, 1], dtype=np.float64)

    loglos.fit(X, y)
    y_pred = loglos.predict_proba(X)
    print(f'f1 score: {f1_score(y_true=y, y_pred=y_pred)}')


def grad_boost():
    classification_data, classification_labels = datasets.make_classification(n_samples=1000,
                                                                              n_features=2, n_informative=2,
                                                                              n_classes=2, n_redundant=0,
                                                                              n_clusters_per_class=1, random_state=23)
    train_data, test_data, train_labels, test_labels = model_selection.train_test_split(classification_data,
                                                                                        classification_labels,
                                                                                        test_size=0.3,
                                                                                        random_state=1)

    n_trees = 10
    max_depth = 60
    num_leaves = 5
    min_samples_leaf = 5
    criteria = 'gini'

    model_b = Boosting(n_trees=n_trees,
                       max_depth=max_depth,
                       num_leaves=num_leaves,
                       min_samples_leaf=min_samples_leaf,
                       criteria=criteria)
    model_b.fit(train_data, train_labels)
    train_answers = model_b.predict(train_data)
    test_answers = model_b.predict(test_data)

    # Точность на обучающей выборке
    train_accuracy = accuracy_metric(train_labels, train_answers)
    print('\n\nГрадиентный бустинг\n')
    print(f'n_trees={n_trees}, max_depth={max_depth}, \
            num_leaves={num_leaves}, \
            min_samples_leaf={min_samples_leaf}, \
            criteria={criteria}')
    print(f' Точность на обучающей выборке: {train_accuracy:.3f}')

    # Точность на тестовой выборке
    test_accuracy = accuracy_metric(test_labels, test_answers)
    print(f' Точность на тестовой выборке: {test_accuracy:.3f}')


if __name__ == '__main__':
    # class_tree()
    # reg_tree()
    # rand_forest()
    # reg_forest()
    # log_los_regression()
    grad_boost()
