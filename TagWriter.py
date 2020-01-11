# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 08:10:07 2020

@author: Sandy Lin
"""

def TagWriter(name,*contents,cls=None,**attrs):
    if cls==None:
        attrs=None
    else:
        attrs['class']=cls
    if attrs is not None:
        attrs_str="".join('%s=%s'%(key,value)for key,value in attrs.items())
    else:
        attrs_str=""
    if contents:
        return '\n'.join('<%s%s>%s</%s>'%(name,attrs_str,c,name)for c in contents)
    else:
        return '<%s%s/>'%(name,attrs_str)
        
