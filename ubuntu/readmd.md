

#安装 usb串口 pl2301 ch341 驱动

ubuntu 18.04 默认已安装


#安装 peak-can 驱动

https://www.peak-system.com/Support.55.0.html?&L=1

### ubuntu 18.04 desktop

```sh
	wget https://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-8.8.0.tar.gz
	tar xzvf peak-linux-driver-8.8.0.tar.gz
	cd peak-linux-driver-8.8.0

	sudo apt-get install libpopt-dev
        make -j4
        sudo make install
```
