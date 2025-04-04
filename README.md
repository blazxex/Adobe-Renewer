CU Adobe Auto Renewer (Dockerized for Synology NAS)
===================================================

This Docker container automates the renewal of your CU Adobe access by logging in with your credentials via a headless browser..

Features
--------

- Automates CU Adobe renewal with Python + Selenium
- Runs headless Chromium in a lightweight container
- Supports Synology NAS Docker
- Secure credential management with `config.json`

Prerequisites
-------------

- Docker installed (e.g., via Synology Docker package)
- CU Adobe username and password

Setup
-----

1. Create a ``config.json`` file in the root directory with the following format::

    {
      "username": "your_cu_username",
      "password": "your_cu_password"
    }


2. Build the Docker image::

    docker build -t cu-adobe-renewer .

3. Run the container::

    docker run -it --rm \
      -v $(pwd)/config.json:/app/config.json \
      cu-adobe-renewer

   On Synology Docker GUI:

   - Mount `config.json` into `/app/config.json`
   - Set **Execution Command** to::

       python it_renewer.py

File Structure
--------------

::

    .
    ├── Dockerfile
    ├── requirements.txt
    ├── config.json         
    ├── it_renewer.py       
    └── README.rst         

Sample requirements.txt
------------------------

Your `requirements.txt` should contain at least::

    selenium
    

Recommendation
--------------

Use **Synology Task Scheduler** or `cron` to automate the container run weekly or monthly.

