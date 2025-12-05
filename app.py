import time
import sys
import datetime
import os

# Get environment variable set by Harness (optional, but good practice)
build_number = os.environ.get('HARNESS_BUILD_ID', 'LOCAL')

print(f"--- Application started for build: {build_number} ---")
sys.stdout.flush() # Ensure the initial message is immediately sent

i = 0
while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log to STDOUT (Standard/Informational Logs)
    # These will typically appear in green/white text in Harness
    print(f"{current_time} [INFO] Cycle {i}: Executing business logic.")
    sys.stdout.flush() 

    # Log to STDERR (Warnings/Errors)
    # These often appear in yellow/red text in Harness (depending on configuration)
    if i % 5 == 0 and i > 0:
        print(f"{current_time} [WARN] A recoverable error occurred on cycle {i}.", file=sys.stderr)
        sys.stderr.flush()

    i += 1
    time.sleep(1) # Wait 1 second
