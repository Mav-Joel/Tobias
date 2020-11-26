mysql -u Python -p$MDP -D tobiasdb -e CREATE USER 'tobias'@'10.96.26.197/24' IDENTIFIED BY 'BladeDBfromTobias';
mysql -u Python -p$MDP -D tobiasdb -e GRANT ALL ON `tobiasdb`.* TO'tobias'@'10.96.26.197';
mysql -u Python -p$MDP -D tobiasdb -e FLUSH PRIVILEGES;
