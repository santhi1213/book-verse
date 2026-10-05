FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=300 --retries=10 --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Create startup script to run migrations then start app
RUN printf '#!/bin/sh\nflask db upgrade || true\npython run.py\n' > /app/start.sh && \
    chmod +x /app/start.sh

CMD ["/app/start.sh"]
