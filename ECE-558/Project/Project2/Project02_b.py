from pylab import *
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

im_gray=cv.imread('wolves.png',0)
m=im_gray.shape[0]
n=im_gray.shape[1]
f=im_gray
f=(f-f.min())*1/(f.max()-f.min())

# prob-a
f0=np.zeros([m,n],dtype=complex)
f1=np.zeros([m,n],dtype=complex)
for i in range(0,m):                 # compute the 1-D DFT transform of each row
    f0[i,:]=np.fft.fft(f[i,:])
for j in range(0,n):                 # compute the 1-D DFT transform of each column
    f0[:,j]=np.fft.fft(f0[:,j])
f1=np.fft.fft2(f)                    # use the build-in function to check my answer
f_shift0=np.fft.fftshift(f0)
f_shift1=np.fft.fftshift(f1)

magnitude_spectrum=np.log(1+abs(np.abs(f_shift0)))
plt.subplot(321),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
phase_spectrum=np.log(1+abs(np.angle(f_shift0)))
plt.subplot(322),plt.imshow(phase_spectrum,cmap='gray')
plt.title('Phase Spectrum'),plt.xticks([]),plt.yticks([])

magnitude_spectrum1=np.log(1+abs(np.abs(f_shift1)))
plt.subplot(323),plt.imshow(magnitude_spectrum1,cmap='gray')
plt.title('Magnitude Spectrum1'),plt.xticks([]),plt.yticks([])
phase_spectrum1=np.log(1+abs(np.angle(f_shift1)))
plt.subplot(324),plt.imshow(phase_spectrum1,cmap='gray')
plt.title('Phase Spectrum1'),plt.xticks([]),plt.yticks([])
plt.show()


# prob-b
g0=np.zeros([m,n],dtype=complex)
f_ishift=np.fft.ifftshift(f_shift0)
for u in range(0,m):                 # compute the 1-D Inverse DFT transform of each row
    g0[u,:]=np.fft.fft((f_ishift.conjugate())[u,:])
for v in range(0,n):                 # compute the 1-D Inverse DFT transform of each column
    g0[:,v]=np.fft.fft(g0[:,v])

g0=abs(g0.conjugate()/(m*n))
g=np.zeros([m,n],np.uint8)

for i in range(0,m):
    for j in range(0,n):
        g[i,j]=g0[i,j]*(im_gray.max()-im_gray.min())+im_gray.min()
        print(i,j)

d=im_gray-g
cv.imwrite('The image of f.png',im_gray)
cv.imwrite('The image of g.png',g)
cv.imwrite('The image of the difference between f and g.png',d)
