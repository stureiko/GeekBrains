import numpy as np


class LogRegression:
    """
    Класс модели логистической регрессии

    Parameters:
        ------------
            iterations=1000
                Количество итераций
            alpha=1e-4
                Скорость обучения
            tol=1e-5
                Выход из цикле, если ошибка меняется менее tol
            bound=1e-5
                граница отсечения хвостов сигмоиды
    """

    def __init__(self, iterations=1000, alpha=1e-4, tol=1e-5, bound=1e-5):
        self.iterations = iterations
        self.alpha = alpha
        self.tol = tol
        self.bound = bound
        self.weights = None
        self.errors = None



    def fit(self, X_input: np.array, y_input: np.array):
        """
        Вычисление модели логистической регрессии
        Parameters:
        ------------
            X: np.array
                Матрица признаков
            y: np.array
                Вектор ответов

        Returns:
        -----------
            weights:np.array
                Вектор весов модели
            errors: np.array
                Вектор ошибок по признакам
        """
        X = self.calc_std_feat(X_input)
        np.random.seed(42)
        W = np.random.randn(X.shape[0])
        n = X.shape[1]

        errors, weights = [], []

        for n_iter in range(1, self.iterations + 1):
            z = np.dot(W, X)
            y_pred = self.sigmoid(z)
            current_error = self.calc_logloss(y_input, y_pred)
            W -= self.alpha * (1 / n * np.dot((y_pred - y_input), X.T))

            errors.append(current_error)
            weights.append(W)

            # проверяем выход по условию tol
            if n_iter > 2 and np.abs(current_error - errors[-2]) < self.tol:
                break
        self.errors = np.array(errors)
        self.weights = np.array(weights[-1])
        return weights, errors

    @staticmethod
    def sigmoid(z) -> float:
        """
        Вычисление сигмоид преобразования

        Parameters:
        -----------
        z: float
            вещественное число

        Returns:
        -----------
            res:float = 1 / (1 + np.exp(-z))
        """
        res = 1 / (1 + np.exp(-z))
        return res

    def calc_logloss(self, y_true: np.array, y_pred: np.array) -> float:
        """
        Вычисление log-loss

        Parameters
        ==============
        y_true - вектор правильных ответов
        y_pred - вектор прогноза

        """
        y_pred = y_pred.copy()
        y_pred = np.clip(y_pred, a_min=self.bound, a_max=1 - self.bound)
        err = - np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))
        return err

    def predict_proba(self, X: np.array) -> np.array:
        """
        Функция вычисления предсказанной вероятности

        Parameters:
        ------------
        W:np.array
            вектор весов обученной модели
        X:np.array
            матрица признаков

        Returns:
        ------------
        y_pred:np.array
            вектор прогнозов
        """
        return self.sigmoid(self.weights @ X)

    def predict(self, X: np.array, bound: float = 0.5) -> np.array:
        """
        Функция вычисления предсказанной вероятности (лейблов признаков) на
        основе сигмоид преобразования по полученному вектору прогнозов

        Parameters:
        ------------
        W - вектор весов
        X - матрица признаков
        bound=0.5 - порог вероятности

        returns:
        y_pred - вектор предсказаний
        """
        y_pred = self.sigmoid(self.weights @ X)
        y_pred = np.where(y_pred > bound, 1, 0)

        return y_pred

    @staticmethod
    def calc_std_feat(X: np.array) -> np.array:
        """
        Scaling features using standardization
        The first sign is const = 1, so does not scale
        Parameters:
        ----------------
        X: np.array
            Feature matrix

        Returns:
        ----------------
            X_trasformed: np.array
                Scaled feature matrix
        ================================================

        Масштабирование признаков методом стандартизации
        Первый признак const=1, поэтому не масштабируется

        Parameters:
        ----------------
        X: np.array
            Матрица признаков

        Returns:
        ----------------
            X_trasformed: np.array
                Масштабированная матрица признаков
        """
        X_transformed = X[1:, ].copy()
        X_mean, X_std = X_transformed.mean(axis=1), X_transformed.std(axis=1)
        X_mean, X_std = X_mean.reshape(X_transformed.shape[0], 1), X_std.reshape(X_transformed.shape[0], 1)

        X_transformed = (X_transformed - X_mean) / X_std
        X_transformed = np.vstack((np.ones(X_transformed.shape[1]), X_transformed))
        return X_transformed


def err_matrix(y_true: np.array, y_pred: np.array):
    """
    Вычисление матрицы ошибок

    Parameters:
    ------------
    y_true: np.array
        вектор правильных ответов
    y_pred: np.array
        вектор предсказаний

    Returns:
    ------------
    TP: int - TruePositive,
    FP: int - FalsePositive,
    TN: int - TrueNegative,
    FN: int - FalseNegative
        Значения матрицы ошибок

    """
    TP = y_true[(y_true - y_pred) == 0].sum().astype(int)
    FP = ((y_true - y_pred) == -1).sum().astype(int)
    TN = (y_true[(y_true - y_pred) == 0] == 0).sum().astype(int)
    FN = ((y_true - y_pred) == 1).sum().astype(int)
    return TP, FP, TN, FN


def precision_score(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычсление метрики precision
    конверсия = TP / (TP + FP)

    Parameters:
    ------------
    y_true: np.array
        вектор правильных ответов
    y_pred: np.array
        вектор предсказаний

    Returns:
    ------------
    precision: float
        значение метрики precision
    """
    TP, FP, _, _ = err_matrix(y_true, y_pred)
    return TP / (TP + FP)


def recall_score(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисление метрики recall = TP / (TP + FN)

    Parameters:
    ------------
    y_true: np.array
        вектор правильных ответов
    y_pred: np.array
        вектор предсказаний

    Returns:
    ------------
    recall: float
        значение метрики precision
    """
    TP, _, _, FN = err_matrix(y_true, y_pred)
    return TP / (TP + FN)


def f1_score(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисление метрики F1:

    Parameters:
    ------------
    y_true: np.array
        вектор правильных ответов
    y_pred: np.array
        вектор предсказаний

    Returns:
    ------------
    F1: float
        значение метрики F1
    """

    return round(
        2 * precision_score(y_true, y_pred) * recall_score(y_true, y_pred) / (precision_score(y_true, y_pred) +
                                                                              recall_score(y_true, y_pred)), 4)
