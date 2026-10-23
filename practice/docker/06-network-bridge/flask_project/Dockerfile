FROM python:3.9-slim
WORKDIR /app
COPY flask_app.py /app/
RUN pip install flask
EXPOSE 5000
CMD ["python", "flask_app.py"]
