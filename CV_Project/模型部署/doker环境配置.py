# 0、初始docker
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

  4、重新打开docker，按照老师的教程安装
'''

# 1、安装vim文件编辑器
'''
apt update
apt install vim -y
apt update
'''

# 2、配置ssh容器步骤：
'''
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

# 3、配置tomcat，看视频及课件
# 4、安装编译环境，make配置
'''
apt install g++ gcc make cmake 

vim main.cpp:

#include <iostream>
using namespace std;
extern int add(int,int);
extern int substract(int,int);
int main(){
        cout<<"hello"<<endl;
        int a=90;
        int b=10;
        cout<<add(a,b)<<","<<substract(a,b)<<endl;
        return 0;
}

vim functions.cpp:

int add(int a,int b){
        return a+b;
}
int substract(int a,int b){
        return a-b;
}

vim makefile:

GCC = g++
CFLAGS = -Wall
all: program
program: main.o functions.o
        $(GCC) $(CFLAGS) -o program main.o functions.o
main.o: main.cpp
        $(GCC) $(CFLAGS) -c main.cpp
functions.o: functions.cpp
        $(GCC) $(CFLAGS) -c functions.cpp
clean:
        rm -f *.o program
        
cat makefile 本界面查看文件内容

vim ~/.bashrc  打开配置文件，改成如下：
export PATH=$JAVA_HOME/bin:$CATALINA_HOME/bin:.:$PATH

source ~/.bashrc  更新配置
make /make all

touch main.cpp 没有mian.cpp文件就创建，有就更新
make clean  #rm -f *.o program 删除所有的.o文件和program ,除了clean可以创建多个命令
cp makefile makefile1  拷贝另外一个make文件
make -f makefile1  和makefile一样的效果
'''
# 5、安装编译环境，cmake配置
'''
#cmake配置：
mkdir demo  创建demo文件夹
cd demo

vim add.cpp:
#include <stdio.h>
#include "head.h"
int add(int a,int b){
        return a+b;
}

vim sub.cpp:
#include <stdio.h>
#include "head.h"
int sub(int a,int b){
        return a-b;
}

vim main.cpp:
#include <stdio.h>
#include "head.h"

int main(){
        int a=20;
        int b=12;
        printf("a=%d,b=%d\n",a,b);
        printf("a+b=%d\n",add(a,b));
        printf("a-b=%d\n",sub(a,b));
        return 0;
}

vim head.h:
#ifndef _HEAD_H
#define _HEAD_H

int add(int a, int b);
int sub(int a, int b);

#endif

# g++ *.cpp -o app 一条命令生成可执行文件，一般用cmake生成可执行程序方法如下：

vim CMakeLists.txt  创建文件：


# specify the minimum cmake version
cmake_minimum_required(VERSION 3.10)        
# set the project name
project(CALC)

set(CMAKE_CXX_STANDARD 14)                # 指定版本   

set(SRC_LIST main.cpp;add.cpp;sub.cpp)    # 宏替代

set(HOME /root)
set(EXECUTABLE_OUTPUT_PATH ${HOME}/bin)   # 生产的app所在路径

# add the executable
add_executable(app ${SRC_LIST})


mkdir build   编译好的文件放在build
cd build
cmake ..  #.表示CMakeLists.txt 文件所在路径 此时生成Makefile文件
make  #再make（用的就是Makefile文件），就生成可执行文件app  #当app main.cpp add.cpp sub.cpp发生改变就要cmake
cd .. 返回上一级目录

mkdir src
mv *.cpp src   所有的待编译文件放在src文件夹
mv *.h src
'''
# 6、apt安装opencv
'''
docker exec -it deb9db6ea3fe /bin/bash  进入到容器
apt update
apt install python3-opencv 安装opencv的python库
apt update
apt install libopencv-dev -y  安装opencv的c++库
find / -name opencv4.pc 查看文件是否在 /usr/lib/x86_64-linux-gnu/pkgconfig 文件夹下。
pkg-config --cflags --libs opencv4  查看里面包含的头文件和库文件

CMakeLists.txt文件示例如下：
cmake_minimum_required(VERSION 3.0)
project(TEST)
file(GLOB SRC_LIST ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(app ${SRC_LIST})
target_link_libraries(app ${OpenCV_LIBS})                                                                                                                ~                                          

'''
