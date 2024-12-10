FROM python:3.10-slim

WORKDIR /app

COPY . ./

EXPOSE 8081

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "src/main.py", "--server.port=8081", "server.address=0.0.0.0"]