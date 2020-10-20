% prob2-b
x=[3,0,-1,2];
y=[1,5,4,-2];
Z1=fft(x,4).*fft(y,4); % multiply the spectrum of x by y with the use of fft
z1=ifft(Z1,4);          % obtain the result of circular convolution with the use of ifft
% prob2-c
z2=conv(x,y);
% prob2-d
Z3=fft(x,7).*fft(y,7);
z3=ifft(Z3,7);

% prob3
y=sampdata;
figure(1)
stem(0:length(y)-1,y)
title('x(n) The input sequence')
xlabel('n')
ylabel('Amplitude')
%(b) Design a 32 coefficient low pass FIR filter
order=32; 
ws=0.749; 
wc=0.85*ws; 
F=[0.0 wc ws 1.0]; 
A=[1.0 0.95 0.01 0.0]; 
b=firpm(order, F, A);
%(c) Plot the magnitude and phase response of the resulting filter
w=pi*(0:0.005:1.0);
h=freqz(b,A,w);
hmag=abs(h);
hphase=angle(h);
figure(2)   % Plot the magnitude response of the resulting filter
plot(w,hmag)
title('Frequency Response Plot')
xlabel('Normalized Frequency (radians)')
ylabel('Magnitude')
figure(3)   % Plot the phase response of the resulting filter
plot(w,hphase)
title('Phase Response Plot')
xlabel('Normalized Frequency (radians)')
ylabel('Magnitude')
%(d) Plot the output of the filter by using cov
[h,t]=impz(b,A); % Calculate impulse response of the filter
y1n=conv(y,h');  % use conv to get y1(n)
figure(4)        % Plot the output sequence y1(n) of the filter 
length(y1n);
stem(0:length(y1n)-1,y1n)
title('y1(n) The output sequence')
xlabel('n')
ylabel('Amplitude')
%(e) Plot the output of the filter by using fft and ifft
Y2=fft(y,length(y1n)).*fft(h',length(y1n));
y2n=ifft(Y2,length(y1n));  % use fft and ifft to get y1(n)
figure(5)        % Plot the output sequence y2(n) of the filter
length(y2n);
stem(0:length(y2n)-1,y2n)
title('y2(n) The output sequence')
xlabel('n')
ylabel('Amplitude')
%(f) Plot the error between y1(n) and y2(n)
figure(6)      % Plot the absolute error between y1(n) and y2(n)
error=abs(y1n-y2n);
stem(0:length(error)-1,error)
title('The absolute error between y1(n) and y2(n)')
xlabel('n')
ylabel('Absolute error')

