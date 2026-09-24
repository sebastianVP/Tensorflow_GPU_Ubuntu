**INSTALACION DE TENSOR FLOW 2.12 CON SOPORTE PARA GPU EN UBUNTU 22.04**

El objetivo de esta guia es proporcinar los pasos del proceso de instalacion de TensorFLow
con soporte para GPU en Ubuntu22.04. Siguiendo estos pasos , podras **ejecutar modelos de TensorFLow en Python**
utilizando tu GPU RTX. Estas son las bibliotecas y versiones requeridas:

- TensorFlow 2.19
- cuDNN 8.9.1
- CUDA Toolkit 12.8
- Controlador NVIDIA(instalado junto con el toolkit)

**Paso 1: Eliminar cualquier instalacion previa de Nvidia**

Abrimos un terminal y ejecutamos los siguientes comandos:
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt-get remove --purge '^nvidia-.*'
$ sudo apt-get autoremove
```
** Paso 2: Desactivar el controlador Nouveau Nvidia**

A) Arbimos el archivo de lista negra(balcklisted) con nano

```
sudo nano /etc/modprobe.d/blacklist-nvidia-nouveau.conf
```

B) Insetar las siguientes lineas en el archivo:
```
blacklist nouveau
options nouveau modeset=0
```
C) Guarda el archivo y sal del editor

D) Regenera el kernel initramfs:

```
sudo update-initramfs -u
```

**Paso 3: Verificar la informacion de la tarjeta grafica**
En la terminal, ejecuta el siguiente comando para verificar que tu GPU sea detectada:

```
sudo lshw -C display
```

**Paso 4: Instalar el controlador Nvidia y el CUDA Toolkit**

Vamos al link siguiente: [CUDA Toolkit Installer](https://developer.nvidia.com/cuda-downloads)

![CUDA Toolkit Installer](/Imagenes/toolkit.png)

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.8.1/local_installers/cuda-repo-ubuntu2204-12-8-local_12.8.1-570.124.06-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-8-local_12.8.1-570.124.06-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-8
```
