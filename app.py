import time
import sys
import datetime
# No need for manual flush() calls with 'python -u'

time.sleep(300)
i = 0
while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Logs will now stream immediately because of the -u flag in the Dockerfile
    print(f"{current_time} [INFO] Cycle {i}: Service is running and logging.")

    if i % 5 == 0 and i > 0:
        # Logs to stderr stream
        print(f"{current_time} [WARN] A background process warning on cycle {i}.", file=sys.stderr)

    i += 1
    time.sleep(5)
