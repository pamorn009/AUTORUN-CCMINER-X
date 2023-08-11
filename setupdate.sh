#!/bin/sh


chmod +x edit-miner
chmod +x run-miner
chmod +x add-ip
chmod +x update


mv mobile-mining ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin
mv update ../../bin


run-miner


cd && cd ../etc/mobile-mining/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

chmod +x ccminer

run-miner
