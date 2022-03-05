FROM python:3.9

RUN echo "a" \
    && echo "NOOOO"

RUN echo "IT'S FEATURE"
 
ENTRYPOINT ["/bin/bash"]
