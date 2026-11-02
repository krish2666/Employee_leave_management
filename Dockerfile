FROM python:3.11
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "library.py"]
