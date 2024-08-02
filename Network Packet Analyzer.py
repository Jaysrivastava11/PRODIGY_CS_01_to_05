from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto
        
        # Check if the packet has a TCP or UDP layer
        if TCP in packet:
            protocol_type = 'TCP'
        elif UDP in packet:
            protocol_type = 'UDP'
        else:
            protocol_type = 'Other'
        
        # Display packet information
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol_type}")
        
        # Optionally display payload data if available
        if len(packet) > len(ip_layer):
            payload = packet[IP].payload
            print(f"Payload: {payload}")
        
        print("-" * 50)

def start_sniffing(interface="eth0"):
    print(f"Starting packet capture on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Replace 'eth0' with your network interface
    start_sniffing(interface="eth0")
