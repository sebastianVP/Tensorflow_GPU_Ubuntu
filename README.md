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
