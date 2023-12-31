Ref : https://github.com/lgs96/NetworkEmulator

I have copied this code because I don't have permission to push

# Network Condition Manipulation with Python and Netem

This repository contains a Python script to manipulate network conditions based on bandwidth and latency values stored in a CSV file. It uses the `tc` and `netem` Linux tools to change the conditions every 100 milliseconds.

The script can manipulate both uplink and downlink traffic conditions.

## Requirements

The script requires Python 3 and the following Python libraries:

- pandas
- subprocess
- time
- threading
- argparse

The script also requires the following Linux tools and modules:

- tc
- netem
- ifb (for uplink traffic manipulation)

## Usage

To run the emulation, use the following command:

```bash
sudo python3 emulation.py --interface <interface_name> --file <path_to_your_csv_file> --direction <uplink_or_downlink>
```

To run the change_bw_rtt.py, use the following command:

```bash
sudo python3 change_bw_rtt.py --interface <interface_name> --BW <BW_Mbits> --latency <delay_latency_value_ms>
```


To reset the emulation setting:

```bash
sudo python3 reset_emulation.py 
