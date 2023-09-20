#!/usr/bin/env python3
import subprocess
import time
import threading
import argparse
import pandas as pd



def main():
    parser = argparse.ArgumentParser(description='Change network conditions.')
    parser.add_argument('--interface', type=str, help='The network interface to control.')
    parser.add_argument('--BW', type=str, help='The network interface to control.')
    parser.add_argument('--latency', type=str, help='The network interface to control.')
    args = parser.parse_args()
    bandwidth=args.BW
    latency=args.latency
    cmd = f'sudo tc qdisc replace dev ifb0 root netem rate {bandwidth}mbit delay {latency}ms'
    subprocess.run(cmd, shell=True, check=True)

    

if __name__ == "__main__":
    main()
