FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4 pyyaml

CMD ["python", "src/main.py", "--config", "src/config/config.yaml"]