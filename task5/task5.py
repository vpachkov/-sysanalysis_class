import argparse
import json
import numpy as np


def extract_payload(templates):
    maxx = 0
    for i in range(len(templates)):
        if isinstance(templates[i], str):
            maxx += 1
        if isinstance(templates[i], list):
            maxx += len(templates[i])

    matrix = np.full((maxx, maxx), 0)

    for i in range(len(templates)):
        if isinstance(templates[i], str):
            for j in range(maxx):
                if j != int(templates[i])-1:
                    if matrix[(int(templates[i])-1), j] == 0:
                        matrix[(int(templates[i])-1), j] = 1
                    else:
                        matrix[(int(templates[i])-1), j] = 0
            matrix[:, (int(templates[i])-1)] = 1

        elif isinstance(templates[i], list):
            ls = []
            for v in templates[i]:
                ls.append(int(v)-1)
            for l in ls:
                for j in range(maxx):
                    if j not in ls:
                        if matrix[l, j] == 0:
                            matrix[l, j] = 1
                        else:
                            matrix[int(l), j] = 0
                matrix[:, l] = 1

    return matrix


def task(templates, templates_2):
    templates = json.loads(templates)
    templates_2 = json.loads(templates_2)

    a = (extract_payload(templates))
    b = (extract_payload(templates_2))

    at = a.T
    bt = b.T

    c = np.multiply(a, b)
    d = np.multiply(at, bt)

    e = c | d

    l = [[str(j+1), str(k+1)] for j in range(len(e))
         for k in range(j, len(e[j])) if e[j][k] == 0]

    return json.dumps(l)
