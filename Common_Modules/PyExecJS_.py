#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PyExecJS是ExecJS从 ruby 移植的。 PyExecJS自动 选择可以用于评估你的JavaScript程序的最佳运行时间。
# PyExecJS是一个可以运行JavaScript代码的Python第三方库。
# PyExecJS的优点是你不需要处理JavaScript环境。 尤其是在 Windows 环境中，无需安装额外的库。
# PyExecJS的缺点之一就是。 PyExecJS通过文本通信JavaScript运行时，速度慢。 另一种缺点是它不完全支持运行时特定的特性。
# 对于某些用例来说， PyV8可能是更好的选择。

# 首先通过，get_js方法，读取本地的 des_rsa.js 文件。
# 2，调用 execjs.compile() 编译并加载 js 文件内容。
# 3，使用call()调用js中的方法，具体方法如下：

import execjs

code = '''
var ver="4.7.1版本";
var upgrade=0;
function add(x, y) {
    return x + y;
}
'''

context = execjs.compile(code.decode('utf-8r'))
js_ver = context.eval('ver')
func_ret = context.call('add', 1, 2)
print("%s%s" % (js_ver, func_ret))