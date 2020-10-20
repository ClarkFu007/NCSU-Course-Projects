% prob2-b
filter(1:98)=1;
filter(99:512)=0;
DFT_filter=fft(filter,512);
% prob2-c
data_block_1st(1:414)=1;
data_block_1st(415:512)=0;
DFT_data_block_1st=fft(data_block_1st,512);

% prob3-b
wr_n(1:30)=1;                   % The sequence of the rectangular window
n=0:30;
wh_n=0.5*(1-cos(2*pi*n/29));    % The sequence of the Hanning window
Wr_w=fft(wr_n,400);
Wh_w=fft(wh_n,400);
% Plot the magnitude and phase of the sampled spectra of the sequence of the rectangular window
y1_am=abs(Wr_w);
y1_ph=angle(Wr_w);
figure(1)
subplot(2,1,1)
stem(0:length(y1_am)-1,y1_am)
title('Sampled Spectrum of wr(n) for N=400 - Amplitude')
xlabel('k')
ylabel('Amplitude')
subplot(2,1,2)
stem(0:length(y1_ph)-1,y1_ph)
title('Sampled Spectrum of wr(n) for N=400 - Phase')
xlabel('k')
ylabel('Phase')
% Plot the magnitude and phase of the sampled spectra of the sequence of the Hanning window
y2_am=abs(Wh_w);
y2_ph=angle(Wh_w);
figure(2)
subplot(2,1,1)
stem(0:length(y2_am)-1,y2_am)
title('Sampled Spectrum of wh(n) for N=400 - Amplitude')
xlabel('k')
ylabel('Amplitude')
subplot(2,1,2)
stem(0:length(y2_ph)-1,y2_ph)
title('Sampled Spectrum of wh(n) for N=400 - Phase')
xlabel('k')
ylabel('Phase')

% prob3-c
% i.Use the rectangular window
n=0:49;                       % L=50
x10_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wr_n1(1:50)=1;
xr1=x10_n.*wr_n1;
Xr1=fft(xr1,2^14);
n=0:99;                       % L=100
x11_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wr_n2(1:100)=1;
xr2=x11_n.*wr_n2;
Xr2=fft(xr2,2^14);
n=0:149;                       % L=150
x12_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wr_n3(1:150)=1;
xr3=x12_n.*wr_n3;
Xr3=fft(xr3,2^14);
w=0:2^14-1;
figure(3)
subplot(3,1,1)                  % Plot the magnitude spectrum for Xr1(k)
plot(w,Xr1)
title('The magnitude spectrum for Xr1(k) L=50')
xlabel('k')
ylabel('Magnitude')
subplot(3,1,2)                  % Plot the magnitude spectrum for Xr2(k)
plot(w,Xr2)
title('The magnitude spectrum for Xr2(k) L=100')
xlabel('k')
ylabel('Magnitude')
subplot(3,1,3)                  % Plot the magnitude spectrum for Xr3(k)
plot(w,Xr3)
title('The magnitude spectrum for Xr3(k) L=150')
xlabel('k')
ylabel('Magnitude')
% ii.Use the Hanning window
n=0:49;                       % L=50
x20_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wh_n=0.5*(1-cos(2*pi*n/49));
xh1=x20_n.*wh_n;
Xh1=fft(xh1,2^14);
n=0:99;                       % L=100
x21_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wh_n=0.5*(1-cos(2*pi*n/99));
xh2=x21_n.*wh_n;
Xh2=fft(xh2,2^14);
n=0:149;                       % L=150
x22_n=cos(2*200*pi*n/1500)+cos(2*220*pi*n/1500)+cos(2*250*pi*n/1500);
wh_n=0.5*(1-cos(2*pi*n/149));
xh3=x22_n.*wh_n;
Xh3=fft(xh3,2^14);
w=0:2^14-1;
figure(4)
subplot(3,1,1)                  % Plot the magnitude spectrum for Xh1(k)
plot(w,Xh1)
title('The magnitude spectrum for Xh1(k) L=50')
xlabel('k')
ylabel('Magnitude')
subplot(3,1,2)                  % Plot the magnitude spectrum for Xh2(k)
plot(w,Xh2)
title('The magnitude spectrum for Xh2(k) L=100')
xlabel('k')
ylabel('Magnitude')
subplot(3,1,3)                  % Plot the magnitude spectrum for Xh3(k)
plot(w,Xh3)
title('The magnitude spectrum for Xh3(k) L=150')
xlabel('k')
ylabel('Magnitude')


% prob4-a
figure(5)
y1=sampdata;
stem(0:length(y1)-1,y1)
title('A sample input sequence')
xlabel('Sample Number')
ylabel('Amplitude')
% prob4-b
X_dct=dct(y1);
Mag_dct=abs(X_dct);
figure(6)
stem(0:length(Mag_dct)-1,Mag_dct)
title('The magnitudes of the DCT for the test sequence')
xlabel('Frequency (Radians)')
ylabel('Amplitude')


% prob4-c
n=length(y1);
y2=y1;
for j = n+1:1:2*n           % Extend the original sequence to make it even symmetric
    y2(j)=y1(2*n+1-j);
end
Y2=fft(y2,length(y2));      % Use a 2N point DFT to compute Y2
for k = 1:1:length(Y2)      % Multiply Y2 by relevant complex exponential
    Y2(k)=Y2(k)*exp(1)^(-1i*2*pi*k/(4*n));
end
Y2(n+1:2*n)=[];             % Extract the first N values
Mag_Y2=abs(Y2);
Abs_error=abs(Mag_dct-Mag_Y2);
figure(7)
stem(0:length(Abs_error)-1,Abs_error)
title('The absolute error between the implementation and the result from b')
xlabel('Frequency (Radians)')
ylabel('Absolute error')
figure(8)
stem(0:length(Mag_Y2)-1,Mag_Y2)
title('The magnitudes of the DCT for the test sequence')
xlabel('Frequency (Radians)')
ylabel('Amplitude')

% prob4-d
Mag_Y3=Mag_Y2;
Mag_Y3(1)=Mag_Y2(1)/sqrt(n);        % Change each coefficient according to the documentation
for k = 2:1:length(Y2)
    Mag_Y3(k)=Mag_Y2(k)/sqrt(n/2);
end
figure(9)
Abs_error=abs(Mag_dct-Mag_Y3);
stem(0:length(Abs_error)-1,Abs_error)
title('The absolute error between the implementation and the result from b')
xlabel('Frequency (Radians)')
ylabel('Absolute error')
figure(10)
stem(0:length(Mag_Y3)-1,Mag_Y3)
title('The magnitudes of the DCT for the test sequence')
xlabel('Frequency (Radians)')
ylabel('Amplitude')


