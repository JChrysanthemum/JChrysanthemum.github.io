from os.path import join as pj
from os import listdir,mkdir
from os.path import isfile,exists
import shutil

def list_files(mypath, end = None):
    if end is None:
        return [f for f in listdir(mypath) if isfile(pj(mypath, f))]
    else:
        return [f for f in listdir(mypath) if isfile(pj(mypath, f)) and f.endswith(end)]


def list_folders(mypath):
    return [f for f in listdir(mypath) if not isfile(pj(mypath, f))]


def clean(s):
    return " ".join(s.split())

def style_formate(txt):
    e_idx = txt.index("---",3)
    head = txt[3:e_idx]
    content = txt[e_idx+3:].strip()
    eles = head.split(":")
    res = {}
    k = eles[0].strip()
    for i in range(1,len(eles)-1):
        _i = eles[i].index("\n")
        v, k2 = eles[i][:_i].strip(), eles[i][_i:].strip()
        res[k]=v
        k = k2
    _i = eles[-1].index("\n")
    v = eles[-1][:_i].strip()
    res[k]=v
    return res,content

def new_head(title,description):
#     s = """---
# layout: post
# title: %s
# categories: 
# description: %s
# keywords: 
# mermaid: false
# sequence: false
# flow: false
# mathjax: false
# mindmap: false
# mindmap2: false
# ---""" % (title,description)
    s="""---
layout: post
title: %s
categories: [cate1, cate2]
description: some word here
keywords: keyword1, keyword2
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---"""%title
    return s

back_up_path = r'C:\Projects\JChrysanthemum.github.io - 副本 (2)\_posts'
new_path = r'C:\Projects\JChrysanthemum.github.io\_posts'

fs = list_files(back_up_path,"md")
fs = [file for file in fs if file != "template.md"]
for file in fs:
    print(file)
    with open(pj(back_up_path,file),"r",encoding="utf-8") as f :
        txt = f.read()
        res,content = style_formate(txt)
        res["title"] = res["title"].replace("[","").replace("]","")
        if "description" in res:
            des = res["description"]
        elif "subtitle" in res:
            des = res["subtitle"]
        else:
            des = ""
        new_txt = new_head(res["title"],des) + "\n\n" + content
    # if exists(pj(new_path,file)):
    #     print("File exists, ignored", pj(new_path,file))
    #     continue
    # shutil.copy(pj(new_path,"template.md"),pj(new_path,file))
    # with open(pj(new_path,"template.md"),"r",encoding="utf-8") as f :
    #     print(["",f.read()])
    # with open(pj(new_path,"2024-11-17-RealSense-Open3D.md"),"r",encoding="utf-8") as f :
    #     print(["",f.read()])
    # exit()
    with open(pj(new_path,file),"a",encoding="utf-8") as f :
        f.write("\n Intro \n\n\n" + ("abc"*50 + "\n")*20 + "  \n\n")

