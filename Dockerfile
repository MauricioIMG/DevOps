FROM python:3.12.5-slim-bullseye

WORKDIR /opt/python-api/

COPY . /opt/python-api/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8005

CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8005"]