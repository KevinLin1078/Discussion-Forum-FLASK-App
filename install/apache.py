import os
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
sys.path.append('/usr/local/lib/python2.7/site-packages/')

arr =[
        'sudo apt-get update',
        'sudo apt-get install -y apache2',
        'sudo ufw app list',
        'sudo ufw enable',
        "sudo ufw allow 'Apache Full'",
        "sudo systemctl status apache2",
        "sudo ufw allow 'OpenSSH'",
        "sudo apt-get install curl",
        "curl -4 icanhazip.com"
    ]   




for i in arr:
    os.system(i)
    #sudo systemctl restart apache2
