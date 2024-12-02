import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = 10000
sample_size = 30
num_samples = 1000

# Generate a non-normal population distribution (e.g., uniform distribution)
population = np.random.uniform(0, 10, population_size)

# Collect sample means
sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(num_samples)]

# Plot the population distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(population, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Population Distribution (Uniform)', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Plot the sampling distribution of the sample mean
plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Sampling Distribution of the Sample Mean', fontsize=14)
plt.xlabel('Sample Mean', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.tight_layout()
plt.show()