##################
## cuda 10.0
## cudnn 10.0
##################

# 安装 NVIDIA 驱动
[NVIDIA 驱动下载] (https://www.nvidia.cn/Download/index.aspx?lang=cn)

```
NVIDIA Geforce GTX 1660 Ti
```

```
Ctrl+Alt+F1
```

### 关闭 X server ：

```
# (1) gdm类型的桌面系统
sudo /etc/init.d/gdm stop
sudo /etc/init.d/gdm status

# (2) light类型的桌面系统
sudo /etc/init.d/lightdm stop
sudo /etc/init.d/lightdm status
```


```
sudo init 3
sudo ./your-nvidia-file.run
```

```
nvidia-smi
nvidia-settings 
```
[CUDA Download] (https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal)

```
sudo dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
ip a
sudo dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```

[cuDNN Download](https://developer.nvidia.com/rdp/cudnn-download)

```
sudo dpkg -i libcudnn7_7.6.0.64-1+cuda10.0_amd64.deb 
```
