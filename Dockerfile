FROM alpine:latest

# Safe shell script for generating logs during build
RUN echo "#!/bin/sh" > /tmp/buildlog.sh \
 && echo "for i in \$(seq 1 1000); do echo Build log line \$i; done" >> /tmp/buildlog.sh \
 && chmod +x /tmp/buildlog.sh \
 && sh /tmp/buildlog.sh
