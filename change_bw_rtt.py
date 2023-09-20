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
    cmd = f'sudo tc qdisc replace dev {args.interface} root netem rate {bandwidth}mbit delay {latency}ms'

    print(cmd)
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    main()
