# nju-forever
Simple script to keep alive nju mobile account

1. Install requirements
```
git clone https://github.com/gbajson/nju-forever.git
cd nju-forever
pip install -r requirements.txt
```

2. Add your additionl phone number to .bash_profile
```
pi@raspberrypi:~ $ cat .bash_profile
PHONE="+1234567890123"
export PHONE
```

3. Setup your cron
```
0 */6 * * * (. $HOME/.bash_profile; date; /home/pi/py3.7.3/bin/python nju-forever/nju_forever.py) >> /var/tmp/sms.log 2>&1
```
