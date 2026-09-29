# UniBoard PoC
Demonstrates one end-to-end Assignment 1 interface contract.

Run:
cd poc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend:app --reload

Open http://127.0.0.1:8000.
Demo: enter a post, choose University, create it, show the result and HTTP 201, then demonstrate invalid input.

Simplifications: no real authentication, React, PostgreSQL, WebSockets or LLM. These are Assignment 2 targets. Fictional u_demo is used. No secrets or paid API.