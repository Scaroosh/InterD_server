FROM python:3.9-slim-buster AS builder
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-dev gcc libffi-dev libpython3-dev
RUN pip install -r requirements.txt

# Second stage: Use a minimal Python image
FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /app/ .
COPY . .
EXPOSE 5000
ENV FLASK_APP=server.py
CMD ["flask", "run", "--host", "0.0.0.0"]
