FROM alpine:latest

# Number of log lines (change 1000 to whatever you want)
ENV LOG_COUNT=1000

CMD sh -c '
  echo "Starting fixed-log container...";
  for i in $(seq 1 $LOG_COUNT); do
    echo "Log line $i - $(date)";
    echo "Random: $RANDOM";
    echo "ERROR: Something failed at line $i" >&2;
  done
  echo "Completed logging $LOG_COUNT lines."
'
