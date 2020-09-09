from sklearn import datasets
from sklearn import model_selection

from DesisionTree import DesisionTree, accuracy_metric
from RandomForestDesign import RandomForestDesign
from RegressionTree import RegressionTree, R2
from RandomForestRegression import RandomForestRegression


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
    classification_data, classification_labels = datasets.make_classification(n_samples=500,
                                                                              n_features=5, n_informative=5,
                                                                              n_classes=2, n_redundant=0,
                                                                              n_clusters_per_class=1, random_state=23)
    train_data, test_data, train_labels, test_labels = model_selection.train_test_split(classification_data,
                                                                                        classification_labels,
                                                                                        test_size=0.3,
                                                                                    random_state=1)

    n_trees = 10

    my_forest_1 = RandomForestDesign(n_trees=n_trees)
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



if __name__ == '__main__':
    # class_tree()
    # reg_tree()
    # rand_forest()
    reg_forest()
