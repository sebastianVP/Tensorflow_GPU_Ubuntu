**INSTALACION DE TENSOR FLOW 2.12 CON SOPORTE PARA GPU EN UBUNTU 22.04**

El objetivo de esta guia es proporcinar los pasos del proceso de instalacion de TensorFLow
con soporte para GPU en Ubuntu22.04. Siguiendo estos pasos , podras **ejecutar modelos de TensorFLow en Python**
utilizando tu GPU RTX. Estas son las bibliotecas y versiones requeridas:

- TensorFlow 2.12
- cuDNN 8.9.1
- CUDA Toolkit 11.8
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
