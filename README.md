# Learn the hard way - FastAPI

Run locally
```
curl -X POST -H 'Content-Type: application/json' -d '{"text": "Everything is practice.", "author": "Pele"}' http://localhost:8000/quotes

curl http://localhost:8000

```

Deploy to onrender.com
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"text": "Everything is practice.", "author": "Pele"}' http://lthwfastapi.onrender.com/quotes

curl -X POST -H 'Content-Type: application/json' -d '{"text": "You are what you practice most.", "author": "Richard Carlson"}' http://lthwfastapi.onrender.com/quotes
```