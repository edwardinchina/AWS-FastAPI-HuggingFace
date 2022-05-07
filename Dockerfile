FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1 #OUTPUT
EXPOSE 8000
WORKDIR /app
COPY /src .
RUN pip install -r requirements.txt
CMD ["uvicorn","--host","0.0.0.0","--port","8000","main:app"]