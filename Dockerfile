FROM python:3.10.0
WORKDIR /usr/src/app
COPY requirements.txt .
COPY . .
RUN python -m pip --no-cache-dir install --requirement requirements.txt \
    && rm requirements.txt
CMD ["python", "main.py"]
