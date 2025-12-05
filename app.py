import sys
import datetime

# Define the number of log lines to generate
NUM_LOG_LINES = 10000000

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"--- Application started: Generating {NUM_LOG_LINES} log lines ---")
sys.stdout.flush() # Ensure the header is sent

# Loop to generate the large burst of logs
for i in range(1, NUM_LOG_LINES + 1):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] # More precise timestamp
    
    # Log to STDOUT
    print(f"{timestamp} [BURST_INFO] Log Line {i:05d} of {NUM_LOG_LINES}. Testing log throughput.")
    
    # Optionally generate an error log every 1000 lines
    if i % 1000 == 0:
        print(f"{timestamp} [BURST_WARN] Checkpoint warning at line {i}.", file=sys.stderr)
        
# Note: Since we are using 'python -u' in the Dockerfile, the output is unbuffered
# and the flush() call is technically not required, but good practice if needed.
sys.stdout.flush()
sys.stderr.flush()

print(f"--- Finished generating {NUM_LOG_LINES} log lines. Application exiting. ---")

# The script exits here, causing the container to stop.
