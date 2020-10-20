%% Pro1
f1=[0 0.05 0.1 0.15 0.2 0.4 0.6 0.8 1];
m1=[1 0.75 0.5 0.25 0.0 0.0 0.0 0.0 0];
% part(a)
% a.(i)
b1=fir2(100,f1,m1);   % Produce a 101 sample sequences x[n] who has required magnitude response 
w=pi*(0:0.005:1);
h1=freqz(b1,1,w);
hmag1=abs(h1);
figure(1)
plot(w/pi,hmag1);
title('Magnitude Spectrum Plot before down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
num1=length(b1);
b1_new=b1(1,1:2:num1);
h1_new=freqz(b1_new,1,w);
hmag1_new=abs(h1_new);
figure(2)
plot(w/pi,hmag1_new);
title('Magnitude Spectrum Plot after down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% a.(ii)
f2=[0 0.2 0.4 0.5 0.6 0.8 1];
m2=[1 0.6 0.2 0.0 0.0 0.0 0];
b2=fir2(100,f2,m2);   % Produce a 101 sample sequences x[n] who has required magnitude response     
w=pi*(0:0.005:1);
h2=freqz(b2,1,w);
hmag2=abs(h2);
figure(3)
plot(w/pi,hmag2);
title('Magnitude Spectrum Plot before down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
num2=length(b2);
b2_new=b2(1,1:2:num2);
h2_new=freqz(b2_new,1,w);
hmag2_new=abs(h2_new);
figure(4)
plot(w/pi,hmag2_new);
title('Magnitude Spectrum Plot after down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% a.(iii)
f3=[0 0.25 0.5 0.75 1];
m3=[1 2/3  1/3 0.0  0];
b3=fir2(100,f3,m3);    % Produce a 101 sample sequences x[n] who has required magnitude response    
w=pi*(0:0.005:1);
h3=freqz(b3,1,w);
hmag3=abs(h3);
figure(5)
plot(w/pi,hmag3);
title('Magnitude Spectrum Plot before down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
num3=length(b3);
b3_new=b3(1,1:2:num3);
h3_new=freqz(b3_new,1,w);
hmag3_new=abs(h3_new);
figure(6)
plot(w/pi,hmag3_new);
ylim([0 0.5])
title('Magnitude Spectrum Plot after down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% a.(iv)
f4=[0 0.2 0.4 0.6 0.8 1];
m4=[1 0.8 0.6 0.4 0.2 0];
b4=fir2(100,f4,m4);     % Produce a 101 sample sequences x[n] who has required magnitude response   
w=pi*(0:0.005:1);
h4=freqz(b4,1,w);
hmag4=abs(h4);
figure(7)
plot(w/pi,hmag4);
title('Magnitude Spectrum Plot before down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
num4=length(b4);
b4_new=b4(1,1:2:num4);
h4_new=freqz(b4_new,1,w);
hmag4_new=abs(h4_new);
figure(8)
plot(w/pi,hmag4_new);
ylim([0 0.6])
title('Magnitude Spectrum Plot after down sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% part(b)
f_b=[0 0.2 0.4 0.5 0.6 0.8 1];
m_b=[1 0.6 0.2 0.0 0.0 0.0 0];
b_b=fir2(100,f_b,m_b);    
w=pi*(0:0.005:1);
h_b=freqz(b_b,1,w);
hmag_b=abs(h_b);
figure(9)
plot(w/pi,hmag_b);
title('Magnitude Spectrum Plot before up sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
num=length(b_b);
% b.(i)
num0=2*num;
b_b1new=zeros(1,num0);
b_b1new(1,1:2:num0)=b_b;
h_b1new=freqz(b_b1new,1,w);
hmag_b1new=abs(h_b1new);
figure(10)
plot(w/pi,hmag_b1new);
title('Magnitude Spectrum Plot after up sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
% b.(ii)
num0=3*num;
b_b2new=zeros(1,num0);
b_b2new(1,1:3:num0)=b_b;
h_b2new=freqz(b_b2new,1,w);
hmag_b2new=abs(h_b2new);
figure(11)
plot(w/pi,hmag_b2new);
title('Magnitude Spectrum Plot after up sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
% b.(iii)
num0=4*num;
b_b3new=zeros(1,num0);
b_b3new(1,1:4:num0)=b_b;
h_b3new=freqz(b_b3new,1,w);
hmag_b3new=abs(h_b3new);
figure(12)
plot(w/pi,hmag_b3new);
title('Magnitude Spectrum Plot after up sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
% b.(iv)
num0=5*num;
b_b4new=zeros(1,num0);
b_b4new(1,1:5:num0)=b_b;
h_b4new=freqz(b_b4new,1,w);
hmag_b4new=abs(h_b4new);
figure(13)
plot(w/pi,hmag_b4new);
title('Magnitude Spectrum Plot after up sampling')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% Prob4
% part(a)
f=[0 0.1 0.2 0.3 0.4 0.5 0.6 0.8 1];
m=[1 0.8 0.6 0.4 0.2 0.0 0.0 0.0 0];
b=fir2(128,f,m);          % Use the Matlab routine fir2 
w=pi*(0:0.005:1);
h=freqz(b,1,w);
hmag=abs(h);
figure(1)                 %  Plot the magnitude response of the resulting signal
plot(w/pi,hmag);
title('Magnitude Spectrum Plot')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
%% part(b)          
b1_new=up_sample(b,2,w);      % L=2
b2_new=up_sample(b,3,w);      % L=3
b3_new=up_sample(b,4,w);      % L=4
%% part(c)
fs=10000;           % The sample rate
ws=0.25;            % The stop band edge frequency
wc=0.25-1500/fs;    % The cut-off frequency
delp=0.01;
dels=0.001;
fedge=[wc ws];
mval=[1 0];
dev=[delp dels];        
[A,Fo,Ao,W]=firpmord(fedge,mval,dev);
b_b=firpm(A,Fo,Ao,W);
w=pi*(0:0.005:1.0);
h_b=freqz(b_b,1,w);
hmag_b=abs(h_b);
hphase_b=angle(h_b);
tol=0.95*pi;
figure(5)   
subplot(2,1,1)      % Plot the magnitude response of the resulting filter
hmag_b=unwrap(hmag_b,tol);
plot(w/pi,hmag_b)
title('Magnitude Response Plot (firpm FIR filter)')
ylabel('Magnitude ')
xlabel('Frequency (\times\pi radians)')
subplot(2,1,2)      % Plot the phase response of the resulting filter
hphase_b=unwrap(hphase_b,tol);
plot(w/pi,hphase_b)
title('Phase Response Plot (firpm FIR filter)')
ylabel('Phase (radians)')
xlabel('Frequency (\times\pi radians)')
%% part(d)
y2_new= filter(b_b,1,b1_new); 
b0_new=zeros(1,length(y2_new));
b0_new(1,1:2:length(y2_new))=b;     % Align the sequences accordingly
stem(0:length(y2_new)-1,abs(y2_new-b0_new))
title('The absolute error between y2[n] and x[n/2]')
xlabel('Sample')
ylabel('Amplitude')
%% Prob5
% part(a)
Fs=10000;
Fpass=45;    
Fstop=50;
delp=0.01;
dels=0.001;
mval=[1 0];
dev=[delp dels];        
[A,Fo,Ao,W]=firpmord([Fpass Fstop],mval,dev,Fs);
b1=firpm(A,Fo,Ao,W);
%% part(b)
M_b1=10;M_b2=10;
F_b0=Fs;
F_b1=F_b0/M_b1;
F_b2=F_b1/M_b2;
% The first filter
Fpass_b1=Fpass;
Fstop_b1=F_b1-Fstop;
delp_b1=delp/2;
dels_b1=dels;
mval=[1 0];
dev=[delp_b1 dels_b1];        
[A,Fo,Ao,W]=firpmord([Fpass_b1 Fstop_b1],mval,dev,F_b0);
b_b1=firpm(A,Fo,Ao,W);
% The second filter
Fpass_b2=Fpass;
Fstop_b2=F_b2-Fstop;
delp_b2=delp/2;
dels_b2=dels;
mval=[1 0];
dev=[delp_b2 dels_b2];        
[A,Fo,Ao,W]=firpmord([Fpass_b2 Fstop_b2],mval,dev,F_b1);
b_b2=firpm(A,Fo,Ao,W);
%% part(c)
M_c1=25;M_c2=2;M_c3=2;
F_c0=Fs;
F_c1=F_c0/M_c1;
F_c2=F_c1/M_c2;
F_c3=F_c2/M_c3;
% The first filter
Fpass_c1=Fpass;
Fstop_c1=F_c1-Fstop;
delp_c1=delp/2;
dels_c1=dels;
mval=[1 0];
dev=[delp_c1 dels_c1];        
[A,Fo,Ao,W]=firpmord([Fpass_c1 Fstop_c1],mval,dev,F_c0);
b_c1=firpm(A,Fo,Ao,W);
% The second filter
Fpass_c2=Fpass;
Fstop_c2=F_c2-Fstop;
delp_c2=delp/2;
dels_c2=dels;
mval=[1 0];
dev=[delp_c2 dels_c2];        
[A,Fo,Ao,W]=firpmord([Fpass_c2 Fstop_c2],mval,dev,F_c1);
b_c2=firpm(A,Fo,Ao,W);
% The third filter
Fpass_c3=Fpass;
Fstop_c3=F_c3-Fstop;
delp_c3=delp/2;
dels_c3=dels;
mval=[1 0];
dev=[delp_c3 dels_c3];        
[A,Fo,Ao,W]=firpmord([Fpass_c3 Fstop_c3],mval,dev,F_c2);
b_c3=firpm(A,Fo,Ao,W);
%% part(d)
% Frequency response of single stage implementation in part(a)
w=pi*(0:0.005:1.0);
h1=freqz(b1,1,w);
hphase=angle(h1);
hmag=20*log10(abs(h1));
tol=0.5*pi;
figure(1)  
subplot(2,1,1)    % Plot the magnitude response of the resulting filter
plot(w/pi,hmag)
ylim([-400 0])
title('Magnitude Response Plot (firpm FIR single-stage filter)')
ylabel('Magnitude ')
xlabel('Frequency (\times\pi radians)')
subplot(2,1,2)    % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w/pi,hphase)
title('Phase Response Plot (firpm FIR single-stage filter)')
ylabel('Phase (radians)')
xlabel('Frequency (\times\pi radians)')
% Frequency response of multistage implementation in part(b)
b_b2_up=upsample(b_b2,M_b1);
h_casc_b=conv(b_b1,b_b2_up);
h2=freqz(h_casc_b,1,w);
hphase=angle(h2);
hmag=20*log10(abs(h2));
figure(2)  
subplot(2,1,1)    % Plot the magnitude response of the resulting filter
plot(w/pi,hmag)
title('Magnitude Response Plot (firpm FIR two-stage filter)')
ylabel('Magnitude ')
xlabel('Frequency (\times\pi radians)')
subplot(2,1,2)    % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w/pi,hphase)
title('Phase Response Plot (firpm FIR two-stage filter)')
ylabel('Phase (radians)')
xlabel('Frequency (\times\pi radians)')
% Frequency response of multistage implementation in part(c)
b_c2_up=upsample(b_c2,M_c1);
h_casc_c=conv(b_c1,b_c2_up);
b_c3_up=upsample(b_c3,M_c1*M_c2);
h_casc_c=conv(h_casc_c,b_c3_up);
h3=freqz(h_casc_c,1,w);
hphase=angle(h3);
hmag=20*log10(abs(h3));

figure(3)  
subplot(2,1,1)    % Plot the magnitude response of the resulting filter
plot(w/pi,hmag)
ylim([-400 0])
title('Magnitude Response Plot (firpm FIR three-stage filter)')
ylabel('Magnitude ')
xlabel('Frequency (\times\pi radians)')
subplot(2,1,2)    % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w/pi,hphase)
title('Phase Response Plot (firpm FIR three-stage filter)')
ylabel('Phase (radians)')
xlabel('Frequency (\times\pi radians)')
%% Prob6
% part(a)
b0=fir1(20,0.413);
w=pi*(0:0.005:1.0);
h1=freqz(b0,1,w);
hmag1=abs(h1);
hphase1=angle(h1);
tol=0.95*pi;
figure(1)  
subplot(2,1,1)   % Plot the magnitude response of the resulting filter
hmag1=unwrap(hmag1,tol);
plot(w/pi,hmag1)
title('Magnitude Response Plot (firpm FIR filter)')
ylabel('Magnitude ')
xlabel('Frequency (\times\pi radians)')
subplot(2,1,2)    % Plot the phase response of the resulting filter
hphase1=unwrap(hphase1,tol);
plot(w/pi,hphase1)
title('Phase Response Plot (firpm FIR filter)')
ylabel('Phase (radians)')
xlabel('Frequency (\times\pi radians)')
% part(b) Determine the coefficients for H1(z),H2(z), and H3(z)
b1=b0(1,1:3:end);
b2=b0(1,2:3:end);
b3=b0(1,3:3:end);
% part(c) Implement a filter using the 3-level polyphase decomposition
%% part(d)
x_n=sampdata;
figure(2)
stem(0:length(x_n)-1,x_n)
title('x(n) The input sequence')
xlabel('Sample number')
ylabel('Amplitude')

n0=length(b0)+3*length(x_n)-1;
% Implement the polyphase decomposition
s1=level3_filter(b1,x_n,1,n0);
s2=level3_filter(b2,x_n,2,n0);
s3=level3_filter(b3,x_n,3,n0);
y1_n=s1+s2+s3;
figure(3)
stem(0:length(y1_n)-1,y1_n)
title('Output y1(n) using polyphase with up sampling')
xlabel('Sample number')
ylabel('Amplitude')
% part(e) 
v=zeros(1,3*length(x_n));
v(1,1:3:end)=x_n;
y2_n=conv(b0,v);
figure(4)
stem(0:length(y2_n)-1,y2_n)
title('Output y2(n) using up sampling before filtering')
xlabel('Sample number')
ylabel('Amplitude')
%% part(f)
stem(0:length(y1_n)-1,abs(y1_n-y2_n))
title('The absolute error between two methods')
xlabel('Sample number')
ylabel('Absolute error')

































