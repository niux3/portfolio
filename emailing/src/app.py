#coding:utf-8
from emailing.Emailing import Emailing
try:
    if __name__ == '__main__':
        Emailing.run()
except Exception as e:
    print('erreur systeme ==> ', e)
