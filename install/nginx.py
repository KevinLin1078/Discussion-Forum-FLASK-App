import os


arr =[  'sudo apt-get update', 'sudo apt-get install -y nginx',
		'sudo ufw enable', "sudo ufw allow 'Nginx HTTP'",'systemctl status nginx',
		'sudo apt-get install curl', 'curl -4 icanhazip.com'
	]

for i in arr:
	os.system(i);

