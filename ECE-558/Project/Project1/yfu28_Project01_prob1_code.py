from PIL import Image
from pylab import *
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import cv2


# Horizontal
def hor_p(arr_):
    m,n,j=len(arr_),len(arr_.T),0
    data=[0]*(m*n)
    for i in range(0,m):
        for p in range(0,n-1):
            data[j]=int(arr_[i,p+1]-arr_[i,p])
            j+=1
    for i in range(0,len(data)):
        data[i]=data[i]*data[i]
    return data


# Vertical
def ver_p(arr_):
    m,n,j=len(arr_),len(arr_.T),0
    data=[0]*(m*n)
    for p in range(0,n):
        for i in range(0,m-1):
            data[j]=int(arr_[i+1,p]-arr_[i,p])
            j+=1
    for i in range(0,len(data)):
        data[i]=data[i]*data[i]
    return data


# 4-Neighbors
def n4_p(arr_):
    m,n=len(arr_),len(arr_.T)
    data=[0]*(m*n)
    # On the border
    data[0],data[1]=round((arr_[0,1]-2*arr_[0,0]+arr_[1,0])/2),round((arr_[0,n-2]-2*arr_[0,n-1]+arr_[1,n-1])/2)
    data[2],data[3]=round((arr_[m-2,0]-2*arr_[m-1,0]+arr_[m-1,1])/2),round((arr_[m-1,n-2]-2*arr_[m-1,n-1]+arr_[m-2,n-1])/2)
    j=4
    for i in range(1,m-1):
        data[j]=round((arr_[i-1,0]-3*arr_[i,0]+arr_[i,1]+arr_[i+1,0])/3)
        data[j+1]=round((arr_[i-1,n-1]-3*arr_[i,n-1]+arr_[i,n-2]+arr_[i+1,n-1])/3)
        j+=2
    for i in range(1,n-1):
        data[j]=round((arr_[0,i-1]-3*arr_[0,i]+arr_[1,i]+arr_[0,i+1])/3)
        data[j+1]=round((arr_[m-1,i-1]-3*arr_[m-1,i]+arr_[m-2,i]+arr_[m-1,i+1])/3)
        j+=2
    # Off the border
    for i in range(1,m-1):
        for p in range(1,n-1):
            data[j]=round((arr_[i,p-1]+arr_[i+1,p]+arr_[i-1,p]+arr_[i,p+1]-4*arr_[i,p])/4)
            j+=1
    for i in range(0,len(data)):
        data[i]=data[i]*data[i]
    return data


# Diagonal-Neighbors
def nd_p(arr_):
    m,n=len(arr_),len(arr_.T)
    data=[0]*(m*n)
    # On the border
    data[0],data[1],data[2],data[3]=arr_[1,1]-arr_[0,0],arr_[1,n-2]-arr_[0,n-1],arr_[m-2,1]-arr_[m-1,0],arr_[m-2,n-2]-arr_[m-1,n-1]
    j=4
    for i in range(1,m-1):
        data[j]=round((arr_[i-1,1]-2*arr_[i,0]+arr_[i+1,1])/2)
        data[j+1]=round((arr_[i-1,n-2]-2*arr_[i,n-1]+arr_[i+1,n-2])/2)
        j+=2
    for i in range(1,n-1):
        data[j]=round((arr_[1,i-1]-2*arr_[0,i]+arr_[1,i+1])/2)
        data[j+1]=round((arr_[m-2,i-1]-2*arr_[m-1,i]+arr_[m-2,i+1])/2)
        j+=2
    # off the border
    for i in range(1,m-1):
        for p in range(1,n-1):
            data[j]=round((arr_[i-1,p-1]+arr_[i-1,p+1]+arr_[i+1,p-1]+arr_[i+1,p+1]-4*arr_[i,p])/4)
            j+=1
    for i in range(0,len(data)):
        data[i]=data[i]*data[i]
    return data


# 8-Neighbors
def n8_p(arr_):
    m,n=len(arr_),len(arr_.T)
    data=[0]*(m*n)
    # On the border
    data[0]=round((arr_[0,1]+arr_[1,0]+arr_[1,1]-3*arr_[0,0])/3)
    data[1]=round((arr_[0,n-2]+arr_[1,n-2]+arr_[1,n-1]-3*arr_[0,n-1])/3)
    data[2]=round((arr_[m-2,0]+arr_[m-2,1]+arr_[m-1,1]-3*arr_[m-1,0])/3)
    data[3]=round((arr_[m-2,n-1]+arr_[m-2,n-2]+arr_[m-1,n-2]-3*arr_[m-1,n-1])/3)
    j=4
    for i in range(1,m-1):
        data[j]=round((arr_[i-1,0]+arr_[i-1,1]+arr_[i,1]+arr_[i+1,1]+arr_[i+1,0]-5*arr_[i,0])/5)
        data[j+1]=round((arr_[i-1,n-1]+arr_[i-1,n-2]+arr_[i,n-2]+arr_[i+1,n-2]+arr_[i+1,n-1]-5*arr_[i,n-1])/5)
        j+=2
    for i in range(1,n-1):
        data[j]=round((arr_[0,i-1]+arr_[1,i-1]+arr_[1,i]+arr_[1,i+1]+arr_[0,i+1]-5*arr_[0,i])/5)
        data[j+1]=round((arr_[m-1,i-1]+arr_[m-2,i-1]+arr_[m-2,i]+arr_[m-2,i+1]+arr_[m-1,i+1]-5*arr_[m-1,i])/5)
        j+=2
    # off the border
    for i in range(1,m-1):
        for p in range(1,n-1):
            data[j]=round((arr_[i-1,p-1]+arr_[i-1,p]+arr_[i-1,p+1]+arr_[i,p-1]+arr_[i,p+1]+
                           arr_[i+1,p-1]+arr_[i+1,p]+arr_[i+1,p+1]-8*arr_[i,p])/8)
            j+=1
    for i in range(0,len(data)):
        data[i]=data[i]*data[i]
    return data


# utilize 5 types of neighbors to visualize histograms of differences between intensity or color values
def plot_histogram_hor(arr1,arr2):      # Horizontal
    data_hor,mark_4=arr1,['horizontal']
    data_hor_mean=round(np.mean(data_hor))
    data_hor_sigma=round(np.std(data_hor,ddof=1))
    num_bins=100
    fig,ax=plt.subplots()
    n_4,bins_4,patches_4=ax.hist(data_hor,num_bins,range=[0,8000],edgecolor='black',facecolor='green',histtype='bar',density=True)
    ax.set_xlabel('Differences')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Histogram of Squared Differences: $\mu=%d$, $\sigma=%d$' %(data_hor_mean,data_hor_sigma))
    fig.savefig('p_%s.png' %(''.join(arr2+mark_4)))


def plot_histogram_ver(arr1,arr2):      # Vertical
    data_ver,mark_4=arr1,['vertical']
    data_ver_mean=round(np.mean(data_ver))
    data_ver_sigma=round(np.std(data_ver,ddof=1))
    num_bins=100
    fig,ax=plt.subplots()
    n_4,bins_4,patches_4=ax.hist(data_ver,num_bins,range=[0,8000],edgecolor='black',facecolor='green',histtype='bar',density=True)
    ax.set_xlabel('Differences')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Histogram of Squared Differences: $\mu=%d$, $\sigma=%d$' %(data_ver_mean,data_ver_sigma))
    fig.savefig('p_%s.png' %(''.join(arr2+mark_4)))


def plot_histogram_4(arr1,arr2):        # 4-Neighbors
    data_4,mark_4=arr1,['four']
    data_4_mean=round(np.mean(data_4))
    data_4_sigma=round(np.std(data_4,ddof=1))
    num_bins=100
    fig,ax=plt.subplots()
    n_4,bins_4,patches_4=ax.hist(data_4,num_bins,range=[0,8000],edgecolor='black',facecolor='green',histtype='bar',density=True)
    ax.set_xlabel('Differences')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Histogram of Squared Differences: $\mu=%d$, $\sigma=%d$' %(data_4_mean,data_4_sigma))
    fig.savefig('p_%s.png' %(''.join(arr2+mark_4)))


def plot_histogram_d(arr1,arr2):        # Diagonal-Neighbors
    data_d,mark_d=arr1,['diagonal']
    data_d_mean=round(np.mean(data_d))
    data_d_sigma=round(np.std(data_d,ddof=1))
    num_bins=100
    fig,ax=plt.subplots()
    n_d,bins_d,patches__d=ax.hist(data_d,num_bins,range=[0,8000],edgecolor='black',facecolor='green',histtype='bar',density=True)
    ax.set_xlabel('Differences')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Histogram of Squared Differences: $\mu=%d$, $\sigma=%d$' %(data_d_mean,data_d_sigma))
    fig.savefig('p_%s.png' %(''.join(arr2+mark_d)))


def plot_histogram_8(arr1,arr2):        # 8-Neighbors
    data_8,mark_8=arr1,['eight']
    data_8_mean=round(np.mean(data_8))
    data_8_sigma=round(np.std(data_8,ddof=1))
    num_bins=100
    fig,ax=plt.subplots()
    n_8,bins_8,patches_8=ax.hist(data_8,num_bins,range=[0,8000],edgecolor='black',facecolor='green',histtype='bar',density=True)
    ax.set_xlabel('Differences')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Histogram of Squared Differences: $\mu=%d$, $\sigma=%d$' %(data_8_mean,data_8_sigma))
    fig.savefig('p_%s.png' %(''.join(arr2+mark_8)))


# open the image
im=Image.open("G:/wolves.png")

# operate the gray image
gray_im=im.convert('L')                         # convert the image into mode 'L'( gray image)
arr_gray=array(gray_im,dtype='int64')
gray=['gray ']
# operate the RGB image
r,g,b=im.split()                               # split the image into R, G, and B channels
arr_r=array(r,dtype='int64')
arr_g=array(g,dtype='int64')
arr_b=array(b,dtype='int64')
rgb=['RGB ']
# operate the HSV image
arr_im=array(im)
arr_hsv=cv2.cvtColor(arr_im, cv2.COLOR_RGB2HSV)
arr_h=arr_hsv[..., 0]
arr_s=arr_hsv[..., 1]
arr_v=arr_hsv[..., 2]
arr_h,arr_s,arr_v=arr_h.astype(np.int64),arr_s.astype(np.int64),arr_v.astype(np.int64)
hsv=['HSV ']
# operate the Lab image
arr_lab=cv2.cvtColor(arr_im, cv2.COLOR_RGB2Lab)
arr_l=arr_lab[..., 0]
arr_a=arr_lab[..., 1]
arr_b_=arr_lab[..., 2]
arr_l,arr_a,arr_b=arr_l.astype(np.int64),arr_a.astype(np.int64),arr_b.astype(np.int64)
lab=['Lab ']

Type=input("Please choose your type(hor, ver, 4, D, and 8): ")
if Type=="hor":
    data_gray=hor_p(arr_gray)
    data_RGB=hor_p(arr_r)+hor_p(arr_g)+hor_p(arr_b)
    data_HSV=hor_p(arr_h)+hor_p(arr_s)+hor_p(arr_v)
    data_lab=hor_p(arr_l)+hor_p(arr_a)+hor_p(arr_b_)
    plot_histogram_hor(data_gray,gray)
    plot_histogram_hor(data_RGB,rgb)
    plot_histogram_hor(data_HSV,hsv)
    plot_histogram_hor(data_lab,lab)
elif Type=="ver":
    data_gray=ver_p(arr_gray)
    data_RGB=ver_p(arr_r)+ver_p(arr_g)+ver_p(arr_b)
    data_HSV=ver_p(arr_h)+ver_p(arr_s)+ver_p(arr_v)
    data_lab=ver_p(arr_l)+ver_p(arr_a)+ver_p(arr_b_)
    plot_histogram_ver(data_gray,gray)
    plot_histogram_ver(data_RGB,rgb)
    plot_histogram_ver(data_HSV,hsv)
    plot_histogram_ver(data_lab,lab)
elif Type=="4":
    data_gray=n4_p(arr_gray)
    data_RGB=n4_p(arr_r)+n4_p(arr_g)+n4_p(arr_b)
    data_HSV=n4_p(arr_h)+n4_p(arr_s)+n4_p(arr_v)
    data_lab=n4_p(arr_l)+n4_p(arr_a)+n4_p(arr_b_)
    plot_histogram_4(data_gray,gray)
    plot_histogram_4(data_RGB,rgb)
    plot_histogram_4(data_HSV,hsv)
    plot_histogram_4(data_lab,lab)
elif Type=="D":
    data_gray=nd_p(arr_gray)
    data_RGB=nd_p(arr_r)+nd_p(arr_g)+nd_p(arr_b)
    data_HSV=nd_p(arr_h)+nd_p(arr_s)+nd_p(arr_v)
    data_lab=nd_p(arr_l)+nd_p(arr_a)+nd_p(arr_b_)
    plot_histogram_d(data_gray,gray)
    plot_histogram_d(data_RGB,rgb)
    plot_histogram_d(data_HSV,hsv)
    plot_histogram_d(data_lab,lab)
elif Type=="8":
    data_gray=n8_p(arr_gray)
    data_RGB=n8_p(arr_r)+n8_p(arr_g)+n8_p(arr_b)
    data_HSV=n8_p(arr_h)+n8_p(arr_s)+n8_p(arr_v)
    data_lab=n8_p(arr_l)+n8_p(arr_a)+n8_p(arr_b_)
    plot_histogram_8(data_gray,gray)
    plot_histogram_8(data_RGB,rgb)
    plot_histogram_8(data_HSV,hsv)
    plot_histogram_8(data_lab,lab)
else:
    print("Your input is incorrect!")




