%% Prob1
% Part(a)
b=[0.0609 -0.3157 0.8410 -1.4378 1.7082 -1.4378 0.8410 -0.3157 0.0609];
a=[1.0 -0.8961 2.6272 -0.9796 2.1282 -0.0781 0.9172 0.0502 0.2602];
[sos,gain]=tf2sos(b,a);
% Part(c)
sos_change=gain^(1/4)*sos(1:4,1:3); % Distribute the gain evenly
sos(1:4,1:3)=sos_change;
% The 1st second section
K21=sos(1,6);
K11=sos(1,5)/(1+sos(1,6));
V31=sos(1,3);
V21=sos(1,2)-(K11*K21+K11)*V31;
V11=sos(1,1)-K11*V21-K21*V31;
% The 2nd second section
K22=sos(2,6);
K12=sos(2,5)/(1+sos(2,6));
V32=sos(2,3);
V22=sos(2,2)-(K12*K22+K12)*V32;
V12=sos(2,1)-K12*V22-K22*V32;
% The 3rd second section
K23=sos(3,6);
K13=sos(3,5)/(1+sos(3,6));
V33=sos(3,3);
V23=sos(3,2)-(K13*K23+K13)*V33;
V13=sos(3,1)-K13*V23-K23*V33;
% The 4th second section
K24=sos(4,6);
K14=sos(4,5)/(1+sos(4,6));
V34=sos(4,3);
V24=sos(4,2)-(K14*K24+K14)*V34;
V14=sos(4,1)-K14*V24-K24*V34;
K_parameters=[K21,K11;K22,K12;K23,K13;K24,K14];
V_parameters=[V31,V21,V11;V32,V22,V12;V33,V23,V13;V34,V24,V14];
%% Prob2
K1=[0.4545 0.5703];
V1=[1.2459 0.7137 -1.0];
K2=[-0.1963 0.8052];
V2=[-0.0475 -1.2347 1.0];
K3=[0.8273 0.8835];
V3=[-0.1965 0.3783 1.0];
% part(a)
  % implement_sos_IIR(K,V)
% part(b)
x_n=sampdata;
figure(1)
stem(0:length(x_n)-1,x_n)
title('x(n) The input sequence')
xlabel('n')
ylabel('Amplitude')
% part(c)
x_n=sampdata;
sos=zeros(3,6);
ba1=implement_sos_IIR(K1,V1);           % The 1st transfer function
sos(1,1:6)=ba1(1:6);
ba2=implement_sos_IIR(K2,V2);           % The 2nd transfer function
sos(2,1:6)=ba2(1:6);
ba3=implement_sos_IIR(K3,V3);           % The 3rd transfer function
sos(3,1:6)=ba3(1:6);
[h,~]=impz(sos);
y1_n=conv(x_n,h');
% part(d)
x_n=sampdata;
[NUM1,DEN1]=latc2tf(K1,V1);             % The 1st transfer function
s21_n=filter(NUM1,DEN1,x_n); 
[NUM2,DEN2]=latc2tf(K2,V2);             % The 2nd transfer function
s22_n=filter(NUM2,DEN2,s21_n);
[NUM3,DEN3]=latc2tf(K3,V3);             % The 3rd transfer function
y2_n=filter(NUM3,DEN3,s22_n);
% part(e)
figure(2)
stem(0:length(y1_n)-1,y1_n)
title('y1(n) The output sequence')
xlabel('n')
ylabel('Amplitude')
figure(3)
stem(0:length(y2_n)-1,y2_n)
title('y2(n) The output sequence')
xlabel('n')
ylabel('Amplitude')
y2_n(length(y2_n)+1:length(y1_n))=zeros(1,length(y1_n)-length(y2_n));
difference=abs(y1_n-y2_n);
figure(4)
stem(0:length(difference)-1,difference)
title('The difference between two y1(n) and y2(n)')
xlabel('n')
ylabel('Amplitude')
%% Prob3
% part(a)
% (i) and (ii)
w1=pi/4;
w2=3*pi/4;
M=(61-1)/2;
n1=-M:-1;
w_neg=0.42+0.5*cos(2*pi*(n1)/(2*M))+0.08*cos(4*pi*(n1)/(2*M));
b2_neg=(1/pi)*(sin(w2*(n1))./(n1)-sin(w1*(n1))./(n1));
n2=1:M-1;
w_pos=0.42+0.5*cos(2*pi*(n2)/(2*M))+0.08*cos(4*pi*(n2)/(2*M));
b2_pos=(1/pi)*(sin(w2*(n2))./(n2)-sin(w1*(n2))./(n2));
b2_31=1/2;
b2=[b2_neg b2_31 b2_pos];     % The required 61 samples for the desired impulse response
w_Blackman=[w_neg 1 w_pos];   % The required 61 samples for the Blackman window
b2=b2.*w_Blackman;            % Multiply the two sequences
% Plot the magnitude and phase response of the resulting filter
w=pi*(0:0.005:1.0);
h=freqz(b2,1,w);
hmag=abs(h);
hphase=angle(h);
tol=0.95*pi;
figure(5)   
subplot(2,1,1)  % Plot the magnitude response of the resulting filter
hmag=unwrap(hmag,tol);
plot(w,hmag)
title('Frequency Response Plot')
xlabel('Frequency (radians)')
ylabel('Magnitude')
subplot(2,1,2)  % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w,hphase)
title('Phase Response Plot')
xlabel('Frequency (radians)')
ylabel('Magnitude (decibels)')
% (iii)
order=60;
wn=[1/4 3/4];
w=window(@blackman,order+1);
b1=fir1(order,wn,'bandpass',w);
% Plot the magnitude and phase response of the resulting filter
w=pi*(0:0.005:1.0);
h=freqz(b1,1,w);
hmag=abs(h);
hphase=angle(h);
figure(6)   % Plot the magnitude response of the resulting filter
subplot(2,1,1)
hmag=unwrap(hmag,tol);
plot(w,hmag)
title('Frequency Response Plot')
xlabel('Frequency (radians)')
ylabel('Magnitude')
subplot(2,1,2)  % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w,hphase)
title('Phase Response Plot')
xlabel('Frequency (radians)')
ylabel('Magnitude (decibels)')
%% Prob4
hd=zeros(1,31);
hd(1:13)=ones(1,13);
hd(14)=0.9;
M=length(hd)-1;
N=2*M+1;
t=0:M;
s=exp(-1i*2*pi*M*t/N);
hw=s.*hd;
hw(M+2:N)=zeros(1,M);
for k=32:1:61 % Use the relationship H(-k)=conjugate(H(k))
   hw(k)=conj(hw(N+1+1-k)); 
end
b=real(ifft(hw));
a=1;
[h,w]=freqz(b,a,200);
hmag=abs(h);
hang=angle(h);
tol=0.99*pi;
figure(7)   % Plot the magnitude response of the resulting filter
subplot(2,1,1)
hmag=unwrap(hmag,tol);
plot(w,hmag)
title('Magnitude response plot for frequency sampling')
xlabel('Frequency (radians)')
ylabel('Magnitude')
subplot(2,1,2)  % Plot the phase response of the resulting filter
hang=unwrap(hang,tol);
plot(w,hang)
title('Phase response plot for frequency sampling')
xlabel('Frequency (radians)')
ylabel('Magnitude (decibels)')






















