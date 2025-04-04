FROM python:3.10-slim

# Install dependencies and Chromium
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        chromium \
        chromium-driver \
        fonts-liberation \
        libnss3 \
        libxss1 \
        libgconf-2-4 \
        libasound2 \
        xvfb \
        curl \
        unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Chromium path
ENV CHROME_BIN=/usr/bin/chromium
ENV DISPLAY=:99

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app
COPY . /app
WORKDIR /app

# Run your script
CMD ["python", "it_renewer.py"]
