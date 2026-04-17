\## Как запустить проект



Для запуска вам понадобятся установленные \*\*Docker\*\* и \*\*Docker Compose\*\*.



1\. Клонируйте репозиторий:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/zhoratolk/effective-mobile-devops.git](https://github.com/zhoratolk/effective-mobile-devops.git)

&#x20;  cd effective-mobile-devops

2\. Запустите контейнеры:

&#x20;   ```bash

&#x20;  docker-compose up -d --build



\## Как проверить результат

&#x20;  ```Bash

&#x20;  curl http://localhost

&#x20;  

&#x20;  Выведет Hello from Effective Mobile!

\## Как работает схема

Проект построен на взаимодействии двух сервисов внутри изолированной Docker-сети:



1\. Nginx (Proxy): - Слушает внешний порт 80.



&#x20;  Принимает входящие HTTP-запросы от пользователя.



&#x20;  Перенаправляет их на внутреннее имя сервиса backend на порт 8080.



2\. Backend (Python):



&#x20;  Простой HTTP-сервер на базе стандартных библиотек Python.



&#x20;  Слушает порт 8080 только внутри сети Docker.



&#x20;  Работает от имени не-root пользователя (myuser) для повышения безопасности.  



Трафик: Пользователь (Browser/Curl) -> Nginx:80 -> Docker Network -> Python:8080



