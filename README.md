# Live Stream Live

This repository contains the source material for my OSCON 2019 presentation, "Live Streams Live". This presentation
walks through getting up and running with gRPC streaming.

## Install dependencies

You'll need Python 3.7 for the backend portion of this talk. To get setup with Python 3's builtin venv support, you can do the following.
(`make setup` is provided for convenience)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You'll need nodejs installed for the frontend portion (`v12.4.0` was used to prepare this talk).

## Getting Started

First, we'll need a virtualenv
