import csv

with open("raw_traffic.csv", newline="", encoding="utf-8") as infile, \
     open("traffic.csv", "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    writer.writerow(["timestamp", "src_ip", "dst_ip", "packet_size"])

    for row in reader:
        try:
            timestamp = int(float(row["Time"]))
            src_ip = row["Source"]
            dst_ip = row["Destination"]
            size = int(row["Length"])

            writer.writerow([timestamp, src_ip, dst_ip, size])
        except Exception:
            continue