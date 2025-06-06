# Simple Blockchain in C++

This project is a basic simulation of a blockchain implemented in C++.

## Features

- Add and store transactions
- Mine blocks using a simple Proof-of-Work algorithm
- Validate blockchain integrity
- Maintain balances for each wallet
- Display and traverse the entire blockchain
- Reward miners with a system-generated transaction

## Requirements

- C++11 or newer
- OpenSSL (for SHA256 hashing)

## How to run the program
### Clone the repo
```
git clone https://github.com/Phuc12012005/Blockchain.git
```
### Install dependencies (Ubuntu)
```bash
sudo apt update
sudo apt install build-essential libssl-dev
```

### Build the program
```
g++ -std=c++11 blockchain.cpp -o blockchain -lcrypto
```

### Executing
```
./blockchain
```
