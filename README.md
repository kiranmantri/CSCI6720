## Run PostgreSQL Docker First


```bash
docker run \
  --name pg10 \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=p4ssw0rd \
  -e POSTGRES_DB=CSCI6720G \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v $(pwd)/data:/var/lib/postgresql/data \
  -p 5432:5432 --rm -it \
  postgres:10

  ```

## Init the Database 

```bash
python init.db

```

## Run the Worker (listener)

```bash
python worker.py

```


## Run the data producer
```bash
python producer.py

```
