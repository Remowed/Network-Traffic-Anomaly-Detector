import numpy as np
import os

# sanity check
print("Current working directory:", os.getcwd())
print("Files in folder:", os.listdir())

data = np.genfromtxt(
    "traffic.csv",
    delimiter=",",
    names=True,  # use header
    dtype=None,
    encoding="utf-8"
)

packet_sizes = data["packet_size"]

mean_size = np.mean(packet_sizes)
std_size = np.std(packet_sizes)

print(f"Average packet size: {mean_size:.2f}")
print(f"Standard deviation: {std_size:.2f}")

z_scores = (packet_sizes - mean_size) / std_size

THRESHOLD = 3
anomalies = np.abs(z_scores) > THRESHOLD

print("\n--- Anomaly Report ---")

found = False

for i, is_anomaly in enumerate(anomalies):
    if is_anomaly:
        found = True
        print("⚠️  Suspicious packet detected")
        print(f"   Timestamp  : {data[i]['timestamp']}")
        print(f"   Source IP  : {data[i]['src_ip']}")
        print(f"   Dest IP    : {data[i]['dst_ip']}")
        print(f"   Packet size: {packet_sizes[i]}")
        print(f"   Z-score    : {z_scores[i]:.2f}\n")

if not found:
    print("No anomalies detected.")
