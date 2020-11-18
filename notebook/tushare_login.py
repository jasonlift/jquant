import tushare as ts


def getToken():
    token_file = open('token.txt', 'r')
    return token_file.readline()


token = getToken()
ts.set_token(token)
pro = ts.pro_api()