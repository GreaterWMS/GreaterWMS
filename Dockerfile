FROM python:3.8.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .
RUN chmod +x ./entrypoint.sh

EXPOSE 8008

ENTRYPOINT ["/app/entrypoint.sh"]