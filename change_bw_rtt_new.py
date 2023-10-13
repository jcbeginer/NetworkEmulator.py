#!/usr/bin/env python3
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description='Change network conditions for outbound traffic.')
    parser.add_argument('--interface', required=True, type=str, help='The network interface to control.')
    parser.add_argument('--BW', required=True, type=str, help='Bandwidth to set for the interface.')
    parser.add_argument('--latency', required=True, type=str, help='Latency to set for the interface.')
    args = parser.parse_args()
    
    # Clear existing qdiscs
    clear_cmd = f'sudo tc qdisc del dev {args.interface} root'
    subprocess.run(clear_cmd, shell=True)
    
    # Add the HTB qdisc with a default class
    cmd1 = f'sudo tc qdisc add dev {args.interface} root handle 1: htb default 10'
    subprocess.run(cmd1, shell=True, check=True)

    # Create a class under HTB for rate limiting
    cmd2 = f'sudo tc class add dev {args.interface} parent 1: classid 1:10 htb rate {args.BW}mbit'
    subprocess.run(cmd2, shell=True, check=True)

    # Add netem qdisc under the class to introduce delay
    cmd3 = f'sudo tc qdisc add dev {args.interface} parent 1:10 handle 10: netem delay {args.latency}ms'
    subprocess.run(cmd3, shell=True, check=True)

    # Attach bfifo qdisc for byte-based buffer limiting
    BUFFER_LIMIT = "2.7mb"
    cmd4 = f'sudo tc qdisc add dev {args.interface} parent 10: bfifo limit {BUFFER_LIMIT}'
    subprocess.run(cmd4, shell=True, check=True)

    print(f"Configured {args.interface} with {args.BW}mbit bandwidth, {args.latency}ms latency, and {BUFFER_LIMIT} buffer limit.")

if __name__ == "__main__":
    main()
