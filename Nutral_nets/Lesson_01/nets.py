import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# нормализация массива
def normalize(X, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)


def to_one_hot(Y):
    n_col = np.amax(Y) + 1
    binarized = np.zeros((len(Y), n_col))
    for i in range(len(Y)):
        binarized[i, Y[i]] = 1.
    return binarized


# преобразование массива в необходимый вид
def from_one_hot(Y):
    arr = np.zeros((len(Y), 1))

    for i in range(len(Y)):
        hot = Y[i]
        for j in range(len(hot)):
            if hot[j] == 1:
                arr[i] = j + 1
    return arr


def sigmoid(var):
    return 1 / (1 + np.exp(-var))


class TwoLayerNet:
    """
    Class for neutral net with two layers
    """

    def __init__(self, neuron_numb, steps, learning_rate):
        self.learning_rate = learning_rate
        self.steps = steps
        self.neuron_numb = neuron_numb
        self.w0 = (1, 1)
        self.w1 = (1, 1)
        self.fit_flag = False

    # сигмоида и ее производная
    @staticmethod
    def act_func(var):
        return 1 / (1 + np.exp(-var))

    @staticmethod
    def act_func_deriv(var):
        return var * (1 - var)

    def fit(self, X_train, y_train):
        self.fit_flag = True
        # присваевание случайных весов
        self.w0 = 2 * np.random.random((X_train.shape[1], self.neuron_numb)) - 1  # для входного слоя
        self.w1 = 2 * np.random.random((self.neuron_numb, y_train.shape[1])) - 1  # для внутреннего слоя

        # процесс обучения
        accuracy = 0
        for i in range(self.steps):
            # прямое распространение(feed forward)
            layer0 = X_train
            layer1 = self.act_func(np.dot(layer0, self.w0))
            layer2 = self.act_func(np.dot(layer1, self.w1))

            # обратное распространение(back propagation) с использованием градиентного спуска
            layer2_error = y_train - layer2  # производная функции потерь = производная квадратичных потерь
            layer2_delta = layer2_error * self.act_func_deriv(layer2)

            layer1_error = layer2_delta.dot(self.w1.T)
            layer1_delta = layer1_error * self.act_func_deriv(layer1)
            # коррекция
            self.w1 += layer1.T.dot(layer2_delta) * self.learning_rate
            self.w0 += layer0.T.dot(layer1_delta) * self.learning_rate
            # метрика модели
            error = np.mean(np.abs(layer2_error))
            accuracy = (1 - error) * 100

        return accuracy

    def predict(self, X_test, y_test):
        if self.fit_flag:
            # прямое распространение(feed forward)
            layer0_t = X_test
            layer1_t = self.act_func(np.dot(layer0_t, self.w0))
            layer2_t = self.act_func(np.dot(layer1_t, self.w1))
            layer2_error_t = y_test - layer2_t

            # метрика модели
            error_t = np.mean(np.abs(layer2_error_t))
            accuracy_t = (1 - error_t) * 100
        else:
            accuracy_t = None

        return accuracy_t


class MultyLayerNet:
    """
    Class for neutral net with several layers
    """

    def __init__(self, num_layers, neuron_numb, steps, learning_rate, a_fuct):
        self.num_layers = num_layers
        self.learning_rate = learning_rate
        self.steps = steps
        self.neuron_numb = neuron_numb
        self.w = []
        self.layers = []
        self.layers_error = []
        self.layers_delta = []
        self.fit_flag = False
        self.a_fuct = a_fuct

    # сигмоида и ее производная
    def act_func(self, var):
        if self.a_fuct == 'tanh':
            return np.tanh(var)
        else:
            return sigmoid(var)

    def act_func_deriv(self, var):
        if self.a_fuct == 'tanh':
            return 1 - np.tanh(var) ** 2
        else:
            return var * (1 - var)

    def fit(self, X_train, y_train):
        self.fit_flag = True
        # присваевание случайных весов
        self.w.append(2 * np.random.random((X_train.shape[1], self.neuron_numb)) - 1)  # для входного слоя
        for n in np.arange(1, self.num_layers-1):
            self.w.append(2 * np.random.random((self.neuron_numb, self.neuron_numb)) - 1)  # для внутреннего слоя
        self.w.append(2 * np.random.random((self.neuron_numb, y_train.shape[1])) - 1)  # для последнего внутреннего слоя

        # процесс обучения
        accuracy = 0

        for i in range(self.steps):
            # прямое распространение(feed forward)
            self.layers.append(X_train)
            for n in np.arange(1, self.num_layers+1):
                self.layers.append(self.act_func(np.dot(self.layers[n-1], self.w[n-1])))

            # обратное распространение(back propagation) с использованием градиентного спуска

            self.layers_error.append(y_train - self.layers[-1])
            self.layers_delta.append(self.layers_error[-1] * self.act_func_deriv(self.layers[-1]))

            for n in np.arange(self.num_layers, 0, -1):
                self.layers_error.insert(0, self.layers_delta[0].dot(self.w[n-1].T))
                self.layers_delta.insert(0, self.layers_error[0] * self.act_func_deriv(self.layers[n-1]))

            # коррекция
            for n in np.arange(self.num_layers, 0, -1):
                self.w[n-1] += self.layers[n-1].T.dot(self.layers_delta[n]) * self.learning_rate

            # метрика модели
            error = np.mean(np.abs(self.layers_error[-1]))
            accuracy = (1 - error) * 100

        return accuracy

    def predict(self, X_test, y_test):
        if self.fit_flag:
            # прямое распространение(feed forward)
            layer0_t = X_test
            layer1_t = self.act_func(np.dot(layer0_t, self.w0))
            layer2_t = self.act_func(np.dot(layer1_t, self.w1))
            layer2_error_t = y_test - layer2_t

            # метрика модели
            error_t = np.mean(np.abs(layer2_error_t))
            accuracy_t = (1 - error_t) * 100
        else:
            accuracy_t = None

        return accuracy_t


if __name__ == '__main__':
    # Подготовка тренировочных данных
    # получения данных из csv файла. укажите здесь путь к файлу Iris.csv
    iris_data = pd.read_csv("Iris.csv")

    # замена текстовых значений на цифровые
    iris_data['Species'].replace(['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], [0, 1, 2], inplace=True)

    # формирование входных данных
    columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    x = pd.DataFrame(iris_data, columns=columns)
    x = normalize(x.values)

    # формирование выходных данных(результатов)
    columns = ['Species']
    y = pd.DataFrame(iris_data, columns=columns)
    y = y.values
    y = y.flatten()
    y = to_one_hot(y)

    # Разделение данных на тренировочные и тестовые
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    net = TwoLayerNet(5, 1000, 0.05)
    acc_train = net.fit(X_train, y_train)
    print(f"Точность сети на трейне {acc_train}")

    acc_test = net.predict(X_test, y_test)
    print(f"Точность сети на тeсте {acc_test}")

    # net_2 = MultyLayerNet(3, 5, 1000, 0.05, 'sigmoid')
    # acc_train_2 = net_2.fit(X_train, y_train)
    # print(f"Точность сети 2 на трейне {acc_train_2}")
