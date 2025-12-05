FROM alpine:latest

# Number of logs
ENV LOG_COUNT=1000

# CMD that prints logs at runtime
CMD sh -c '
  echo "Starting runtime log container...";
  for i in $(seq 1 $LOG_COUNT); do
    echo "Log line $i - $(date)";
    echo "ERROR: something failed at line $i" >&2;
  done;
  echo "Completed $LOG_COUNT logs."
'
