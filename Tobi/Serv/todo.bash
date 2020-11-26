sudo apt-get install nginx
CREATE USER 'Python'@'localhost' IDENTIFIED BY 'GrpAmPMaverick&';
GRANT ALL PRIVILEGES ON * . * TO 'Python'@'localhost';
FLUSH PRIVILEGES;
pip3 install PyQt5
sudo apt-get install python3-pip python3-dev  
sudo apt-get install git
git config --global user.name "joel"
git config --global user.email "joel.toula@gmail.com"
git remote add origin SSH git@github.com:Mav-Joel/projet.git
git branch -M main
git push -u origin main --verbose