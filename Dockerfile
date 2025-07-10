FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential git clang flex bison libcap-dev libprotobuf-dev libnl-route-3-dev protobuf-compiler pkg-config ca-certificates \
    && git clone --depth 1 https://github.com/google/nsjail /tmp/nsjail \
    && make -C /tmp/nsjail \
    && install -m 755 /tmp/nsjail/nsjail /usr/local/bin/nsjail \
    && rm -rf /tmp/nsjail \
    && apt-get purge -y git clang \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app /app
COPY nsjail.cfg /app/nsjail.cfg
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "main.py"]
