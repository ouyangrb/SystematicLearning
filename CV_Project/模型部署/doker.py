'''
1、安装docker desktop 安装在c盘
2、用windows powershell 执行命令，比如 docker images（查看镜像）
3、docker是一种开源的容器化平台，可将应用程序和依赖包打包到里面的一种可移植性容器
4、docker技术：独立的文件系统和命名空间+Cgroups（control group）对cpu、内存、io、摄像头等控制分配及资源共享
5、docher主要组件：
 1）、docher引擎：当成是服务器，一致打开   powershell当作客户端（客户端可以开启多个，也可以在其他电脑终端开启）
    pwoershell:比如执行命令 docher run -it ubantu:20.04 *启动一个镜像，就得到一个容器 （it 是interactrive terminal 终端交互）
 2）、docher镜像：一个只读的模板，包含了应用程序和依赖项
 3）、docher容器：镜像的运行实例
 4）、docher仓库：用来保管镜像，push把镜像放入仓库，用的时候pull
    比如：dochker pull ubantu:20.04 从官方仓库下载下来，到本地服务区（docher引擎）
    仓库有两种，public（公用的比如阿里的可以申请）private（公司内部的）

6、安装docher: 打开任何东西都以管理员身份
  0、下载安装包：https://www.docker.com/get-started/
  1、https://www.bilibili.com/video/BV1zh411F7wv/?vd_source=71b562c55a1f2434bcb1fbc0d34a66b0 安装教程
  2、出现 docker desktop-unexpected wsl error 解决方法如下：
  右键开始菜单。在桌面左下角开始按钮上右键单击，选择“Windows PowerShell”或“Windows PowerShell (管理员)”来打开PowerShell
  wsl --set-default-version 2
  3、打开微软商城，下载ubantu 20.04.LTS
  4、重新打开docker，按照老师的教程安装

  docker run -it -v d:/dockerv:/localfiles -p 8088:8080 -p 22:22 ubuntu:20.04

'''