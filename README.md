# pendler-statistik

Simpel service til at opsamle statistik for tog-afgange for Hedehusene station

Udviklet til at køre under [Google App Engine](https://cloud.google.com/appengine)


### Lokalt udviklingsmiljø

Kræver:
* Python 3
* Google Cloud SDK (hvis deploy til Google App Engine)

Python virtuelt miljø:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Kør webserver lokalt:
```
python main.py
```

Du kan nu åbne http://localhost:8080/trains i browser


### Deploy til Google App Engine

```
gcloud deploy
gcloud app browse
```


### Credits

Tak til https://github.com/ParmoDev for første version af koden :)
