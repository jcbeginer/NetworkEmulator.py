#!/usr/bin/env python3
import subprocess
import time
import threading
import argparse
import pandas as pd


def set_up_network(interface):
    # Set up the IFB for the ingress traffic control.
    cmd1 = f'sudo modprobe ifb numifbs=1'
    cmd2 = f'sudo ip link set dev ifb0 up'
    cmd3 = f'sudo tc qdisc add dev {interface} handle ffff: ingress'
    cmd4 = f'sudo tc filter add dev {interface} parent ffff: u32 match u32 0 0 action mirred egress redirect dev ifb0'

    subprocess.run(cmd1, shell=True, check=True)
    subprocess.run(cmd2, shell=True, check=True)
    subprocess.run(cmd3, shell=True, check=True)
    subprocess.run(cmd4, shell=True, check=True)
"""
def change_network_conditions(file, direction, interface):
    df = pd.read_csv(file)  # Read the CSV file.
    while True:
        for index, row in df.iterrows():
            # Extract the bandwidth and latency values.
            bandwidth = row['bandwidth']
            latency = row['delay']

            # Print the current bandwidth and latency values.
            print(f"Changing {direction} bandwidth to: {bandwidth}Mbps and latency to: {latency}ms")

            # Create the command string.
            if direction == "downlink":
                cmd = f'sudo tc qdisc replace dev {interface} root netem rate {bandwidth}mbit delay {latency}ms'
            elif direction == "uplink":
                cmd = f'sudo tc qdisc replace dev ifb0 root netem rate {bandwidth}mbit delay {latency}ms'

            # Execute the command.
            subprocess.run(cmd, shell=True, check=True)

            # Wait 100ms before next iteration.
            time.sleep(0.1)
"""
def main():
    parser = argparse.ArgumentParser(description='Change network conditions.')
    #parser.add_argument('--file', type=str, help='The CSV file to read network conditions from.')
    #parser.add_argument('--direction', type=str, choices=['uplink', 'downlink'], help='The direction of the network conditions to change.')
    #parser.add_argument('--interface', type=str, help='The network interface to control.')
    #args = parser.parse_args()

    #if args.direction == "uplink":
    interfaces = ['WiFi0','WiFi1']
    for interface in interfaces:
      try : set_up_network(interface)
      except : print("Alread setted interface")
    
    #thread = threading.Thread(target=change_network_conditions, args=(args.file, args.direction, args.interface))
    #thread.start()
    #thread.join()

if __name__ == "__main__":
    main()
