import numpy as np
import csv
from io import StringIO


def task(data):
    f = StringIO(data)
    reader = csv.reader(f, delimiter=',')
    vertecies = []
    for row in reader:
        vertecies.append(row)

    N = len(vertecies)

    cnt = [list() for _ in range(5)]
    cnt[0] = [x[0] for x in vertecies]
    cnt[1] = [x[1] for x in vertecies]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if vertecies[i][0] == vertecies[j][1]:
                cnt[2].append(vertecies[j][0])

            if vertecies[i][1] == vertecies[j][0]:
                cnt[3].append(vertecies[j][1])

            if vertecies[i][0] == vertecies[j][0]:
                cnt[4].append(vertecies[j][1])

    nodes = list(set(np.array(vertecies).reshape((-1,))))
    nodes = list(map(lambda x: x-1, nodes))
    ans = [list() for _ in range(len(nodes))]

    for node in nodes:
        for clist in cnt:
            ans[node].append(clist.count(str(node+1)))

    npans = np.array(ans)
    nprans = npans / (len(nodes) - 1)
    s = (nprans * np.log2(nprans, where=(nprans != 0)))
    s = np.nan_to_num(s, nan=0)
    return np.sum(s) * -1
