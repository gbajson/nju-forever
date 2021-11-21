# nju-forever
Simple script to keep alive nju mobile account

Script does use 'mailx' client to set up emails.
Sample configuration of SMTP and email client:
https://gist.github.com/gbajson/88d179499136dc5945f5a13fd6a8b9ff


1. Install requirements
```
git clone https://github.com/gbajson/nju-forever.git
cd nju-forever
pip install -r requirements.txt
```

2. Add your additionl phone number to .bash_profile
```
pi@raspberrypi:~ $ cat .bash_profile
EMAIL="your@email.address.to.receive.notifications"
export PHONE
```

3. Setup your cron
```
0 */6 * * * (. $HOME/.bash_profile; date; /home/pi/py3.7.3/bin/python nju-forever/nju_forever.py) >> /var/tmp/sms.log 2>&1

```
