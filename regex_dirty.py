# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 01:00:27 2016

@author: fritz_000
"""

import re

x ='db??a f? Pi F/P=Kia+Maro P(123)a'
a =re.sub('\S+\/[^\s+]+|\S+\?+\S*|\S+\(\S+\)\S*','',x)
b =re.findall('[^+/\s]+',a.upper())