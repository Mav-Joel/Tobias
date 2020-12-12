sudo cp -R ~/Archetype/Tobi/* ~/Git/
sudo rm -R ~/Git/Locker
sudo rm -R ~/Git/Mavker
sudo rm -R ~/Git/Nginx
sudo chmod ugo+rwx ./*/*
cd ~/Git && git add .
git commit -m "test"
git push -u joel master