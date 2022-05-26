### python 패키지 redis, celery 설치 및 실행

```shell
pip3 install redis

celery -A tasks worker --loglevel=INFO
```

### celery 실행 시 아래와 같이 콘솔 확인됨
```shell
  ~/Study/celery  celery -A tasks worker --loglevel=INFO

[2022-05-26 14:26:44,902: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'

celery@blabla.local v5.1.2 (sun-harmonics)

Darwin-21.3.0-x86_64-i386-64bit 2022-05-26 14:26:44

[config]
.> app:         tasks:0x7f77c121a518
.> transport:   redis://localhost:6379//
.> results:     redis://localhost/
.> concurrency: 10 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . tasks.add

[2022-05-26 14:26:45,241: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
[2022-05-26 14:26:45,242: INFO/MainProcess] Connected to redis://localhost:6379//
[2022-05-26 14:26:45,250: INFO/MainProcess] mingle: searching for neighbors
[2022-05-26 14:26:45,256: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
[2022-05-26 14:26:46,266: INFO/MainProcess] mingle: all alone
[2022-05-26 14:26:46,274: INFO/MainProcess] celery@blabla.local ready.
```


```shell
from tasks import add
result = add.delay(1, 10000000)
result.ready() # True
result.get() # 결과 반환
```


```shell
[2022-05-26 14:27:05,451: INFO/MainProcess] Task tasks.add[9761699a-0ff2-429a-86cf-ccec774d3744] received
[2022-05-26 14:27:05,933: INFO/ForkPoolWorker-8] Task tasks.add[9761699a-0ff2-429a-86cf-ccec774d3744] succeeded in 0.4757317079929635s: 10000001
```