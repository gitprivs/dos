cd /etc/yum.repos.d/
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
cd
yum -y install java
yum install epel-release -y
yum install nodejs -y
yum install golang -y
yum install python3 -y
yum install npm -y
pip3 install requests colorama

npm i axios
npm i user-agents 
npm i header-generator 
npm i cloudscraper 
npm i set-cookie-parser 
npm i colors 
npm i readline-sync
npm i random-useragent 
npm i cheerio gradient-string 
npm i fake-useragent 
npm i request 
npm i randomstring
npm i puppeteer
npm i puppeteer-extra 
npm i puppeteer-extra-plugin-stealth
npm i async
cd ham
python3 main.py
