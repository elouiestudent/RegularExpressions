#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6


import sys


def createDict():
    questions = dict()
    questions[31] = r"/^0$|^100$|^101$/"
    questions[32] = r"/\A[01]*\Z/"
    questions[33] = r"/[0]$/"
    questions[34] = r"/\w*[aeiou]\w*[aeiou]\w*/"
    questions[35] = r"/\A1+[01]*0\Z|^0$/"
    questions[36] = r"/\A[01]*110[01]*\Z/"
    questions[37] = r"/\A.{2,4}\Z/"
    questions[38] = r"/^[0-9]{3}[ -]*[0-9]{2}[ -]*[0-9]{4}$/"
    questions[39] = r"/^.*?d\w*/m"
    questions[40] = r"/^0[01]*0$|^1[01]*1$/"
    questions[41] = r"/\b[PCKpck]/"
    questions[42] = r"/\A.(..)*\Z/"
    questions[43] = r"/(^[0]([01][01])*$)|(^[1][01]([01][01])*$)/"
    questions[44] = r"/^(?!.*110).*$/"
    questions[45] = r"/\A[xo.]{64}\Z/i"
    questions[46] = r"/\A[xo]*[.]{1}[xo]*\Z/i"
    questions[47] = r"/\A(^[x][xo]*[.]*[xo.]*$)|(^[xo]*[.]*[xo.]*[x]$)\Z/i"
    questions[48] = r"/\A[^a]*a{1}[^a]*\Z/"
    questions[49] = r"/\A[^a]*(a[^a]*a[^a]*)*\Z/"
    questions[50] = r"/\A[^1]*(1[^1]*1[^1]*)*\Z/"
    questions[51] = r"/^(.)\1{10}$/"
    questions[52] = r"/(\w)\w*\1/"
    questions[53] = r"/\w*(\w)\1\w*/"
    questions[54] = r"/\w*(\w)\w*\1\w*/"
    questions[55] = r"/^([01])[01]*\1$/"
    questions[56] = r"(?=\w*cat\w*)\A\w{6}\Z"
    questions[57] = r"/\A([01])(?<=[01])[01]*\1\Z/"
    questions[58] = r"/\A(?=([01]))[01]*\1\Z/"
    questions[59] = r"/\A([aeiou])\w*(?!\1)[aeiou]\Z/"
    questions[60] = r"/\A((?!011)[01])*\Z/"
    return questions


probnum = int(sys.argv[1])
print(createDict()[probnum])