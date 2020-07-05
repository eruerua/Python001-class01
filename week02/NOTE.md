学习笔记

本周学习过程中遇到的问题主要有：

1. windows系统下，mysql启动失败，报InnoDB: .\ibdata1 must be writable错误，以管理员身份启动同样失败，解决方法如下：1、打开任务管理器终止mysqld进程；2、打开mysql安装目录的data文件夹，删除以下2个文件：`ib_logfile0`和`ib_logfile1`3、重新启动mysql。
2. mysql 报错ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executin, 修改用户密码mysql> alter user 'root'@'localhost' identified by 'youpassword';  
3. Tesseract安装，安装后需要添加2个环境变量：把安装路径“C:\Program Files (x86)\Tesseract-OCR”添加到环境变量里，方便在命令行里直接调用；把语言包所在路径“C:\Program Files (x86)\Tesseract-OCR\tessdata”添加到环境变量里，变量名称为“TESSDATA_PREFIX”，不添加语言包路径的话调用tesseract识别会报错误。
4. vs code终端命令不能使用，以管理员身份运行vs code.