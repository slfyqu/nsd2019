# nsd1902_devweb_day03

web框架：django / flask / tornado

## MTV

- M: Model 数据库
- T: Template 模板，网页
- V: View 视图，函数

```mermaid
graph LR
c(client)
s(server)
url(URLConf路由系统)
v(Views视图)
m(Model模型)
t(Template模板)
c --访问-->s
s --查询-->url
url --调用函数-->v
v --操作db-->m
m --返回数据-->v
v --发送到-->t
t --返回页面-->c
```

## django

### 安装

```python
[root@room8pc16 day03]# source ~/nsd1902/bin/activate
(nsd1902) [root@room8pc16 zzg_pypkgs]# pip3 install dj_pkgs/*
# 或在线安装
(nsd1902) [root@room8pc16 zzg_pypkgs]# pip3 install django==1.11.6
```

### 项目管理

什么是项目：一个django网站就是一个django项目。项目由配置和应用构成。

创建项目的方式：

- 使用django-admin命令

```shell
(nsd1902) [root@room8pc16 day03]# django-admin startproject mypro
(nsd1902) [root@room8pc16 day03]# ls
mypro  
```












