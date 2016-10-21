# python_12306
Craw the left tickets data from 12306 by python.

##Brief Introduce
This project use three main liabraries:

1. requests
2. docopt
3. prettytable

##Reminder

**This project is working on Python 3.x,not compatible with 2.x.**

##Usage
You can download the project,and use following code to craw data from 12306.
   
    tickets [-gdtkz] <from> <to> <date>
  	Options:
      -h,--help 显示帮助菜单
      -g        高铁
      -d        动车
      -t        特快
      -k        快速
      -z        直达
  	Example:
      tickets 武汉 无锡 2016-08-25
   
##MIT License

Copyright (c) [2016] [hust201010701]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
