# hse-hw-backend

Start up
```commandline
bash -i run.sh
```

Test your request 
```commandline
curl -X 'GET' 'http://127.0.0.1:5050/generate_and_summarize/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "prompt": "I love you"
}'
```