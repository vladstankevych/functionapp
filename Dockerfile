FROM python:3.9

RUN echo "a" \
    && echo "b"
 
ENTRYPOINT ["/bin/bash"]
