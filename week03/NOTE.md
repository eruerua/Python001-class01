学习笔记

### 1.解题过程

因为本次作业涉及知识点较多，因此把问题分解为小问题逐个解决。

作业1：编写一个基于多进程或多线程模型的主机扫描器

首先仅仅考虑主机扫描器，参考资料如下：[关于nmap所有的参数](https://blog.csdn.net/SKI_12/article/details/61651960)，[Python之nmap-ping扫描探测主机存活](https://blog.csdn.net/q759451733/article/details/84452586)，[Python 第三方模块pythonnmap来实现高效的端口扫描](https://blog.51cto.com/lvnian/1872995)，使用python-nmap包来进行主机扫描，完成主机扫描器后，使用ThreadPoolExecutor对主机扫描器进行多线程操作。

作业2：拉钩爬虫

拉钩爬虫参考了[拉钩爬虫教程](https://darkless.cn/2019/05/25/lagou-crawl-solution/https://darkless.cn/2019/05/25/lagou-crawl-solution/)，在不使用线程的情况下成功抓取，然后使用ThreadPoolExecutor进行多线程操作，但是在使用map对抓取函数进行操作的时候遇到了传递多个参数的困难，因此参照[将多个参数传递给concurrent.futures.Executor.map](https://www.thinbug.com/q/6785226)解决了这个问题，对抓取到的数据进行处理后，使用[Python操作MySQL数据库](https://www.mscto.com/python/169979.html)介绍的方法将数据写入到数据库

### 2.学习心得

1.学会分解问题，把大问题分解成小问题，不要好高骛远，不要怕重构代码，哪怕完成70%的小问题，也比不能解决一个大问题强得多。

2.打好基础，不能因为一个容易简单的问题影响整个解决流程。


