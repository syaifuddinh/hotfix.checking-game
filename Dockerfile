# Gunakan base image Python versi 3.8
FROM python:3.11.3

RUN apt-get update -y \
    && apt-get install -y wget unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Salin semua file yang diperlukan ke dalam container
COPY . /app

COPY .env /app

# Tentukan direktori kerja di dalam container
WORKDIR /app

RUN mv .env.production .env

# Install dependensi proyek
RUN pip install -r requirement.txt

# Spesifikasikan perintah untuk menjalankan aplikasi Python
CMD ["python", "index.py"]
