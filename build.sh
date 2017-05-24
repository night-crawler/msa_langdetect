#!/usr/bin/env bash

docker build -t docker.force.fm/ncrawler/msa_langdetect:latest \
             -t docker.force.fm/ncrawler/msa_langdetect:0.0.1 \
             -t ncrawler/msa_langdetect:latest \
             -t ncrawler/msa_langdetect:0.0.1 \
             .
