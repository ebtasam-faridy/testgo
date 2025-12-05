FROM alpine:latest

# Install bash for nicer scripting (optional)
RUN apk add --no-cache bash

CMD bash -c '
  i=1
  echo "Starting infinite log container..."
  while true; do
    echo "Log line $i - $(date)"
    echo "Random number: $RANDOM"
    echo "ERROR: simulated error at line $i" >&2
    i=$((i+1))
    sleep 0.2
  done
'
