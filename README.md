# 树莓派FM广播~~点歌系统~~

这是一个不错的项目，不过因为时间长了，大部分代码已经失效。

提了issue之后原作者删除了关于根据歌名，自动前往搜狗提取直链的代码。

只保留了通过访问 http://0.0.0.0:8080 **自行输入音乐链接**

然而……web服务器似乎仍然有一些问题，比如在输入音乐链接后cpu飙到100%，无法播放音乐等一系列问题……

so……~笔者删除了关于web服务器方面的的所有代码~(还是没删，只是在start.sh里更改了引导)，使它只能根据list.py的歌单播放本地音乐。

先使用setup.sh安装依赖再使用start.sh启动fm即可～

音乐文件在list.py中修改目录和mp3文件名称。

### 简介

前段时间有人发贴说用树莓派可以发射FM收音机信号，
于是便整来玩玩，发现效果还不错，于是想扩充一下功能。

网上实现的FM发射功能是有局限性的：

- 只能播放wav格式文件，并且wav文件必须是`16 bit 22.5kHz Mono`格式的。
- 只支持播放本地音频文件，或者使用`-`从终端读取音频

我设想的或已经实现的功能是这样的：

- 支持mp3格式
- 支持流媒体，或者说支持直接播放网络上的音乐
- 可以播放局域网内电脑上的音乐
- 有一个web页面，允许任何人添加自己喜欢的歌曲

安装我做的系统之后你就可以用树莓派做服务器，
发送广播，播放流行歌曲或者英语听力（或者法律允许播放的东西）
告诉亲朋好友一个网址，然后他们就能在上面点歌。
四六级没过的朋友可以添加四六级听力，模拟真实考试环境。
或者放到敬老院里面，给老年人播放戏曲。

### 关键技术与原理

因为树莓派只支持wav格式音乐，所以要将mp3格式转换成wav格式。

但是一般软件转换效率比较低，树莓派CPU比较差，转换时间更长。

后来我找到一个比较好的解决方案，用mpg123这个软件进行解码，
解码之后输出到终端上，这时就已经转换成wav格式了。
然后树莓派的pifm程序设置成从终端读取音频，
这样再通过一个管道将两个程序连起来，就能实现一边解码一边播放

另外，mpg123的功能比较强，支持直接播放网络音乐，
也就是说，只要给mpg123传递一个歌曲url，就能实现边下载边播放

上面的文字用一条命令总结就是：

```shell
mpg123 -m -C -q -s 歌曲地址或url | sudo pifm - 频率 歌曲采样率
例如
mpg123 -m -C -q -s /home/pi/aaa.mp3 | sudo pifm - 98.5 44100
mpg123 -m -C -q -s http://abc.com/123.mp3 | sudo pifm - 98.5 44100
```

上面的命令看起来很简单，费了半天劲才鼓捣好，因为命令的参数很多，
组合起来让他们协调工作就需要不断尝试！

解决了这个技术难题，下面的任务就简单了，对于pythoner来说，
下面提到的东西都不叫事！`^_^`

### 安装部署方法

为了简化安装部署，我专门写了一个安装脚本，就是setup.sh，
直接执行就能安装。（注意，本系统树莓派专用，请不要在电脑上执行此脚本）
```shell
wget https://github.com/kirainl/fmpi/archive/master.zip
unzip master.zip
cd fmpi-master
sudo bash setup.sh
```
这样就自动安装依赖的软件

### 使用方法

运行的话可以直接执行程序里面的`start.sh`:

```bash
bash start.sh
```

然后在树莓派的GPIO4这个引脚上插上一根杜邦线当天线

用`ifconfig`命令察看你的ip地址，然后在浏览器上打开：`http://树莓派IP:8000/`，
可以看到正在播放的歌曲，然后你可以添加你想要收听的歌曲。

打开收音机，调到`FM 98.5`频道，你就能听到正在播放的歌曲了！

想终止程序的话按`Ctrl + c`

可以修改config.py修改默认的98.5这个播放频率。

### 其他

对本系统感兴趣的话可以去github上查看源码，扩充系统功能：
`https://github.com/kirainl/fmpi`
