#!/usr/bin/env python

# Required for parsing JSON
import json
# Use to generate random measurement values
import random
# Generate current timestamp values
import time

# Open the param.json file and parse JSON.
with open("param.json") as f:
    parameters = json.load(f)

# Extract the plugin configuration
source = parameters["source"]
interval = parameters["interval"]

# Metric identifier
metric = 'TUTORIAL_METRIC'

# Run in a continuous loop sending measurements to standard out
while True: 
    # Get the current timestamp
    timestamp = int(time.time())

    # Generate a random value
    value = random.randrange(0, 99)

    # Format measurement string and write to standard out
    print("{0} {1} {2} {3}".format(metric, source, value, timestamp))

    # Wait for the next interval
    time.sleep(float(interval))
