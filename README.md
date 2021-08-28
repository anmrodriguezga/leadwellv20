# Control remoto centro de mecanizado Leadwellv20
---

Este proyecto busca conectar a la red al centro de mecanizado Leadwellv20 ubicado en el laboratorio Sala CAM de la Universidad Nacional de Colombia.

Para este procedimiento, y debido a que la máquina no cuenta con un dispositivo o tarjeta de red que le permita conectarse a Internet, se debe utilizar [visión artificial](https://es.wikipedia.org/wiki/Visi%C3%B3n_artificial).

## Requerimientos de hardware

Dado que el sistema está pensado para correr en un servidor en la nube, el usuario no necesita más que un computador con conexión a Internet. Sin embargo, también puede ser utilizado de manera local con un computador con las siguientes especificaciones **mínimas**:

- Procesador: Intel Core i3 4° generación
- RAM: 4 GB
- Se recomienda contar con SSD
- Tarjeta gráfica dedicada

## Requerimientos de software
#### Sistema Operativo
- Linux (local o server)
  - Ubuntu 20.04 LTS

- Windows
  - Windows 10 Home/Pro
  - Soporte para [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

#### Programas

Las aplicaciones utilizadas están optimizadas para funcionar en Ubuntu 20.04, por lo cual es posible utilizar WSL y una imagen de Ubuntu. Los siguientes son los programas requeridos para el funcionamiento del software:

- Robot Operating System (ROS) Noetic
- Rviz
- Gazebo
- Python 3.8
- OpenCV
- Google API Vision[^1]

[^1]: El API de visión de Google se utiliza para procesar video en tiempo real. Se puede reemplazar por un script de visión personalizado.

## Instalación

En este instructivo se detallarán los pasos para la instalación y puesta a punto del software en un servidor en la nube. Para este caso se utilizará Google Cloud Platform, pero cualquier servicio en la nube puede ser utilizado para este mismo fin.

