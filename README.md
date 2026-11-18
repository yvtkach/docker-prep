### Compose sample application
### Python/Flask with Nginx proxy and MySQL database

Project structure:
```
.
├── compose.yaml
├── backend
│   ├── db
│   │   └─ password.txt
│   ├── Dockerfile
│   ├── requirements.txt
│   └── hello.py
└── proxy
     ├─── conf
     └─── Dockerfile

```
## What it is
A multi-container web application consisting of an Nginx reverse proxy, a Python Flask backend, and a MariaDB database that serves a list of blog posts.

## Requirements
- Git
- Docker and Docker Compose
- OpenSSL (for password generation)
- curl (for testing)

## Run it
   Clone the repository and enter the directory:
   ```bash
   git clone [https://github.com/yvtkach/docker-prep.git](https://github.com/yvtkach/docker-prep.git)
   cd docker-prep

## Create the database password file (do not use echo to avoid trailing newlines):

```bash
printf '%s' "$(openssl rand -hex 16)" > db/password.txt

```
> ℹ️ **_INFO_**  
> For compatibility purpose between `AMD64` and `ARM64` architecture, we use a MariaDB as database instead of MySQL.  
> You still can use the MySQL image by uncommenting the following line in the Compose file   
> `#image: mysql:8`

## Deploy with docker compose

```
$ docker compose up -d
Creating network "nginx-flask-mysql_default" with the default driver
Pulling db (mysql:8.0.19)...
5.7: Pulling from library/mysql
...
...
WARNING: Image for service proxy was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating nginx-flask-mysql_db_1 ... done
Creating nginx-flask-mysql_backend_1 ... done
Creating nginx-flask-mysql_proxy_1   ... done
```

## Expected result

Listing containers should show three containers running and the port mapping as below:
```
$ docker compose ps
NAME                          COMMAND                  SERVICE             STATUS              PORTS
nginx-flask-mysql-backend-1   "flask run"              backend             running             0.0.0.0:8000->8000/tcp
nginx-flask-mysql-db-1        "docker-entrypoint.s…"   db                  running (healthy)   3306/tcp, 33060/tcp
nginx-flask-mysql-proxy-1     "nginx -g 'daemon of…"   proxy               running             0.0.0.0:80->80/tcp
```

After the application starts, navigate to `http://localhost:80` in your web browser or run:
```
$ curl localhost:80
<div>Blog post #1</div><div>Blog post #2</div><div>Blog post #3</div><div>Blog post #4</div>
```

Stop and remove the containers
```
$ docker compose down

