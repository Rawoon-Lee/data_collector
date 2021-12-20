# keras_regression.py
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def regression_basic():
    x = [1, 2, 3]
    y = [1, 2, 3]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
                  loss=tf.keras.losses.mse)

    model.fit(x, y, epochs=100)
    print(model.evaluate(x, y))

    preds = model.predict(x)
    print(preds)


def get_cars():
    cars = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/data/cars.csv', index_col=0)

    return cars.speed.values, cars.dist.values


def regression_cars():
    x, y = get_cars()

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.0001),
                  loss=tf.keras.losses.mse)

    model.fit(x, y, epochs=100)
    print(model.evaluate(x, y))

    preds = model.predict(x)
    print(preds)

    plt.plot(x, y, 'ro')
    plt.plot(x, preds)
    # plt.show()


def regression_trees():
    trees = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/data/trees.csv', index_col=0)

    x, y = np.float32(trees.values[:, :-1]), trees.values[:, -1:]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
                  loss=tf.keras.losses.mse)

    model.fit(x, y, epochs=100)
    print(model.evaluate(x, y))

    # preds = model.predict(x)
    # print(preds)


# regression_basic()
# [[1.001347 ]
#  [2.001547 ]
#  [3.0017474]]

# regression_cars()

regression_trees()
