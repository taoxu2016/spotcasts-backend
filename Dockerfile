FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9081

CMD ["scrapyrt", "-i", "0.0.0.0", "-p", "9081"]
