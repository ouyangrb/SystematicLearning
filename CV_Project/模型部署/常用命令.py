'''
docker -v
docker images
exit  从root退出
cd /localfiles/ 进入这个文件
cd  退出这个文件
dockers ps 显示正在running的容器
docker ps -a 显示所有的容器
docker rename clever_snyder mycontainer  修改容器名称
docker exec -it 2059296427ac /bin/bash 进入到容器
docker commit 56298c4f4d13 my_ubuntu2004_sshserver:v1  容器保存成一个镜像
docker run -it -v d:/dockerv:/localfiles -p 80:8080 -p 22:22 --name mywebserver my_ubuntu2004_sshserver:v1  配置一个容器

ps -ef 显示进程

#export PATH=#PATH:.  用于添加到vim ~/.bashrc , 文件路径后面多了一个.
#修改后要更新 source ~/.bashrc

history 查看历史敲击命令记录

cd ~ 到root下
cd - 到root/bin 下
cd / 到根路径
'''