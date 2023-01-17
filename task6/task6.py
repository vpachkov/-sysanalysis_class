import numpy as np
import json
import csv


def task(dt):
    if isinstance(dt, str):
        # В формате JSON.
        if dt.find("[") != -1:
            js = None
            try:
                js = json.loads(dt)
            except:
                raise ("Fail to parse")
            dt = js
        # В формате CSV.
        else:
            cs = None
            try:
                cs = dt.splitlines()
                cs = list(csv.reader(cs))
            except:
                pass
            dt = cs

    if dt is None:
        raise ("Fail to parse")

    if isinstance(dt, list):
        array = np.array(dt)

    SHAPE = (array.shape[0], array.shape[0])
    array = array.T

    A = np.zeros(SHAPE)
    B = np.zeros(SHAPE)
    C = np.zeros(SHAPE)

    def comp(el1, el2):
        if el1 < el2:
            return 1
        elif el1 == el2:
            return 0.5
        return 0

    for i in range(len(array)):
        for j in range(len(array)):
            A[i][j] = comp(array[i][0], array[j][0])
            B[i][j] = comp(array[i][1], array[j][1])
            C[i][j] = comp(array[i][2], array[j][2])

    result = (A + B + C) / 3
    k_0 = np.ones(result.shape[0])
    k_1 = np.ones(result.shape[0]) / result.shape[0]

    while np.max(np.abs(k_1 - k_0)) > 0.001:
        k_0 = k_1
        y_0 = np.dot(result, k_0)
        lambda_0 = np.dot(np.ones(result.shape[0]), y_0)
        k_1 = 1 / lambda_0 * y_0

    return json.dumps(np.round(k_1, 3).tolist())
