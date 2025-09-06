FROM python:3.13.5-slim-bullseye
WORKDIR /docker
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]

