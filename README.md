# How to run project

To install dependencies
```
pip install -r requirements.txt
```
To run application in development mode
```
fastapi dev main.py
```
To run application in production
```
fastapi run main.py
```
To read documentation go to http://127.0.0.1:8000/docs

# How to configure systemd service

```
$ sudo nano /etc/systemd/system/prediction-service.service
```
In this new file we have to put the following:
```
[Unit]
Description=My simple prediction service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=vampyrian
ExecStart=/bin/bash -c 'cd /home/vampyrian/App && source .venv/bin/activate && fastapi run --workers 4 main.py'

[Install]
WantedBy=multi-user.target
```
To reload systemd settings
```
sudo systemctl daemon-reload
```
To run service
```
sudo systemctl enable myapp.service
sudo systemctl start myapp.service
sudo systemctl status myapp.service
```

# How to configure SSL Caddy server
Install caddy server
```
caddy adapt
caddy start
```