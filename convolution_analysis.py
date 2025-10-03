import numpy as np
import matplotlib.pyplot as plt

# 1. Create sin function: 10 cycles (20π), 200 samples per cycle = 2000 total samples
num_cycles = 10
samples_per_cycle = 200
total_samples = num_cycles * samples_per_cycle

x = np.linspace(0, num_cycles * 2 * np.pi, total_samples)
sin_signal = np.sin(x)

# 2. Create kernel from indices 35-65
kernel = sin_signal[35:66]  # 66 because end index is exclusive
# 5. Print kernel values and indexes
print("\n=== Kernel Information ===")
print("Kernel indices: 35-65")
print(f"Kernel length: {len(kernel)}")
print("\nKernel values:")
for i, val in enumerate(kernel, start=35):
    print(f"Index {i}: {val:.6f}")

# 3. Perform convolution
convolution_result = np.convolve(sin_signal, kernel, mode='valid')

# Find top 10 highest results and their first indices
sorted_indices = np.argsort(convolution_result)[::-1]  # Sort descending
top_10_indices = []
top_10_values = []

# Get unique top 10 values and their first occurrence
seen_values = set()
for idx in sorted_indices:
    value = convolution_result[idx]
    if value not in seen_values:
        top_10_values.append(value)
        # Find first index of this value
        first_idx = np.where(convolution_result == value)[0][0]
        top_10_indices.append(first_idx)
        seen_values.add(value)
        if len(top_10_values) == 10:
            break

print("\n=== Top 10 Highest Convolution Results ===")
for i, (value, idx) in enumerate(zip(top_10_values, top_10_indices), 1):
    count = np.sum(convolution_result == value)
    print(f"{i}. Value: {value:.6f} | First index: {idx} | Detected {count} time(s)")

# Keep the highest for visualization
max_value = top_10_values[0]
first_max_index = top_10_indices[0]
max_indices = np.where(convolution_result == max_value)[0]

# 4. Draw graphs
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Top graph: Original sin function
ax1.plot(x/np.pi, sin_signal, 'b-', linewidth=1.5, label='sin(x)')
ax1.axvspan(x[35]/np.pi, x[65]/np.pi, alpha=0.3, color='red', label='Kernel region (35-65)')
ax1.set_title('Original Sin Function (10 cycles, 2000 samples)', fontsize=14, fontweight='bold')
ax1.set_xlabel('x (in terms of π)', fontsize=12)
ax1.set_ylabel('Amplitude', fontsize=12)
ax1.set_xticks(np.arange(0, 21, 2))
ax1.set_xticklabels([f'{i}π' for i in range(0, 21, 2)])
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)

# Bottom graph: Convolution results
ax2.plot(convolution_result, 'g-', linewidth=1.5, label='Convolution result')
ax2.axhline(y=max_value, color='r', linestyle='--', linewidth=2, label=f'Max value: {max_value:.3f}')
ax2.axvline(x=first_max_index, color='orange', linestyle='--', linewidth=2, label=f'First max at index: {first_max_index}')
ax2.scatter(max_indices, [max_value] * len(max_indices), color='red', s=100, zorder=5, label='All max points')
ax2.set_title('Convolution Result', fontsize=14, fontweight='bold')
ax2.set_xlabel('Index', fontsize=12)
ax2.set_ylabel('Convolution Value', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.show()

