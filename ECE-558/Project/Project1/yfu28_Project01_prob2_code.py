from PIL import Image
from pylab import *
import numpy as np
import cv2
from collections import deque


def enum_(start,arr_key,arr_value,ord,ind):
    for index1,key1 in enumerate(arr_key):
        if key1==arr_value[ind]:
            ord.append(arr_key[index1])
            ind=index1
        if arr_value[ind]==list(start):
            ord.append(arr_value[ind])
            return ord
    else:
        return enum_(start,arr_key,arr_value,ord,ind)


def find_4_path(im_seg,arr_begin,arr_end,v):
    m,n=len(im_seg),len(im_seg.T)
    if m<=2 and n<=2:
        print("You don't have to use the function!")
        return True
    graph={}
    # On the border
    graph[(im_seg[0,0],0,0)]=[]
    if im_seg[0,1] in v: graph[im_seg[0,0],0,0].append([im_seg[0,1],0,1])
    if im_seg[1,0] in v: graph[im_seg[0,0],0,0].append([im_seg[1,0],1,0])
    graph[(im_seg[m-1,0],m-1,0)]=[]
    if im_seg[m-1,1] in v: graph[im_seg[m-1,0],m-1,0].append([im_seg[m-1,1],m-1,1])
    if im_seg[m-2,0] in v: graph[im_seg[m-1,0],m-1,0].append([im_seg[m-2,0],m-2,0])
    graph[(im_seg[0,n-1],0,n-1)]=[]
    if im_seg[0,n-2] in v: graph[im_seg[0,n-1],0,n-1].append([im_seg[0,n-2],0,n-2])
    if im_seg[1,n-1] in v: graph[im_seg[0,n-1],0,n-1].append([im_seg[1,n-1],1,n-1])
    graph[(im_seg[m-1,n-1],m-1,n-1)]=[]
    if im_seg[m-2,n-1] in v: graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-2,n-1],m-2,n-1])
    if im_seg[m-1,n-2] in v: graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-1,n-2],m-1,n-2])

    if m>2:
        for i in range(1,m-1):
            graph[(im_seg[i,0],i,0)]=[]
            if im_seg[i-1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i-1,0],i-1,0])
            if im_seg[i+1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i+1,0],i+1,0])
            if im_seg[i,1]   in v: graph[im_seg[i,0],i,0].append([im_seg[i,1],i,1])
            graph[(im_seg[i,n-1],i,n-1)]=[]
            if im_seg[i-1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i-1,n-1],i-1,n-1])
            if im_seg[i+1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i+1,n-1],i+1,n-1])
            if im_seg[i,n-2]   in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i,n-2],i,n-2])
    if n>2:
        for j in range(1,n-1):
            graph[(im_seg[0,j],0,j)]=[]
            if im_seg[0,j-1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j-1],0,j-1])
            if im_seg[0,j+1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j+1],0,j+1])
            if im_seg[1,j]   in v: graph[im_seg[0,j],0,j].append([im_seg[1,j],1,j])
            graph[(im_seg[m-1,j],m-1,j)]=[]
            if im_seg[m-1,j-1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j-1],m-1,j-1])
            if im_seg[m-1,j+1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j+1],m-1,j+1])
            if im_seg[m-2,j]   in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j],m-2,j])
    # Off the border
    if m>2 and n>2:
        for i in range(1,m-1):
            for j in range(1,n-1):
                graph[(im_seg[i,j],i,j)]=[]
                if im_seg[i-1,j] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j],i-1,j])
                if im_seg[i+1,j] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j],i+1,j])
                if im_seg[i,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i,j-1],i,j-1])
                if im_seg[i,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i,j+1],i,j+1])

    m_begin,n_begin=arr_begin[0],arr_begin[1]
    pre_pixel={}
    search_queue=deque()
    search_queue+=[[im_seg[m_begin,n_begin],m_begin,n_begin]]
    search_queue+=graph[im_seg[m_begin,n_begin],m_begin,n_begin]
    searched1,searched2=[],[[im_seg[m_begin,n_begin],m_begin,n_begin]]

    for element in graph[im_seg[m_begin,n_begin],m_begin,n_begin]:
        element=tuple([element[1],element[2]])
        pre_pixel[element]=[]
        pre_pixel[element].append([m_begin,n_begin])

    while search_queue:
        pixel_next=search_queue.popleft()
        if pixel_next not in searched1:
            if pixel_next[1]==arr_end[0] and pixel_next[2]==arr_end[1]:
                key_list,value_list=[],[]
                for key,value in pre_pixel.items():
                    key_list.append(list(key))
                    value_list.append(list(value[0]))
                order=[]
                index0=0
                for index in range(0,len(key_list)):
                    if key_list[index]==list(q):
                        order.append(key_list[index])
                        index0=index
                order=enum_(p,key_list,value_list,order,index0)
                new_order=[]
                for i in range(0,len(order)):
                    new_order.append(order.pop())
                print("The 4-type path is: ",new_order)
                print("The length of the shortest 4-type path is: ",len(new_order)-1)
                return True
            for index,element in enumerate(graph[pixel_next[0],pixel_next[1],pixel_next[2]]):
                if element in searched2:
                    graph[pixel_next[0],pixel_next[1],pixel_next[2]].pop(index)
            for element1 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                if element1 not in searched2:
                    element1=tuple([element1[1],element1[2]])
                    pre_pixel[element1]=[]
                    pre_pixel[element1].append([pixel_next[1],pixel_next[2]])
            for element2 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                searched2.append([element2[0],element2[1],element2[2]])
            search_queue+=graph[pixel_next[0],pixel_next[1],pixel_next[2]]
            searched1.append(pixel_next)

        else: continue
    print("Sorry! The particular path doesn't exist.")
    return False


def find_8_path(im_seg,arr_begin,arr_end,v):
    m,n=len(im_seg),len(im_seg.T)
    if m<=2 and n<=2:
        print("You don't have to use the function!")
        return True
    graph={}
    # On the border
    graph[(im_seg[0,0],0,0)]=[]
    if im_seg[0,1] in v: graph[im_seg[0,0],0,0].append([im_seg[0,1],0,1])
    if im_seg[1,0] in v: graph[im_seg[0,0],0,0].append([im_seg[1,0],1,0])
    if im_seg[1,1] in v: graph[im_seg[0,0],0,0].append([im_seg[1,1],1,1])
    graph[(im_seg[m-1,0],m-1,0)]=[]
    if im_seg[m-1,1] in v: graph[im_seg[m-1,0],m-1,0].append([im_seg[m-1,1],m-1,1])
    if im_seg[m-2,0] in v: graph[im_seg[m-1,0],m-1,0].append([im_seg[m-2,0],m-2,0])
    if im_seg[m-2,1] in v: graph[im_seg[m-1,0],m-1,0].append([im_seg[m-2,1],m-2,1])
    graph[(im_seg[0,n-1],0,n-1)]=[]
    if im_seg[0,n-2] in v: graph[im_seg[0,n-1],0,n-1].append([im_seg[0,n-2],0,n-2])
    if im_seg[1,n-1] in v: graph[im_seg[0,n-1],0,n-1].append([im_seg[1,n-1],1,n-1])
    if im_seg[1,n-2] in v: graph[im_seg[0,n-1],0,n-1].append([im_seg[1,n-2],1,n-2])
    graph[(im_seg[m-1,n-1],m-1,n-1)]=[]
    if im_seg[m-2,n-1] in v: graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-2,n-1],m-2,n-1])
    if im_seg[m-1,n-2] in v: graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-1,n-2],m-1,n-2])
    if im_seg[m-2,n-2] in v: graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-2,n-2],m-2,n-2])

    if m>2:
        for i in range(1,m-1):
            graph[(im_seg[i,0],i,0)]=[]
            if im_seg[i-1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i-1,0],i-1,0])
            if im_seg[i+1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i+1,0],i+1,0])
            if im_seg[i,1]   in v: graph[im_seg[i,0],i,0].append([im_seg[i,1],i,1])
            if im_seg[i-1,1] in v: graph[im_seg[i,0],i,0].append([im_seg[i-1,1],i-1,1])
            if im_seg[i+1,1] in v: graph[im_seg[i,0],i,0].append([im_seg[i+1,1],i+1,1])
            graph[(im_seg[i,n-1],i,n-1)]=[]
            if im_seg[i-1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i-1,n-1],i-1,n-1])
            if im_seg[i+1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i+1,n-1],i+1,n-1])
            if im_seg[i,n-2]   in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i,n-2],i,n-2])
            if im_seg[i-1,n-2] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i-1,n-2],i-1,n-2])
            if im_seg[i+1,n-2] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i+1,n-2],i+1,n-2])
    if n>2:
        for j in range(1,n-1):
            graph[(im_seg[0,j],0,j)]=[]
            if im_seg[0,j-1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j-1],0,j-1])
            if im_seg[0,j+1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j+1],0,j+1])
            if im_seg[1,j]   in v: graph[im_seg[0,j],0,j].append([im_seg[1,j],1,j])
            if im_seg[1,j-1] in v: graph[im_seg[0,j],0,j].append([im_seg[1,j-1],1,j-1])
            if im_seg[1,j+1] in v: graph[im_seg[0,j],0,j].append([im_seg[1,j+1],1,j+1])
            graph[(im_seg[m-1,j],m-1,j)]=[]
            if im_seg[m-1,j-1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j-1],m-1,j-1])
            if im_seg[m-1,j+1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j+1],m-1,j+1])
            if im_seg[m-2,j]   in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j],m-2,j])
            if im_seg[m-2,j-1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j-1],m-2,j-1])
            if im_seg[m-2,j+1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j+1],m-2,j+1])
    # Off the border
    if m>2 and n>2:
        for i in range(1,m-1):
            for j in range(1,n-1):
                graph[(im_seg[i,j],i,j)]=[]
                if im_seg[i-1,j]   in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j],i-1,j])
                if im_seg[i+1,j]   in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j],i+1,j])
                if im_seg[i,j-1]   in v: graph[im_seg[i,j],i,j].append([im_seg[i,j-1],i,j-1])
                if im_seg[i,j+1]   in v: graph[im_seg[i,j],i,j].append([im_seg[i,j+1],i,j+1])
                if im_seg[i-1,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j-1],i-1,j-1])
                if im_seg[i+1,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j-1],i+1,j-1])
                if im_seg[i-1,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j+1],i-1,j+1])
                if im_seg[i+1,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j+1],i+1,j+1])

    m_begin,n_begin=arr_begin[0],arr_begin[1]
    pre_pixel={}
    search_queue=deque()
    search_queue+=[[im_seg[m_begin,n_begin],m_begin,n_begin]]
    search_queue+=graph[im_seg[m_begin,n_begin],m_begin,n_begin]
    searched1,searched2=[],[[im_seg[m_begin,n_begin],m_begin,n_begin]]

    for element in graph[im_seg[m_begin,n_begin],m_begin,n_begin]:
        element=tuple([element[1],element[2]])
        pre_pixel[element]=[]
        pre_pixel[element].append([m_begin,n_begin])

    while search_queue:
        pixel_next=search_queue.popleft()
        if pixel_next not in searched1:
            if pixel_next[1]==arr_end[0] and pixel_next[2]==arr_end[1]:
                key_list,value_list=[],[]
                for key,value in pre_pixel.items():
                    key_list.append(list(key))
                    value_list.append(list(value[0]))
                order=[]
                index0=0
                for index in range(0,len(key_list)):
                    if key_list[index]==list(q):
                        order.append(key_list[index])
                        index0=index
                order=enum_(p,key_list,value_list,order,index0)
                new_order=[]
                for i in range(0,len(order)):
                    new_order.append(order.pop())
                print("The 8-type path is: ",new_order)
                print("The length of the shortest 8-type path is: ",len(new_order)-1)
                return True

            for index,element in enumerate(graph[pixel_next[0],pixel_next[1],pixel_next[2]]):
                if element in searched2:
                    graph[pixel_next[0],pixel_next[1],pixel_next[2]].pop(index)
                for element1 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                    if element1 not in searched2:
                        element1=tuple([element1[1],element1[2]])
                        pre_pixel[element1]=[]
                        pre_pixel[element1].append([pixel_next[1],pixel_next[2]])
                for element2 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                    searched2.append([element2[0],element2[1],element2[2]])
                search_queue+=graph[pixel_next[0],pixel_next[1],pixel_next[2]]
                searched1.append(pixel_next)

        else: continue
    print("Sorry! The particular path doesn't exist.")
    return False


def find_m_path(im_seg,arr_begin,arr_end,v):
    m,n=len(im_seg),len(im_seg.T)
    if m<=2 and n<=2:
        print("You don't have to use the function!")
        return True
    graph={}
    # On the border
    graph[(im_seg[0,0],0,0)]=[]
    if im_seg[0,1] in v:
        graph[im_seg[0,0],0,0].append([im_seg[0,1],0,1])
    if im_seg[1,0] in v:
        graph[im_seg[0,0],0,0].append([im_seg[1,0],1,0])
    if (im_seg[0,1] not in v) and (im_seg[1,0] not in v):
        if im_seg[1,1] in v:
            graph[im_seg[0,0],0,0].append([im_seg[1,1],1,1])
    graph[(im_seg[m-1,0],m-1,0)]=[]
    if im_seg[m-1,1] in v:
        graph[im_seg[m-1,0],m-1,0].append([im_seg[m-1,1],m-1,1])
    if im_seg[m-2,0] in v:
        graph[im_seg[m-1,0],m-1,0].append([im_seg[m-2,0],m-2,0])
    if (im_seg[m-1,1] not in v) and (im_seg[m-2,0] not in v):
        if im_seg[m-2,1] in v:
            graph[im_seg[m-1,0],m-1,0].append([im_seg[m-2,1],m-2,1])
    graph[(im_seg[0,n-1],0,n-1)]=[]
    if im_seg[0,n-2] in v:
        graph[im_seg[0,n-1],0,n-1].append([im_seg[0,n-2],0,n-2])
    if im_seg[1,n-1] in v:
        graph[im_seg[0,n-1],0,n-1].append([im_seg[1,n-1],1,n-1])
    if (im_seg[0,n-2] not in v) and (im_seg[1,n-1] not in v):
        if im_seg[1,n-2] in v:
            graph[im_seg[0,n-1],0,n-1].append([im_seg[1,n-2],1,n-2])
    graph[(im_seg[m-1,n-1],m-1,n-1)]=[]
    if im_seg[m-2,n-1] in v:
        graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-2,n-1],m-2,n-1])
    if im_seg[m-1,n-2] in v:
        graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-1,n-2],m-1,n-2])
    if (im_seg[m-2,n-1] not in v) and (im_seg[n-1,m-2] not in v):
        if im_seg[m-2,n-2] in v:
            graph[im_seg[m-1,n-1],m-1,n-1].append([im_seg[m-2,n-2],m-2,n-2])

    if m>2:
        for i in range(1,m-1):
            # on the left
            graph[(im_seg[i,0],i,0)]=[]
            if im_seg[i-1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i-1,0],i-1,0])
            if im_seg[i+1,0] in v: graph[im_seg[i,0],i,0].append([im_seg[i+1,0],i+1,0])
            if im_seg[i,1]   in v: graph[im_seg[i,0],i,0].append([im_seg[i,1],i,1])
            if (im_seg[i-1,0] not in v) and (im_seg[i+1,0] not in v):
                if im_seg[i,1] not in v:
                    if im_seg[i-1,1] in v: graph[im_seg[i,0],i,0].append([im_seg[i-1,1],i-1,1])
                    if im_seg[i+1,1] in v: graph[im_seg[i,0],i,0].append([im_seg[i+1,1],i+1,1])
            # on the right
            graph[(im_seg[i,n-1],i,n-1)]=[]
            if im_seg[i-1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i-1,n-1],i-1,n-1])
            if im_seg[i+1,n-1] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i+1,n-1],i+1,n-1])
            if im_seg[i,n-2]   in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i,n-2],i,n-2])
            if (im_seg[i-1,n-1] not in v) and (im_seg[i+1,n-1] not in v):
                if im_seg[i,n-2] not in v:
                    if im_seg[i-1,n-2] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i-1,n-2],i-1,n-2])
                    if im_seg[i+1,n-2] in v: graph[im_seg[i,n-1],i,n-1].append([im_seg[i+1,n-2],i+1,n-2])
    if n>2:
        for j in range(1,n-1):
            # on the top
            graph[(im_seg[0,j],0,j)]=[]
            if im_seg[0,j-1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j-1],0,j-1])
            if im_seg[0,j+1] in v: graph[im_seg[0,j],0,j].append([im_seg[0,j+1],0,j+1])
            if im_seg[1,j]   in v: graph[im_seg[0,j],0,j].append([im_seg[1,j],1,j])
            if (im_seg[0,j-1] not in v) and (im_seg[0,j+1] not in v):
                if im_seg[1,j] not in v:
                    if im_seg[1,j-1] in v: graph[im_seg[0,j],0,j].append([im_seg[1,j-1],1,j-1])
                    if im_seg[1,j+1] in v: graph[im_seg[0,j],0,j].append([im_seg[1,j+1],1,j+1])
            # on the underneath
            graph[(im_seg[m-1,j],m-1,j)]=[]
            if im_seg[m-1,j-1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j-1],m-1,j-1])
            if im_seg[m-1,j+1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-1,j+1],m-1,j+1])
            if im_seg[m-2,j]   in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j],m-2,j])
            if (im_seg[m-1,j-1] not in v) and (im_seg[m-1,j+1] not in v):
                if im_seg[m-2,j] not in v:
                    if im_seg[m-2,j-1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j-1],m-2,j-1])
                    if im_seg[m-2,j+1] in v: graph[im_seg[m-1,j],m-1,j].append([im_seg[m-2,j+1],m-2,j+1])
    # Off the border
    if m>2 and n>2:
        for i in range(1,m-1):
            for j in range(1,n-1):
                graph[(im_seg[i,j],i,j)]=[]
                if im_seg[i-1,j] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j],i-1,j])
                if im_seg[i+1,j] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j],i+1,j])
                if im_seg[i,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i,j-1],i,j-1])
                if im_seg[i,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i,j+1],i,j+1])
                if (im_seg[i,j-1] not in v) and (im_seg[i-1,j] not in v) and (im_seg[i,j+1] not in v):
                    if im_seg[i-1,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j-1],i-1,j-1])
                    if im_seg[i+1,j-1] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j-1],i+1,j-1])
                if (im_seg[i,j-1] not in v) and (im_seg[i-1,j] not in v) and (im_seg[i,j+1] not in v):
                    if im_seg[i-1,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i-1,j+1],i-1,j+1])
                    if im_seg[i+1,j+1] in v: graph[im_seg[i,j],i,j].append([im_seg[i+1,j+1],i+1,j+1])

    m_begin,n_begin=arr_begin[0],arr_begin[1]
    pre_pixel={}
    search_queue=deque()
    search_queue+=[[im_seg[m_begin,n_begin],m_begin,n_begin]]
    search_queue+=graph[im_seg[m_begin,n_begin],m_begin,n_begin]
    searched1,searched2=[],[[im_seg[m_begin,n_begin],m_begin,n_begin]]

    for element in graph[im_seg[m_begin,n_begin],m_begin,n_begin]:
        element=tuple([element[1],element[2]])
        pre_pixel[element]=[]
        pre_pixel[element].append([m_begin,n_begin])

    while search_queue:
        pixel_next=search_queue.popleft()
        if pixel_next not in searched1:
            if pixel_next[1]==arr_end[0] and pixel_next[2]==arr_end[1]:
                key_list,value_list=[],[]
                for key,value in pre_pixel.items():
                    key_list.append(list(key))
                    value_list.append(list(value[0]))
                order=[]
                index0=0
                for index in range(0,len(key_list)):
                    if key_list[index]==list(q):
                        order.append(key_list[index])
                        index0=index
                order=enum_(p,key_list,value_list,order,index0)
                new_order=[]
                for i in range(0,len(order)):
                    new_order.append(order.pop())
                print("The m-type path is: ",new_order)
                print("The length of the shortest m-type path is: ",len(new_order)-1)
                return True

            for index,element in enumerate(graph[pixel_next[0],pixel_next[1],pixel_next[2]]):
                if element in searched2:
                    graph[pixel_next[0],pixel_next[1],pixel_next[2]].pop(index)
                for element1 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                    if element1 not in searched2:
                       element1=tuple([element1[1],element1[2]])
                       pre_pixel[element1]=[]
                       pre_pixel[element1].append([pixel_next[1],pixel_next[2]])
                for element2 in graph[pixel_next[0],pixel_next[1],pixel_next[2]]:
                       searched2.append([element2[0],element2[1],element2[2]])
                search_queue+=graph[pixel_next[0],pixel_next[1],pixel_next[2]]
                searched1.append(pixel_next)

        else: continue
    print("Sorry! The particular path doesn't exist.")
    return False


m=int(input('Please set the number of row of your image: \n'))
n=int(input('Please set the number of column of your image: \n'))
A=[]
for i in range(0,m):
   A.append([])
   for j in range(0,n):
       A[i].append(int(input('Please input pixel values：\n')))
p=[]
for i in range(0,2):
       p.append(int(input('Please set your initial point: \n')))
q=[]
for i in range(0,2):
       q.append(int(input('Please set your final point: \n')))
i=int(input('Please set the length of  your predefined V: \n'))
V=[]
for i in range(0,i):
   V.append(int(input('Please set your V: \n')))
path_type=input('Please set your path type: \n')

A=np.array(A)
p,q=tuple(p),tuple(q)
if path_type=='4':
    find_4_path(A,p,q,V)
elif path_type=='8':
    find_8_path(A,p,q,V)
elif path_type=='m':
    find_m_path(A,p,q,V)
else:
    print("Your input is incorrect!")







