#Создаем secret для логина-пароля к БД
kubectl create secret generic artpod-secret --from-literal=user=root --from-literal=passw=admin -n tenz --dry-run=client -o yaml > artpod-secret.yaml
kubectl create -f artpod-secret.yaml

#Данные о имени БД и namepod с БД передадим через configMap
kubectl create -f artpod-conf.yaml

#Запустим artpod.yaml  с двумя контейнерами, опрашивать будем nginx на 80 порту. Сервис ClusterIP получим ip и пробросим порт 80:80.
kubectl apply - f artpod.yaml

#Для просмотра в браузере (у меня нет GUI) я сделаю сервис NodePort:31777 
