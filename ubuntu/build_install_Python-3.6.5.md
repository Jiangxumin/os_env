# install libssl-dev


```
sudo apt-get install  libssl-dev 
sudo apt-get install  python3-pip 

# 解压 python 3.6
./configure --prefix-dir=/usr/local
make -j6
sudo make install
```
# pip3.6
# python3.6

* pip install  报错 , 需要安装libssl-dev
```
Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)':
```
