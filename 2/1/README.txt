# Собираем образ контейнера со скриптом
docker build -t article .
# Запускаем используя файл .env с описанием credent для подключения к БД и общей папки на диске с nginx, скрипт генерит html файл 
# и размещает его в папку result/
docker run --name article --env-file .env -p 5000:5000 -v /opt/art:/app/result -d article

# Собираем и запускаем nginx c подключением общей папки
docker build -t ng .
docker run --name ng -p 8089:80 -v /opt/art:/usr/share/nginx/html -d ng

Проверяем на Ip кластера  http://10.73.1.115:8089 через две минуты обновляется содержимое страницы на статью с ид, взятым случайным 
образом.
Обращение из docker-контейнеров к statefulset c базой mysql получается только по ip Pod-а
В папке 2/ соберем все в отдельный pod c двумя контейнерами, credentials для подключения к БД будем передавать через secret
