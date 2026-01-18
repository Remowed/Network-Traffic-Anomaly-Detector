# Network-Traffic-Anomaly-Detector

I captured real network using Wireshark to extract packet data. I used Python with NumPy to model normal packet behavior. 
I used Z-score anomaly detection to flag packets that significantly deviated from baseline traffic patterns.

I also wrote a script called convert_wireshark.py to keep only the things that I was interested in, like timestamp, src_ip, dst_ip and packet_size. The raw_traffic.csv is supposed to hold the csv from WireShark and the traffic.csv is the converted one.

This model is quite simple and does not work in real time.
