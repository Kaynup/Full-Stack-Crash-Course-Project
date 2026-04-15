# Server
> Server 'server.py' with two endpoints:
- GET: '/status' - to check the status of server
- POST: '/register' - to recieve a json payload and responding with a message

## To run the server
```bash
uvicorn server:app --reload
```

## To check endpoints
> Server Validation with 'server-check.py':
Uses 'request' module to interact with the live endpoints of running server on uvicorn