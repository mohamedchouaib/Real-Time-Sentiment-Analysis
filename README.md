# Real-Time-Sentiment-Analysis
## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What You'll Learn](#what-youll-learn)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Watch the Video Tutorial](#watch-the-video-tutorial)

## Introduction
This project serves to build an end-to-end data engineering pipeline using TCP/IP Socket, Apache Spark, Kafka, and Elasticsearch. It covers each stage, from data acquisition and processing, sentiment analysis with ChatGPT, to producing Kafka topics and connecting to Elasticsearch.

## System Architecture
![System Architecture]
![architecture](https://github.com/user-attachments/assets/82d79237-1e2d-4352-8761-08d930f69632)

The project is designed with the following components:
- **Data Source**: Uses Yelp dataset for the data pipeline.
- **TCP/IP Socket**: Streams data over the network in chunks.
- **Apache Spark**: Handles data processing with master and worker nodes.
- **Confluent Kafka**: Provides cloud-based Kafka clusters.
- **Control Center and Schema Registry**: Monitors and manages schemas for Kafka streams.
- **Kafka Connect**: Connects Kafka to Elasticsearch.
- **Elasticsearch**: Used for indexing and querying data.

## Technologies
- **Python**
- **TCP/IP**
- **Confluent Kafka**
- **Apache Spark**
- **Docker**
- **Elasticsearch**

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/airscholar/E2EDataEngineering.git
    ```

3. **Run Docker Compose to spin up the Spark cluster**:
    ```bash
    docker-compose up
    ```
