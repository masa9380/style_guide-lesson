# 変数の定義
x = 1  # [=]の前後にスペースを1つ入れる
y = 1
# wrong
xxx     = 1 # スペースの数がおおい、合っていない
y       = 1
x = 1   # 数字の後に不要なスペースを入れている


# 関数の引数の「＝」にはスペース不要
# 正
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# 誤
def complex(real, imag=0.0):
    return magic(r = real, i = imag)

# operator：演算子の周りには前後にスペースを1つ
# 正
x = x + 1
x += 1
# 誤
x=x+1
x +=1

# operatorにpriorityがある場合はスペースをなくす
# 例
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# カンマの後ろにはスペースを入れる
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)
# 例外：カンマの後に閉じかっこがくる場合はスペース不要
foo = (0,)  #正
foo = (0, ) #誤


# 正
FILLES = [
    'setup.cfg',
    'tox.ini',  # 最後の要素でもカンマを打ってもよい
    'tox.ini',  # コピーして足した場合でも、gitのバージョン管理がしやすい
    'tox.ini',
    'tox.ini',
]

# 誤
FILLES = ['setup.cfg', 'tox.ini',] # この場合は結局その行自体が変更されたとなるのでよくないというか意味ない


# 行の折返し
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
# 変数の頭を揃えるか、第一引数の時点でインデントをしてそれを揃えるか。

foo = long_function_name(var_one, var_two,
    var_three, var_four)
# ↑これは間違い

# 関数を定義した
#
# 関数を定義する際の改行について
def long_function_name(
        var_ome, var_two, var_three,    # 引数のところで改行するが
        var_four)                       # インデントはスペース8個分
    print(var_one)                      # 4個分にすると中身の始まりとかぶりわかりにくい

# '\'で開業することもできる
print('このように、表示する文章が長い場合は、\
バックスラッシュで区切ると改行できる')

# 正
a = 10000000000000 \
    + 100000000000 \
    + 100000000000000 \
    + 1000000000000
# 誤
a = 10000000000000 +\
    100000000000 +\
    100000000000000 +\
    1000000000000

# 関数の間は2行空ける
def func1():
    pass


def func2():
    pass


# クラス内のメソッドは1行空ける
class MyClass():
    def __init__(self):
        pass

    def method(self):
        pass

# importのStyle
# correct
import os
import sys

# wrong
import os, sys

# fromを使う時は、1行にまとめる
from subprocess import Popen, PIPE

# 順番
# 1. Standard library (time, sys)
# 2. Third party (numpy, pandas)
# 3. Our library
# 4. Local library
# これらそれぞれに1行空ける

# 基本的にはabsolute importを使う
# パスが長すぎる場合は相対インポートをつかってもOK
import mypkg.sibling
import .sibling

# コメントについて
# ・コメントは常に最新に。コードの中身がコメントと異なるなら、ない方がまし。
# ・なるべく英語で書く。日本人しか読まないなら日本語でもOK
# ・書くときは文章で書くことが望ましい。
# ・＃の後に半角スペースを入れる
# ・インラインコメントはコードの後に半角スペースを2ついれる
# ・Docstringは基本的に全てのmodule, function, class, metnodに付ける
# ・そのコードが「何をしているか」よりも、「なぜそう書いたか」の方が有益


# name convention:命名規則

# return
def foo(x):
    if x >= 0:
        return math.squrt(x)
    else:
        return None


# オブジェクトタイプの確認はisinstance()をつかう

# correct
if isinstance(obj, int):

# wrong
if type(obj) is type(1):


# Booleanに対して、比較演算子はつかわない
bool_var = True
# correct
if bool_var:

# wrong
if bool_var == True:



# type hint
def greeting(name: str) -> str:
    return "Hello" + name
# 一つでもヒントをつけたらその関数の変数には全てhintをつける
