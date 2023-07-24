# Base image: Python 3.9
FROM python:3.9

# Çalışma dizinini /app olarak ayarlayın
WORKDIR /app

# Gerekli Python bağımlılıklarını kopyalayın
COPY requirements.txt .

# Bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalayın
COPY . .

# Docker container'ında testleri çalıştırın
CMD ["python -m pytest --headless"]
