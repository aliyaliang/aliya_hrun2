# 项目介绍

httprunner2.x 框架分层用例结构实现接口自动化测试

# 环境准备

1.python环境使用3.6以及以上版本

2.安装相关依赖包
'''
pip install httprunner==2.5.7
pip install requests==2.22.0
'''
或者直接安装requirements.txt
> pip install -r requirements.txt

# 运行全部用例

> hrun testsuites

报告查看在reports目录

# 切换报告模板

在项目根目录下新增一个report_template目录，放extent_report_2.5.7.html模板。
不同版本对应的模板不一样，extent_report_2.5.7.html对应httprunner 2.5.7版本，
extent_report_template2.4.3.html 对应httprunner 2.5.7版本。
cd到项目根目录，debugtalk.py所在的目录，--report-template参数指定报告模板

> hrun testsuites --report-template report_template/extent_report_2.5.7.html


# 网易云课程完整视频地址

[点这里，查看网易云课程httprunner2.x框架完整讲解](https://study.163.com/course/courseMain.htm?courseId=1211561801&share=2&shareId=480000002230338)

视频讲解教程在网易云课程可以看：https://study.163.com/course/courseMain.htm?courseId=1211561801&share=2&shareId=480000002230338