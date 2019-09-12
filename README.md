### AIS-media-extractor

A REST API server for getting the info for videos from different sites, powered by [youtube-dl](http://rg3.github.io/youtube-dl/) and [youtube-dl-api-server](https://youtube-dl-api-server.readthedocs.io/)


### Download the source code

```
git clone https://github.com/sviete/AIS-media-extractor
```

### Install
go to the AIS-media-extractor foleder and install the dependecies with

```
pip install -r requirements.txt --user
```


### Run

```
python -m ais_media_extractor
```

### PM2

```
pm2 start "python -m ais_media_extractor --host <SERVER_IP> -p 9191" --name YouTubeDL
```

### API

- version
```
http://localhost:9191/api/version
```

- extractions
```
http://localhost:9191/api/extractors
```

- play
```
http://localhost:9191/api/play?url=http://www.ted.com/talks/dan_dennett_on_our_consciousness.html
```
