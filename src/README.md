I am using Python with Flask for simplicity. Flask is lightweight, easy to set up, and has a good ecosystem for handling HTTP requests and JSON responses
app.py will ceate two endpoints: /bitcoin and /ethereum, both of which will fetch real-time prices from a public API like CoinGecko
I installed "pip install -r requirements.txt" in the project directory
I also installed Docker in the project environment

Technology Stack

- Python 3.10
- Flask 2.2.2
- requests 2.28.1
- Docker 20.10

After running the container I got an error with the flask version, therefore I did the following:
Upgrade Flask


bash
pip install Flask==2.3.0


Or, in your requirements.txt:


Flask==2.3.0
requests==2.28.1


Then rebuild your Docker image:
# build docker image:
docker build -t crypto-service .

# run docker container
docker run -p 5000:5000 crypto-service



# To tes the ethereum price
http://localhost:5000/ethereum

#To test the bitcoin price
http://localhost:5000/bitcoin


