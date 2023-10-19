#!/bin/bash

cd text_generation && uvicorn app:app --port=5048 --reload & disown

cd summarization && uvicorn app:app --port=5049 --reload & disown

cd external_api && uvicorn app:app --port=5050 --reload