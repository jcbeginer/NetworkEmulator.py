#!/usr/bin/env python3
import subprocess
import argparse

def set_up_network(interface, ifb):
    # Commands to set up the IFB for ingress traffic control for a given interface.
    cmds = [
        f'sudo ip link set dev {ifb} up',
        f'sudo tc qdisc add dev {interface} handle ffff: ingress',
        f'sudo tc filter add dev {interface} parent ffff: u32 match u32 0 0 action mirred egress redirect dev {ifb}'
    ]

    for cmd in cmds:
        subprocess.run(cmd, shell=True, check=True)

def main():
    parser = argparse.ArgumentParser(description='Set up network conditions for two interfaces.')
    parser.parse_args()  # Currently not using any command-line arguments except the implicit ones.

    # Load the IFB module with two devices (ifb0 and ifb1).
    subprocess.run('sudo modprobe ifb numifbs=2', shell=True, check=True)

    interfaces_ifbs = {
        'WiFi0': 'ifb0',
        'WiFi1': 'ifb1'
    }

    for interface, ifb in interfaces_ifbs.items():
        try:
            set_up_network(interface, ifb)
        except subprocess.CalledProcessError:
            print(f"Failed to set up {interface}. It might be already set or there's another error.")

if __name__ == "__main__":
    main()
