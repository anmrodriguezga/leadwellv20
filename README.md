# Leadwell v20

Control y supervisión gemelo digital Leadwell v20 LabFabEx Universidad Nacional de Colombia.

Descripción del gemelo virtual controlado a través de conexión ROS - MATLAB - Gazebo.

## Requisitos mínimos del sistema:

* Computador con sistema operativo Windows 10 compilación 1909.
* MATLAB R2015b con Robotics System Toolbox.
* Cimco Edit 8.
* Windows Subsystem for Linux (WSL1).
  * Ubuntu 18.04.
  * Robotic Operating System (ROS) versión Melodic.
  * Rviz
  * Gazebo
* XServer para Windows (preferiblemente VcXsrv).


## Procedimiento:
1. Clonar repositorio, de la siguiente manera:\
  1.1. La carpeta cnc_windows se debe copiar a la carpeta C:\Users\USER_NAME\Documents\MATLAB.\
  1.2. En un bash de Ubuntu, crear el [workspace para catkin](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) y copiar la carpeta leadwellV20 en ~/catkin_ws/src.
2. Desde Windows, ejecutar las configuraciones por defecto del VcXsrv.
3. Ejecutar la aplicación **GUI.mlapp** para poder observar la interfaz gráfica de control.
4. Desde el bash, ejecutar el siguiente comando\
    `roslaunch leadwellV20 spawn.launch`\
   para ejecutar el gemelo virtual en Gazebo.
