FROM bitnami/python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 5058
WORKDIR /app

RUN apt-get update && apt-get install git -y && \
    apt-get install libgl1 libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 -y 

COPY ./require/req.txt /tmp/req.txt
# COPY ./require/ml.txt /tmp/ml.txt

RUN pip install --upgrade pip && \
    pip install -r /tmp/req.txt
    # pip install -r /tmp/ml.txt

COPY . ./
ENV PYTHONPATH app

# Use the ping endpoint as a healthcheck,
# so Docker knows if the API is still running ok or needs to be restarted
HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8080/ping || exit 1


CMD ["python", "app/server.py"]

