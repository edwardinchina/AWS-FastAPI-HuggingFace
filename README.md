# AWS-FastAPI-HuggingFace

1. Clone this repo.

2. From the repo's route directory run the following to build the container from the image:
```
docker build -t awsa
```

3. Next run the container with port 8000 mapped to 8000:
```
docker run -p 8000:8000 aws-fastapi-huggingface
```

4. Visit localhost:8000/docs
5. Click POST next to /my-endpoint
6. Click "Try it out"
7. Change the value of query string
```
{
  "query_string": "change this"
}
```
8. Press Execute to see the result. The sentiment of your input will be labeled either POSTIVE or NEGATIVE.
