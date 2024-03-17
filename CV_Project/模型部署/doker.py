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
  3、打开微软商城，下载ubantu 20.04.LTS
  4、重新打开docker，按照老师的教程安装

  docker run -it -v d:/dockerv:/localfiles -p 8088:8080 -p 22:22 ubuntu:20.04

'''
'''
docker -v
docker images
docker run -it ubuntu:20.04  启动一个镜像得到一个容器
exit  从root退出
docker run -it -v e:/ceshi:/localfiles -p 22:22 ubuntu:20.04 创建一个容器，并把本地文件移进去

cd /localfiles/ 进入这个文件
cd  退出这个文件

docker rename clever_snyder mycontainer  修改容器名称
docker ps命令来查看正在运行的容器列表
docker exec -it 2059296427ac /bin/bash 进入到容器

apt update
apt install vim -y


'''
'''
配置容器步骤：
1、  docker run -it --name test1 --gpus all -v d:/dockerv1:/localfiles1 -p 22:22 -p 8080:8080 ubuntu:20.04  创建带有端口号的容器
exit----退出

2、 docker ps -a  查看所有容器
3、docker start 56298c4f4d13 启动这个容器
4、docker exec -it 56298c4f4d13 /bin/bash  进入到容器
2、 apt update  更新

3、 apt install vim -y      安装vim，vim可以打开多个客户端（powershell）
4、vim /etc/apt/sources.list  替换成下面的镜像路径

deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

5、apt update

6、apt install openssh-server -y  安装端口号
7、vim /etc/ssh/sshd_config  
找到#PermitRootLogin prohibit-password这一样，在下面新添一行PermitRootLogin yes，如下
#PermitRootLogin prohibit-password
PermitRootLogin yes
8、service ssh restart
9、passwd  设置密码--一般写root
10、service ssh status  
'''

'''
linex命令：
ps -ef 显示进程
'''
'''
docker命令：
dockers ps 显示正在running的容器
docker ps -a 显示所有的容器
docker commit 56298c4f4d13 my_ubuntu2004_sshserver:v1  容器保存成一个镜像
docker run -it -v d:/dockerv:/localfiles -p 80:8080 -p 22:22 --name mywebserver my_ubuntu2004_sshserver:v1   web镜像
'''