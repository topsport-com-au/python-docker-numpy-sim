import logging

import numpy as np

from app import config

logging.basicConfig(level=config.LOG_LEVEL)


n = 100000
ps = [.6, .4, .3, .3, .4, .1, .3, .3]


def main() -> str:
    probs = np.array(ps)
    # rands = np.random.random(len(ps))
    rands = np.random.random((n, len(ps)))
    sim = (rands <= probs)
    summed_sim = sim.sum(axis=1)
    unique, cnt = np.unique(summed_sim, return_counts=True)
    for elem in unique:
        count = (summed_sim >= elem).sum()
        print(elem, count / n)
