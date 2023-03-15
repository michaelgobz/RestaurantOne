from client import DBClient

Db = DBClient(host='localhost',port=5233,
              user='postgres',password='postgres',db='postgres',echo=True)
__all__ = ['Db']
