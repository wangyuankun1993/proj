#!/bin/bash

name="wangyuankun"
echo ${name}
echo ${#name[0]}
echo ${name:0:5}
echo `expr index "$name" a`

array=("apple" "pear" "banana" 20 wang)
echo ${array[@]}
echo ${array[1]}
echo ${#array[@]}
echo ${#array[2]}

:<<EOF
This is a shell test file!
This section is comment in shell!
The EOF character can be replaced by any string! For example ', !, etc.
EOF

echo "Shell 传递参数实例！"
echo "执行的文件名：$0"
echo "第一个参数为：$1"
echo "第一个参数为：$2"
echo "第一个参数为：$3"
echo "传递到脚本的参数个数：$#"
echo "输出所有参数：\"$*\""
echo "输出所有参数：\"$@\""
echo "脚本运行的当前进程ID号：$$"
echo "后台运行的最后一个进程ID号：$!"
echo "Shell使用的当前选项：$-"
echo "显示最后命令的退出状态，0表示没有错误，其他任何值表明有错误：$?"
