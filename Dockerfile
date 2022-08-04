FROM python:3.9-slim

RUN apt-get update \
&& apt-get install -y --no-install-recommends git

COPY . .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir kserve==0.8.0
RUN pip install protobuf==3.20.1
RUN pip install --no-cache-dir -e .

ENTRYPOINT ["python", "KWSTransformer/kws_transformer.py"]