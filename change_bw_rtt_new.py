#!/usr/bin/env python3
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description='Change network conditions for outbound traffic.')
    parser.add_argument('--interface', type=str, help='The network interface to control.')
    parser.add_argument('--BW', type=str, help='Bandwidth to set for the interface.')
    parser.add_argument('--latency', type=str, help='Latency to set for the interface.')
    args = parser.parse_args()
    bandwidth = args.BW
    latency = args.latency

    # Directly apply to the interface for outbound control
    cmd = f'sudo tc qdisc replace dev {args.interface} root netem rate {bandwidth}mbit delay {latency}ms bfifo limit 2.7mb' #실험을 통해서 cellular buffer size가 1500Bytes * 800이라는 걸 알아내서 이렇게 시도!
    # Variables (Replace with your actual values)
    INTERFACE="{args.interface}"
    BUFFER_LIMIT="2.7mb"

# Add the HTB qdisc with a default class
    cmd1=f'sudo tc qdisc add dev {args.interface} root handle 1: htb default 10'

# Create a class under HTB for rate limiting
    cmd2=f'sudo tc class add dev {args.interface} parent 1: classid 1:10 htb rate {bandwidth}mbit'

# Add netem qdisc under the class to introduce delay
    cmd3=f'sudo tc qdisc add dev {args.interface} parent 1:10 handle 10: netem delay {latency}ms'

# Attach bfifo qdisc for byte-based buffer limiting
    cmd4=f'sudo tc qdisc add dev {args.interface} parent 10: bfifo limit {BUFFER_LIMIT}'


    print(cmd)
    
    subprocess.run(cmd1, shell=True, check=True)
    subprocess.run(cmd2, shell=True, check=True)
    subprocess.run(cmd3, shell=True, check=True)
    subprocess.run(cmd4, shell=True, check=True)

if __name__ == "__main__":
    main()
