FROM python:3.12.5-slim

WORKDIR /opt/python-api/

COPY . /opt/python-api/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8001"]