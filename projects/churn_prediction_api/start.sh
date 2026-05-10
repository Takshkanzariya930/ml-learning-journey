#!/bin/bash

uvicorn app.app:app --host 127.0.0.1 --port 8000 &

streamlit run frontend.py \
  --server.port $PORT \
  --server.address 0.0.0.0