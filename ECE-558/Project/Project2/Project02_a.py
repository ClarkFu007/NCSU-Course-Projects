from pylab import *
import numpy as np
import cv2 as cv


# The realization of padding
def spatial_padding(im,height,width,ext_size,bor_type):
    if bor_type==1:            # Type-1 means clip/zero padding
        im_padding=np.zeros([height+2*ext_size,width+2*ext_size,1],np.uint8)
        for m1 in range(0,height):
            for n1 in range(0,width):
                im_padding[m1+ext_size,n1+ext_size]=im[m1,n1]
        return im_padding
    elif bor_type==2:          # Type-2 means wrapping around
        im_padding=np.zeros([height+2*ext_size,width+2*ext_size,1],np.uint8)
        im_temp=np.zeros([height*3,width*3,1],np.uint8)
        for m2 in range(0,height):
            for n2 in range(0,width):
                im_temp[m2,n2],im_temp[m2,n2+width],im_temp[m2,n2+2*width]=im[m2,n2],im[m2,n2],im[m2,n2]
                im_temp[m2+height,n2],im_temp[m2+height,n2+width],im_temp[m2+height,n2+2*width]=im[m2,n2],im[m2,n2],im[m2,n2]
                im_temp[m2+2*height,n2],im_temp[m2+2*height,n2+width],im_temp[m2+2*height,n2+2*width]=im[m2,n2],im[m2,n2],im[m2,n2]
        for m2 in range(0,height+2*ext_size):
            for n2 in range(0,width+2*ext_size):
                im_padding[m2,n2]=im_temp[m2+height-ext_size,n2+width-ext_size]
        return im_padding
    elif bor_type==3:          # Type-3 means copying edge
        im_padding=np.zeros([height+2*ext_size,width+2*ext_size,1],np.uint8)
        im_temp=np.zeros([height*3,width*3])
        for n3 in range(0,width):
            im_temp[height:height*2,n3]=im[:,0]
            im_temp[height:height*2,n3+2*width]=im[:,width-1]
        for m3 in range(0,height):
            im_temp[m3,width:width*2]=im[0,:]
            im_temp[m3+2*height,width:width*2]=im[height-1,:]
        for m3 in range(0,height):
            im_temp[m3,0:width]=im_temp[height,0:width]
            im_temp[m3+2*height,0:width]=im_temp[2*height-1,0:width]
            im_temp[m3,2*width:3*width]=im_temp[height,2*width:3*width]
            im_temp[m3+2*height,2*width:3*width]=im_temp[2*height-1,2*width:3*width]
        for m3 in range(0,height):
            for n3 in range(0,width):
                im_temp[m3+height,n3+width]=im[m3,n3]
        for m3 in range(0,height+2*ext_size):
            for n3 in range(0,width+2*ext_size):
                im_padding[m3,n3]=im_temp[m3+height-ext_size,n3+width-ext_size]
        return im_padding
    elif bor_type==4:          # Type-4 means reflecting across edge
        im_padding=np.zeros([height+2*ext_size,width+2*ext_size,1],np.uint8)
        im_temp=np.zeros([height*3,width*3])
        for n4 in range(0,width):
            im_temp[0:height,n4+width]=im[::-1,n4]
            im_temp[2*height:height*3,n4+width]=im[::-1,n4]
        for m4 in range(0,height):
            im_temp[m4+height,0:width]=im[m4,::-1]
            im_temp[m4+height,2*width:width*3]=im[m4,::-1]
        for m4 in range(0,height):
            im_temp[m4,0:width]=im_temp[m4,width*2-1:width-1:-1]
            im_temp[m4,2*width:width*3]=im_temp[m4,width*2-1:width-1:-1]
            im_temp[m4+2*height,0:width]=im_temp[m4+2*height,width*2-1:width-1:-1]
            im_temp[m4+2*height,2*width:width*3]=im_temp[m4+2*height,width*2-1:width-1:-1]
        for m4 in range(0,height):
            for n4 in range(0,width):
                im_temp[m4+height,n4+width]=im[m4,n4]
        for m4 in range(0,height+2*ext_size):
            for n4 in range(0,width+2*ext_size):
                im_padding[m4,n4]=im_temp[m4+height-ext_size,n4+width-ext_size]
        return im_padding
    else:
        print("Error!")
        return False


# The realization of convolution
def spatial_filtering(im,height,width,ext_size,bor_type,kernel):
    if bor_type==1:
        im_change=spatial_padding(im,height,width,ext_size,bor_type)
    elif bor_type==2:
        im_change=spatial_padding(im,height,width,ext_size,bor_type)
    elif bor_type==3:
        im_change=spatial_padding(im,height,width,ext_size,bor_type)
    elif bor_type==4:
        im_change=spatial_padding(im,height,width,ext_size,bor_type)
    else:
        print("Error!")
        return False

    m0,n0=len(kernel),len(kernel.T)
    if m0 % 2==1 and n0 % 2==1:          # When both the height and width of the kernel matrix are odd
        index_i=int((m0-1)/2)
        index_j=int((n0-1)/2)
        im_new=np.zeros([height,width],np.uint8)
        for y in range(ext_size,height+ext_size):
            for x in range(ext_size,width+ext_size):
                for i in range(-index_i,index_i+1):
                    for j in range(-index_j,index_j+1):
                        im_new[y-ext_size,x-ext_size]=np.round(im_new[y-ext_size,x-ext_size]+kernel[i+index_i,j+index_j]*im_change[y+i,x+j])
        return im_new
    elif m0 % 2==0 and n0 % 2==1:        # When the height of the kernel matrix is even while the width is odd
        index_i=int(m0/2)
        index_j=int((n0-1)/2)
        im_new=np.zeros([height,width],np.uint8)
        for y in range(ext_size,height+ext_size):
            for x in range(ext_size,width+ext_size):
                for i in range(-index_i,index_i):
                    for j in range(-index_j,index_j+1):
                        im_new[y-ext_size,x-ext_size]=np.round(im_new[y-ext_size,x-ext_size]+kernel[i+index_i,j+index_j]*im_change[y+i,x+j])
        return im_new
    elif m0 % 2==1 and n0 % 2==0:        # When the height of the kernel matrix is odd while the width is even
        index_i=int((m0-1)/2)
        index_j=int(n0/2)
        im_new=np.zeros([height,width],np.uint8)
        for y in range(ext_size,height+ext_size):
            for x in range(ext_size,width+ext_size):
                for i in range(-index_i,index_i+1):
                    for j in range(-index_j,index_j):
                        im_new[y-ext_size,x-ext_size]=np.round(im_new[y-ext_size,x-ext_size]+kernel[i+index_i,j+index_j]*im_change[y+i,x+j])
        return im_new
    elif m0 % 2==0 and n0 % 2==0:        # When both the height and width of the kernel matrix are even
        index_i=int(m0/2)
        index_j=int(n0/2)
        im_new=np.zeros([height,width],np.uint8)
        for y in range(ext_size,height+ext_size):
            for x in range(ext_size,width+ext_size):
                for i in range(-index_i,index_i):
                    for j in range(-index_j,index_j):
                        im_new[y-ext_size,x-ext_size]=np.round(im_new[y-ext_size,x-ext_size]+kernel[i+index_i,j+index_j]*im_change[y+i,x+j])
        return im_new


img=cv.imread('lena.png')                # Input the image( 'lena.png' and 'wolves.png')
im_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
im_b,im_g,im_r=cv.split(img)
m=img.shape[0]
n=img.shape[1]

# To get pictures of four types of padding
im_change_b1=spatial_padding(im_b,m,n,20,1)                # Clip/zero-padding
im_change_g1=spatial_padding(im_g,m,n,20,1)                # Clip/zero-padding
im_change_r1=spatial_padding(im_r,m,n,20,1)                # Clip/zero-padding
im_change_1=cv.merge([im_change_b1,im_change_g1,im_change_r1])
cv.imwrite('Type1 padding.png',im_change_1)
im_change_b2=spatial_padding(im_b,m,n,20,2)                # Wrap around
im_change_g2=spatial_padding(im_g,m,n,20,2)                # Wrap around
im_change_r2=spatial_padding(im_r,m,n,20,2)                # Wrap around
im_change_2=cv.merge([im_change_b2,im_change_g2,im_change_r2])
cv.imwrite('Type2 padding.png',im_change_2)
im_change_b2=spatial_padding(im_b,m,n,20,3)                # Copy edge
im_change_g2=spatial_padding(im_g,m,n,20,3)                # Copy edge
im_change_r2=spatial_padding(im_r,m,n,20,3)                # Copy edge
im_change_3=cv.merge([im_change_b2,im_change_g2,im_change_r2])
cv.imwrite('Type3 padding.png',im_change_3)
im_change_b4=spatial_padding(im_b,m,n,20,4)               # Reflect across edge
im_change_g4=spatial_padding(im_g,m,n,20,4)               # Reflect across edge
im_change_r4=spatial_padding(im_r,m,n,20,4)               # Reflect across edge
im_change_4=cv.merge([im_change_b4,im_change_g4,im_change_r4])
cv.imwrite('Type4 padding.png',im_change_4)


# Question(a)
box_filter=np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9
first_ord_der_filter_x,first_ord_der_filter_y=np.array([[-1,1]]),np.array([[1],[-1]])
Pitt_x, Pitt_y=np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]), np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
Sbl_x,Sbl_y=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
Rots_x,Rots_y=np.array([[0,1],[-1,0]]),np.array([[1,0],[0,-1]])

# Use the box filter
im_gray1_1=spatial_filtering(im_gray,m,n,20,1,box_filter)
cv.imwrite('wolves_gray_clip_box.png',im_gray1_1)
im_gray1_2=spatial_filtering(im_gray,m,n,20,2,box_filter)
cv.imwrite('wolves_gray_wrap_box.png',im_gray1_2)
im_gray1_3=spatial_filtering(im_gray,m,n,20,3,box_filter)
cv.imwrite('wolves_gray_copy_box.png',im_gray1_3)
im_gray1_4=spatial_filtering(im_gray,m,n,20,4,box_filter)
cv.imwrite('wolves_gray_reflect_box.png',im_gray1_4)

im_b1_1=spatial_filtering(im_b,m,n,20,1,box_filter)
im_g1_1=spatial_filtering(im_g,m,n,20,1,box_filter)
im_r1_1=spatial_filtering(im_r,m,n,20,1,box_filter)
im_rgb1_1=cv.merge([im_b1_1,im_g1_1,im_r1_1])
cv.imwrite('wolves_rgb_clip_box.png',im_rgb1_1)
im_b1_2=spatial_filtering(im_b,m,n,20,2,box_filter)
im_g1_2=spatial_filtering(im_g,m,n,20,2,box_filter)
im_r1_2=spatial_filtering(im_r,m,n,20,2,box_filter)
im_rgb1_2=cv.merge([im_b1_2,im_g1_2,im_r1_2])
cv.imwrite('wolves_rgb_wrap_box.png',im_rgb1_2)
im_b1_3=spatial_filtering(im_b,m,n,20,3,box_filter)
im_g1_3=spatial_filtering(im_g,m,n,20,3,box_filter)
im_r1_3=spatial_filtering(im_r,m,n,20,3,box_filter)
im_rgb1_3=cv.merge([im_b1_3,im_g1_3,im_r1_3])
cv.imwrite('wolves_rgb_copy_box.png',im_rgb1_3)
im_b1_4=spatial_filtering(im_b,m,n,20,4,box_filter)
im_g1_4=spatial_filtering(im_g,m,n,20,4,box_filter)
im_r1_4=spatial_filtering(im_r,m,n,20,4,box_filter)
im_rgb1_4=cv.merge([im_b1_4,im_g1_4,im_r1_4])
cv.imwrite('wolves_rgb_reflect_box.png',im_rgb1_4)

# Use the simple first order derivative filter in the X direction
im_gray2x_1=spatial_filtering(im_gray,m,n,20,1,first_ord_der_filter_x)
cv.imwrite('wolves_gray_clip_1st_der_x.png',im_gray2x_1)
im_gray2x_2=spatial_filtering(im_gray,m,n,20,2,first_ord_der_filter_x)
cv.imwrite('wolves_gray_wrap_1st_der_x.png',im_gray2x_2)
im_gray2x_3=spatial_filtering(im_gray,m,n,20,3,first_ord_der_filter_x)
cv.imwrite('wolves_gray_copy_1st_der_x.png',im_gray2x_3)
im_gray2x_4=spatial_filtering(im_gray,m,n,20,4,first_ord_der_filter_x)
cv.imwrite('wolves_gray_reflect_1st_der_x.png',im_gray2x_4)

im_b2x_1=spatial_filtering(im_b,m,n,20,1,first_ord_der_filter_x)
im_g2x_1=spatial_filtering(im_g,m,n,20,1,first_ord_der_filter_x)
im_r2x_1=spatial_filtering(im_r,m,n,20,1,first_ord_der_filter_x)
im_rgb2x_1=cv.merge([im_b2x_1,im_g2x_1,im_r2x_1])
cv.imwrite('wolves_rgb_clip_1st_der_x.png',im_rgb2x_1)
im_b2x_2=spatial_filtering(im_b,m,n,20,2,first_ord_der_filter_x)
im_g2x_2=spatial_filtering(im_g,m,n,20,2,first_ord_der_filter_x)
im_r2x_2=spatial_filtering(im_r,m,n,20,2,first_ord_der_filter_x)
im_rgb2x_2=cv.merge([im_b2x_2,im_g2x_2,im_r2x_2])
cv.imwrite('wolves_rgb_wrap_1st_der_x.png',im_rgb2x_2)
im_b2x_3=spatial_filtering(im_b,m,n,20,3,first_ord_der_filter_x)
im_g2x_3=spatial_filtering(im_g,m,n,20,3,first_ord_der_filter_x)
im_r2x_3=spatial_filtering(im_r,m,n,20,3,first_ord_der_filter_x)
im_rgb2x_3=cv.merge([im_b2x_3,im_g2x_3,im_r2x_3])
cv.imwrite('wolves_rgb_copy_1st_der_x.png',im_rgb2x_3)
im_b2x_4=spatial_filtering(im_b,m,n,20,4,first_ord_der_filter_x)
im_g2x_4=spatial_filtering(im_g,m,n,20,4,first_ord_der_filter_x)
im_r2x_4=spatial_filtering(im_r,m,n,20,4,first_ord_der_filter_x)
im_rgb2x_4=cv.merge([im_b2x_4,im_g2x_4,im_r2x_4])
cv.imwrite('wolves_rgb_reflect_1st_der_x.png',im_rgb2x_4)

# Use the simple first order derivative filter in the Y direction
im_gray2y_1=spatial_filtering(im_gray,m,n,20,1,first_ord_der_filter_y)
cv.imwrite('wolves_gray_clip_1st_der_y.png',im_gray2y_1)
im_gray2y_2=spatial_filtering(im_gray,m,n,20,2,first_ord_der_filter_y)
cv.imwrite('wolves_gray_wrap_1st_der_y.png',im_gray2y_2)
im_gray2y_3=spatial_filtering(im_gray,m,n,20,3,first_ord_der_filter_y)
cv.imwrite('wolves_gray_copy_1st_der_y.png',im_gray2y_3)
im_gray2y_4=spatial_filtering(im_gray,m,n,20,4,first_ord_der_filter_y)
cv.imwrite('wolves_gray_reflect_1st_der_y.png',im_gray2y_4)

im_b2y_1=spatial_filtering(im_b,m,n,20,1,first_ord_der_filter_y)
im_g2y_1=spatial_filtering(im_g,m,n,20,1,first_ord_der_filter_y)
im_r2y_1=spatial_filtering(im_r,m,n,20,1,first_ord_der_filter_y)
im_rgb2y_1=cv.merge([im_b2y_1,im_g2y_1,im_r2y_1])
cv.imwrite('wolves_rgb_clip_1st_der_y.png',im_rgb2y_1)
im_b2y_2=spatial_filtering(im_b,m,n,20,2,first_ord_der_filter_y)
im_g2y_2=spatial_filtering(im_g,m,n,20,2,first_ord_der_filter_y)
im_r2y_2=spatial_filtering(im_r,m,n,20,2,first_ord_der_filter_y)
im_rgb2y_2=cv.merge([im_b2y_2,im_g2y_2,im_r2y_2])
cv.imwrite('wolves_rgb_wrap_1st_der_y.png',im_rgb2y_2)
im_b2y_3=spatial_filtering(im_b,m,n,20,3,first_ord_der_filter_y)
im_g2y_3=spatial_filtering(im_g,m,n,20,3,first_ord_der_filter_y)
im_r2y_3=spatial_filtering(im_r,m,n,20,3,first_ord_der_filter_y)
im_rgb2y_3=cv.merge([im_b2y_3,im_g2y_3,im_r2y_3])
cv.imwrite('wolves_rgb_copy_1st_der_y.png',im_rgb2y_3)
im_b2y_4=spatial_filtering(im_b,m,n,20,4,first_ord_der_filter_y)
im_g2y_4=spatial_filtering(im_g,m,n,20,4,first_ord_der_filter_y)
im_r2y_4=spatial_filtering(im_r,m,n,20,4,first_ord_der_filter_y)
im_rgb2y_4=cv.merge([im_b2y_4,im_g2y_4,im_r2y_4])
cv.imwrite('wolves_rgb_reflect_1st_der_y.png',im_rgb2y_4)

# Use the Prewitt filter in the X direction
im_gray31x_1=spatial_filtering(im_gray,m,n,20,1,Pitt_x)
cv.imwrite('wolves_gray_clip_Pitt_x.png',im_gray31x_1)
im_gray31x_2=spatial_filtering(im_gray,m,n,20,2,Pitt_x)
cv.imwrite('wolves_gray_wrap_Pitt_x.png',im_gray31x_2)
im_gray31x_3=spatial_filtering(im_gray,m,n,20,3,Pitt_x)
cv.imwrite('wolves_gray_copy_Pitt_x.png',im_gray31x_3)
im_gray31x_4=spatial_filtering(im_gray,m,n,20,4,Pitt_x)
cv.imwrite('wolves_gray_reflect_Pitt_x.png',im_gray31x_4)

im_b31x_1=spatial_filtering(im_b,m,n,20,1,Pitt_x)
im_g31x_1=spatial_filtering(im_g,m,n,20,1,Pitt_x)
im_r31x_1=spatial_filtering(im_r,m,n,20,1,Pitt_x)
im_rgb31x_1=cv.merge([im_b31x_1,im_g31x_1,im_r31x_1])
cv.imwrite('wolves_rgb_clip_Pitt_x.png',im_rgb31x_1)
im_b31x_2=spatial_filtering(im_b,m,n,20,2,Pitt_x)
im_g31x_2=spatial_filtering(im_g,m,n,20,2,Pitt_x)
im_r31x_2=spatial_filtering(im_r,m,n,20,2,Pitt_x)
im_rgb31x_2=cv.merge([im_b31x_2,im_g31x_2,im_r31x_2])
cv.imwrite('wolves_rgb_wrap_Pitt_x.png',im_rgb31x_2)
im_b31x_3=spatial_filtering(im_b,m,n,20,3,Pitt_x)
im_g31x_3=spatial_filtering(im_g,m,n,20,3,Pitt_x)
im_r31x_3=spatial_filtering(im_r,m,n,20,3,Pitt_x)
im_rgb31x_3=cv.merge([im_b31x_3,im_g31x_3,im_r31x_3])
cv.imwrite('wolves_rgb_copy_Pitt_x.png',im_rgb31x_3)
im_b31x_4=spatial_filtering(im_b,m,n,20,4,Pitt_x)
im_g31x_4=spatial_filtering(im_g,m,n,20,4,Pitt_x)
im_r31x_4=spatial_filtering(im_r,m,n,20,4,Pitt_x)
im_rgb31x_4=cv.merge([im_b31x_4,im_g31x_4,im_r31x_4])
cv.imwrite('wolves_rgb_reflect_Pitt_x.png',im_rgb31x_4)
# Use the Prewitt filter in the Y direction
im_gray31y_1=spatial_filtering(im_gray,m,n,20,1,Pitt_y)
cv.imwrite('wolves_gray_clip_Pitt_y.png',im_gray31y_1)
im_gray31y_2=spatial_filtering(im_gray,m,n,20,2,Pitt_y)
cv.imwrite('wolves_gray_wrap_Pitt_y.png',im_gray31y_2)
im_gray31y_3=spatial_filtering(im_gray,m,n,20,3,Pitt_y)
cv.imwrite('wolves_gray_copy_Pitt_y.png',im_gray31y_3)
im_gray31y_4=spatial_filtering(im_gray,m,n,20,4,Pitt_y)
cv.imwrite('wolves_gray_reflect_Pitt_y.png',im_gray31y_4)

im_b31y_1=spatial_filtering(im_b,m,n,20,1,Pitt_y)
im_g31y_1=spatial_filtering(im_g,m,n,20,1,Pitt_y)
im_r31y_1=spatial_filtering(im_r,m,n,20,1,Pitt_y)
im_rgb31y_1=cv.merge([im_b31y_1,im_g31y_1,im_r31y_1])
cv.imwrite('wolves_rgb_clip_Pitt_y.png',im_rgb31y_1)
im_b31y_2=spatial_filtering(im_b,m,n,20,2,Pitt_y)
im_g31y_2=spatial_filtering(im_g,m,n,20,2,Pitt_y)
im_r31y_2=spatial_filtering(im_r,m,n,20,2,Pitt_y)
im_rgb31y_2=cv.merge([im_b31y_2,im_g31y_2,im_r31y_2])
cv.imwrite('wolves_rgb_wrap_Pitt_y.png',im_rgb31y_2)
im_b31y_3=spatial_filtering(im_b,m,n,20,3,Pitt_y)
im_g31y_3=spatial_filtering(im_g,m,n,20,3,Pitt_y)
im_r31y_3=spatial_filtering(im_r,m,n,20,3,Pitt_y)
im_rgb31y_3=cv.merge([im_b31y_3,im_g31y_3,im_r31y_3])
cv.imwrite('wolves_rgb_copy_Pitt_y.png',im_rgb31y_3)
im_b31y_4=spatial_filtering(im_b,m,n,20,4,Pitt_y)
im_g31y_4=spatial_filtering(im_g,m,n,20,4,Pitt_y)
im_r31y_4=spatial_filtering(im_r,m,n,20,4,Pitt_y)
im_rgb31y_4=cv.merge([im_b31y_4,im_g31y_4,im_r31y_4])
cv.imwrite('wolves_rgb_reflect_Pitt_y.png',im_rgb31y_4)

# Use the Sobel filter in the X direction
im_gray32x_1=spatial_filtering(im_gray,m,n,20,1,Sbl_x)
cv.imwrite('wolves_gray_clip_Sbl_x.png',im_gray32x_1)
im_gray32x_2=spatial_filtering(im_gray,m,n,20,2,Sbl_x)
cv.imwrite('wolves_gray_wrap_Sbl_x.png',im_gray32x_2)
im_gray32x_3=spatial_filtering(im_gray,m,n,20,3,Sbl_x)
cv.imwrite('wolves_gray_copy_Sbl_x.png',im_gray32x_3)
im_gray32x_4=spatial_filtering(im_gray,m,n,20,4,Sbl_x)
cv.imwrite('wolves_gray_reflect_Sbl_x.png',im_gray32x_4)

im_b32x_1=spatial_filtering(im_b,m,n,20,1,Sbl_x)
im_g32x_1=spatial_filtering(im_g,m,n,20,1,Sbl_x)
im_r32x_1=spatial_filtering(im_r,m,n,20,1,Sbl_x)
im_rgb32x_1=cv.merge([im_b32x_1,im_g32x_1,im_r32x_1])
cv.imwrite('wolves_rgb_clip_Sbl_x.png',im_rgb32x_1)
im_b32x_2=spatial_filtering(im_b,m,n,20,2,Sbl_x)
im_g32x_2=spatial_filtering(im_g,m,n,20,2,Sbl_x)
im_r32x_2=spatial_filtering(im_r,m,n,20,2,Sbl_x)
im_rgb32x_2=cv.merge([im_b32x_2,im_g32x_2,im_r32x_2])
cv.imwrite('wolves_rgb_wrap_Sbl_x.png',im_rgb32x_2)
im_b32x_3=spatial_filtering(im_b,m,n,20,3,Sbl_x)
im_g32x_3=spatial_filtering(im_g,m,n,20,3,Sbl_x)
im_r32x_3=spatial_filtering(im_r,m,n,20,3,Sbl_x)
im_rgb32x_3=cv.merge([im_b32x_3,im_g32x_3,im_r32x_3])
cv.imwrite('wolves_rgb_copy_Sbl_x.png',im_rgb32x_3)
im_b32x_4=spatial_filtering(im_b,m,n,20,4,Sbl_x)
im_g32x_4=spatial_filtering(im_g,m,n,20,4,Sbl_x)
im_r32x_4=spatial_filtering(im_r,m,n,20,4,Sbl_x)
im_rgb32x_4=cv.merge([im_b32x_4,im_g32x_4,im_r32x_4])
cv.imwrite('wolves_rgb_reflect_Sbl_x.png',im_rgb32x_4)
# Use the Sobel filter in the Y direction
im_gray32y_1=spatial_filtering(im_gray,m,n,20,1,Sbl_y)
cv.imwrite('wolves_gray_clip_Sbl_y.png',im_gray32y_1)
im_gray32y_2=spatial_filtering(im_gray,m,n,20,2,Sbl_y)
cv.imwrite('wolves_gray_wrap_Sbl_y.png',im_gray32y_2)
im_gray32y_3=spatial_filtering(im_gray,m,n,20,3,Sbl_y)
cv.imwrite('wolves_gray_copy_Sbl_y.png',im_gray32y_3)
im_gray32y_4=spatial_filtering(im_gray,m,n,20,4,Pitt_y)
cv.imwrite('wolves_gray_reflect_Sbl_y.png',im_gray32y_4)

im_b32y_1=spatial_filtering(im_b,m,n,20,1,Sbl_y)
im_g32y_1=spatial_filtering(im_g,m,n,20,1,Sbl_y)
im_r32y_1=spatial_filtering(im_r,m,n,20,1,Sbl_y)
im_rgb32y_1=cv.merge([im_b32y_1,im_g32y_1,im_r32y_1])
cv.imwrite('wolves_rgb_clip_Sbl_y.png',im_rgb32y_1)
im_b32y_2=spatial_filtering(im_b,m,n,20,2,Sbl_y)
im_g32y_2=spatial_filtering(im_g,m,n,20,2,Sbl_y)
im_r32y_2=spatial_filtering(im_r,m,n,20,2,Sbl_y)
im_rgb32y_2=cv.merge([im_b32y_2,im_g32y_2,im_r32y_2])
cv.imwrite('wolves_rgb_wrap_Sbl_y.png',im_rgb32y_2)
im_b32y_3=spatial_filtering(im_b,m,n,20,3,Sbl_y)
im_g32y_3=spatial_filtering(im_g,m,n,20,3,Sbl_y)
im_r32y_3=spatial_filtering(im_r,m,n,20,3,Sbl_y)
im_rgb32y_3=cv.merge([im_b32y_3,im_g32y_3,im_r32y_3])
cv.imwrite('wolves_rgb_copy_Sbl_y.png',im_rgb32y_3)
im_b32y_4=spatial_filtering(im_b,m,n,20,4,Sbl_y)
im_g32y_4=spatial_filtering(im_g,m,n,20,4,Sbl_y)
im_r32y_4=spatial_filtering(im_r,m,n,20,4,Sbl_y)
im_rgb32y_4=cv.merge([im_b32y_4,im_g32y_4,im_r32y_4])
cv.imwrite('wolves_rgb_reflect_Sbl_y.png',im_rgb32y_4)

# Use the Roberts filter in the X direction
im_gray33x_1=spatial_filtering(im_gray,m,n,20,1,Rots_x)
cv.imwrite('wolves_gray_clip_Rots_x.png',im_gray33x_1)
im_gray33x_2=spatial_filtering(im_gray,m,n,20,2,Rots_x)
cv.imwrite('wolves_gray_wrap_Rots_x.png',im_gray33x_2)
im_gray33x_3=spatial_filtering(im_gray,m,n,20,3,Rots_x)
cv.imwrite('wolves_gray_copy_Rots_x.png',im_gray33x_3)
im_gray33x_4=spatial_filtering(im_gray,m,n,20,4,Rots_x)
cv.imwrite('wolves_gray_reflect_Rots_x.png',im_gray33x_4)

im_b33x_1=spatial_filtering(im_b,m,n,20,1,Rots_x)
im_g33x_1=spatial_filtering(im_g,m,n,20,1,Rots_x)
im_r33x_1=spatial_filtering(im_r,m,n,20,1,Rots_x)
im_rgb33x_1=cv.merge([im_b33x_1,im_g33x_1,im_r33x_1])
cv.imwrite('wolves_rgb_clip_Rots_x.png',im_rgb33x_1)
im_b33x_2=spatial_filtering(im_b,m,n,20,2,Rots_x)
im_g33x_2=spatial_filtering(im_g,m,n,20,2,Rots_x)
im_r33x_2=spatial_filtering(im_r,m,n,20,2,Rots_x)
im_rgb33x_2=cv.merge([im_b33x_2,im_g33x_2,im_r33x_2])
cv.imwrite('wolves_rgb_wrap_Rots_x.png',im_rgb33x_2)
im_b33x_3=spatial_filtering(im_b,m,n,20,3,Rots_x)
im_g33x_3=spatial_filtering(im_g,m,n,20,3,Rots_x)
im_r33x_3=spatial_filtering(im_r,m,n,20,3,Rots_x)
im_rgb33x_3=cv.merge([im_b33x_3,im_g33x_3,im_r33x_3])
cv.imwrite('wolves_rgb_copy_Rots_x.png',im_rgb33x_3)
im_b33x_4=spatial_filtering(im_b,m,n,20,4,Rots_x)
im_g33x_4=spatial_filtering(im_g,m,n,20,4,Rots_x)
im_r33x_4=spatial_filtering(im_r,m,n,20,4,Rots_x)
im_rgb33x_4=cv.merge([im_b33x_4,im_g33x_4,im_r33x_4])
cv.imwrite('wolves_rgb_reflect_Rots_x.png',im_rgb33x_4)
# Use the Roberts filter in the Y direction
im_gray33y_1=spatial_filtering(im_gray,m,n,20,1,Rots_y)
cv.imwrite('wolves_gray_clip_Rots_y.png',im_gray33y_1)
im_gray33y_2=spatial_filtering(im_gray,m,n,20,2,Rots_y)
cv.imwrite('wolves_gray_wrap_Rots_y.png',im_gray33y_2)
im_gray33y_3=spatial_filtering(im_gray,m,n,20,3,Rots_y)
cv.imwrite('wolves_gray_copy_Rots_y.png',im_gray33y_3)
im_gray33y_4=spatial_filtering(im_gray,m,n,20,4,Rots_y)
cv.imwrite('wolves_gray_reflect_Rots_y.png',im_gray33y_4)

im_b33y_1=spatial_filtering(im_b,m,n,20,1,Rots_y)
im_g33y_1=spatial_filtering(im_g,m,n,20,1,Rots_y)
im_r33y_1=spatial_filtering(im_r,m,n,20,1,Rots_y)
im_rgb33y_1=cv.merge([im_b33y_1,im_g33y_1,im_r33y_1])
cv.imwrite('wolves_rgb_clip_Rots_y.png',im_rgb33y_1)
im_b33y_2=spatial_filtering(im_b,m,n,20,2,Rots_y)
im_g33y_2=spatial_filtering(im_g,m,n,20,2,Rots_y)
im_r33y_2=spatial_filtering(im_r,m,n,20,2,Rots_y)
im_rgb33y_2=cv.merge([im_b33y_2,im_g33y_2,im_r33y_2])
cv.imwrite('wolves_rgb_wrap_Rots_y.png',im_rgb33y_2)
im_b33y_3=spatial_filtering(im_b,m,n,20,3,Rots_y)
im_g33y_3=spatial_filtering(im_g,m,n,20,3,Rots_y)
im_r33y_3=spatial_filtering(im_r,m,n,20,3,Rots_y)
im_rgb33y_3=cv.merge([im_b33y_3,im_g33y_3,im_r33y_3])
cv.imwrite('wolves_rgb_copy_Rots_y.png',im_rgb33y_3)
im_b33y_4=spatial_filtering(im_b,m,n,20,4,Rots_y)
im_g33y_4=spatial_filtering(im_g,m,n,20,4,Rots_y)
im_r33y_4=spatial_filtering(im_r,m,n,20,4,Rots_y)
im_rgb33y_4=cv.merge([im_b33y_4,im_g33y_4,im_r33y_4])
cv.imwrite('wolves_rgb_reflect_Rots_y.png',im_rgb33y_4)


# Question(b)
img_impulse=np.zeros([1024,1024,1],np.uint8)
img_impulse[512,512]=255
img_convolution=spatial_filtering(img_impulse,1024,1024,20,1,box_filter)
cv.imwrite('The image of unit impulse.png',img_impulse)
cv.imwrite('The filter result.png',img_convolution)