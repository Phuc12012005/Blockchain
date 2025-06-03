FROM ubuntu:latest

RUN apt update
RUN apt install -y build-essential libssl-dev

WORKDIR /app
COPY . .

RUN g++ -std=c++11 blockchain.cpp -o blockchain -lcrypto

