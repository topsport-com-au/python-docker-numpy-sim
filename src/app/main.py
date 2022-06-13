import argparse
import logging

import numpy as np

from app import config

logging.basicConfig(level=config.LOG_LEVEL)


n = 100000


def compute(ps: list[int]) -> str:
    rng = np.random.default_rng(654654)
    probs = np.array([p / 100 for p in ps])
    print(f"Inputs: {probs}")
    # rands = np.random.random(len(ps))
    rands = rng.random((n, len(ps)))
    sim = rands <= probs
    summed_sim = sim.sum(axis=1)
    unique, cnt = np.unique(summed_sim, return_counts=True)
    exact_summed = 0.0
    for elem in unique:
        exact_count = (summed_sim == elem).sum()
        exact_or_more_count = (summed_sim >= elem).sum()
        exact_prob = exact_count / n
        exact_or_more_prob = exact_or_more_count / n
        print(f"Exactly {elem}: {exact_prob} | {elem} or more: {exact_or_more_prob}")
        exact_summed += exact_prob
    assert np.isclose(exact_summed, 1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Provide some probabilities.")
    parser.add_argument(
        "probabilities",
        metavar="N",
        type=int,
        nargs="+",
        help="a list of probabilities for the simulation",
    )
    args = parser.parse_args()
    compute(args.probabilities)


if __name__ == "__main__":
    main()
