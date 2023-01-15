# 安装依赖
本demo需要`pydirectinput`,`pypiwin32`依赖请自行安装。
# 如何运行
注：__需要管理员权限__
方法很多上网搜有很多
这里提一个方法，进入cmd.exe的目录，一般在`C:\Windows\System32\cmd.exe`，右键已管理员运行。
然后`cd`到该文件夹下。执行`pytyon demo.py`，前提是`python`已经添加到环境变量了。
# YsMusicalInstruments类的使用
请直接看demo.py里的例子
``` python
y = YsMusicalInstruments(133,majorTremoloHarmonicaGamut)
y.addNote([8],["1","1."])
y.addNote([8],["3."])
y.addNote([8],["1","5."])
y.addNote([8],["3."])
y.play()
```
