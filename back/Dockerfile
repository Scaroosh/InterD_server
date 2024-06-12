FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-dev gcc libffi-dev libpython3-dev
# Install TA-Lib
RUN pip install ta-lib
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=server.py
CMD ["flask", "run", "--host", "0.0.0.0"]