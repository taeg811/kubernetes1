FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . ./
#RUN mkdir -p /app/result выше передаю и каталог result/ для результатов работы скрипта
CMD [ "python", "/app/script.py" ]
