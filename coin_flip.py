# probability_statistics/coin_flip.py
from config_probability_statistics import logger
import warnings

import numpy as np
import scipy.stats as stats
from scipy.stats import norm, beta
import matplotlib.pyplot as plt

def plot_beta_distribution(x, y, heads, n_trials):
    plt.figure(figsize=(8, 5))

    plt.plot(x, y, label=f'Observed {n_trials} tosses,\n {heads} heads')
    plt.fill_between(x, 0, y, color='#348ABD', alpha=0.4)
    plt.vlines(0.5, 0, max(y), color="k", linestyles="--", lw=1)

    plt.xlabel("Probability of Heads (P(Head))")  # X-axis label
    plt.ylabel("Density")  # Y-axis label

    plt.legend().get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)
    plt.title(f'Estimated Probability of Heads: {heads / n_trials:.3f}')

    plt.show()

def compute_beta_distribution(max_trials=10000, threshold=0.001):
    data = stats.bernoulli.rvs(0.5, size=max_trials)
    heads = 0  # Total number of heads
    previous_estimate = None

    for n_trial in range(1, max_trials + 1):
        heads += data[n_trial - 1]
        current_estimate = heads / n_trial

        if previous_estimate is not None and abs(current_estimate - previous_estimate) < threshold:
            break

        previous_estimate = current_estimate

    a, b = 1, 1  # Prior (uninformative prior)
    s = heads
    f = n_trial - s

    x = np.linspace(0, 1, 100)  # Probability range
    y = beta.pdf(x, a + s, b + f)  # Compute Beta distribution

    return x, y, heads, n_trial

def coin_flip_main():
    logger.info("coin_flip_main()")
    warnings.filterwarnings("ignore")
    x, y, heads, n_trials = compute_beta_distribution()
    logger.info(f"n_trials = {n_trials}; heads = {heads}")
    plot_beta_distribution(x, y, heads, n_trials)

if __name__ == "__main__":
    import datetime, time
    logger.info("Run directly")
    start_time = time.time()
    coin_flip_main()
    end_time = time.time()
    execution_time = end_time - start_time
    execution_time_readable = str(datetime.timedelta(seconds=execution_time))