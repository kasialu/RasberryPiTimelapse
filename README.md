# Raspberry Pi Camera Timelapse

## Run locally

To run the script go to the directory containing the code:
```bash
cd ~/timelapse
``` 
create environment 
```bash
pipenv shell
``` 

and run
```bash
python capture.py
```
to stop the process press ``ctrl+c``

## Service

To enable timelapse script on boot create a service by copying ``timelapse.service`` to
``/lib/systemd/system/timelapse.service``. Enable  and start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable timelapse.service
```

and reboot by

```bash
sudo reboot
```

to check if the service sucessfully started

```bash
systemctl status timelapse
```
