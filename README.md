# Minnal-Blockchain

A basic blockchain implementation in Python. "Minnal" means "lightning" in Tamil.

This project implements the core mechanics of a blockchain from scratch and exposes them through a small Flask HTTP API, so multiple nodes can run, mine, transact, and reach consensus over the network.

## Features

- SHA-256 block hashing with a genesis block
- Proof of Work mining (find a proof such that `hash(last_proof + proof)` starts with `0000`)
- Transactions (sender, recipient, amount) batched into the next mined block
- Mining reward credited to the node identifier
- Multi-node support with node registration
- Consensus algorithm: longest valid chain wins, fetched from peer nodes
- Flask REST API for interacting with the chain

## Tech Stack

- Python
- Flask (HTTP API)
- requests (peer-to-peer chain fetching)
- hashlib / json / uuid (standard library)

## Getting Started

### Prerequisites

- Python 3
- pip

### Install

```bash
pip install Flask==0.12.2 requests==2.18.4
```

### Run a node

```bash
python app.py
```

The node listens on `http://0.0.0.0:5000` by default. To run multiple nodes locally, start additional instances on different ports (edit the `app.run(...)` call or run `appmachine2.py`).

## API Endpoints

| Method | Endpoint            | Description                                          |
|--------|---------------------|------------------------------------------------------|
| GET    | `/mine`             | Run Proof of Work, forge a new block, get a reward   |
| POST   | `/transactions/new` | Add a new transaction (`sender`, `recipient`, `amount`) |
| GET    | `/chain`            | Return the full chain and its length                 |
| POST   | `/nodes/register`   | Register peer nodes (`nodes`: list of addresses)     |
| GET    | `/nodes/resolve`    | Run the consensus algorithm against registered peers |

## Project Structure

- `blockchain.py` — Core `Blockchain` class (blocks, transactions, PoW, consensus)
- `app.py` — Flask HTTP API exposing the blockchain
- `appmachine2.py` — Second node instance for testing multi-node consensus
- `requirements` — Python dependencies
