FROM python:3.12-slim

WORKDIR /app
COPY bridge-requirements.txt .
RUN pip install --no-cache-dir -r bridge-requirements.txt
COPY bridge_identity.py github_artwork_source.py bridge_service.py ./

ENV PYTHONDONTWRITEBYTECODE=1
CMD ["sh", "-c", "exec gunicorn --bind :${PORT:-8080} bridge_service:application"]
