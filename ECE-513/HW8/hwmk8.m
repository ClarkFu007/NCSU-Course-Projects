%% Prob1
yt;                 % A signal of length N
Fs=88200;           % The sampling frequency in Hz
%%
sound(ypop,Fspop)
%%
sound(ycou,Fscountry)
%%
sound(yroc,Fsrock)
%%
yout_pop=demod(yt,Fs,10000,10000);
%%
yout_cou=demod(yt,Fs,20000,10000);
%%
yout_roc=demod(yt,Fs,30000,10000);
%% Magnitude spectrum
figure(1)
ypop_f=fft(ypop);
stem(0:length(ypop_f)-1,abs(ypop_f))
title('The magnitude spectrum of the original Pop')
xlabel('Sample Frequency')
ylabel('Amplitude')
figure(2)
ycou_f=fft(ycou);
stem(0:length(ycou_f)-1,abs(ycou_f))
title('The magnitude spectrum of the original Country')
xlabel('Sample Frequency')
ylabel('Amplitude')
figure(3)
yroc_f=fft(yroc);
stem(0:length(yroc_f)-1,abs(yroc_f))
title('The magnitude spectrum of the original Rock')
xlabel('Sample Frequency')
ylabel('Amplitude')
figure(4)
yout_pop_f=fft(yout_pop);
stem(0:length(yout_pop_f)-1,abs(yout_pop_f))
title('The magnitude spectrum of the filtered Pop')
xlabel('Sample Frequency')
ylabel('Amplitude')
figure(5)
yout_cou_f=fft(yout_cou);
stem(0:length(yout_cou_f)-1,abs(yout_cou_f))
title('The magnitude spectrum of the filtered Country')
xlabel('Sample Frquency')
ylabel('Amplitude')
figure(6)
yout_roc_f=fft(yout_roc);
stem(0:length(yout_roc_f)-1,abs(yout_roc_f))
title('The magnitude spectrum of the filtered Rock')
xlabel('Sample Frequency')
ylabel('Amplitude')
%% Absolute error plots
abs_error_pop=abs(ypop'-yout_pop);
abs_error_cou=abs(ycou'-yout_cou);
abs_error_roc=abs(yroc'-yout_roc);
figure(1)
stem(0:length(abs_error_pop)-1,abs_error_pop)
title('The absolute error plot of the Pop')
xlabel('Sample Number')
ylabel('Amplitude')
figure(2)
stem(0:length(abs_error_cou)-1,abs_error_cou)
title('The absolute error plot of the Country')
xlabel('Sample Number')
ylabel('Amplitude')
figure(3)
stem(0:length(abs_error_roc)-1,abs_error_roc)
title('The absolute error plot of the Rock')
xlabel('Sample Number')
ylabel('Amplitude')
%% Prob2
% Part(a)
B=[1.5000 6.9050 1.8880];   % The numerator of H(s)
A=[1.0000 5.0900 5.7114];   % The denominator of H(s)
[R,P,K]=residue(B,A);       % Expand H(s) into partial fractions
Ts=1.15;
Fs=1/Ts;
bs_a1=R(1);                   % Operate the H1(s)
as_a1=[1 -P(1)];
[BZ_a1,AZ_a1]=impinvar(bs_a1,as_a1,Fs);
bs_a2=R(2);                   % Operate the H2(s)
as_a2=[1 -P(2)];
[BZ_a2,AZ_a2]=impinvar(bs_a2,as_a2,Fs);
bs_a3=K;                      % Operate the H3(s)
% Get the transfer function
A1=conv(AZ_a1,AZ_a2);         % The denominator of the transfer function
B1=1.5*A1+[0 conv(BZ_a1,AZ_a2)]+[0 conv(BZ_a2,AZ_a1)]; % The numerator of the transfer function
% part(b)
bs_b1=R(1);                    % Operate the H1(s)
as_b1=[1 -P(1)];
[BZ_b1,AZ_b1]=bilinear(bs_b1,as_b1,Fs);
bs_b2=R(2);                    % Operate the H2(s)
as_b2=[1 -P(2)];
[BZ_b2,AZ_b2]=bilinear(bs_b2,as_b2,Fs);
bs_b3=K;                       % Operate the H3(s)
% Get the transfer function
A2=conv(AZ_b1,AZ_b2);          % The denominator of the transfer function
B2=1.5*A2+conv(BZ_b1,AZ_b2)+conv(BZ_b2,AZ_b1); % The numerator of the transfer function
% part(c)
w=pi*(0:0.005:0.5);
h=freqs(B,A,w);
h1=freqz(B1,A1,w);
h2=freqz(B2,A2,w);
hmag=abs(h);
hmag1=abs(h1);
hmag2=abs(h2);
figure(1)
plot(w,hmag,'r-');hold on;
plot(w,hmag1,'g--');hold on;
plot(w,hmag2,'b-.');hold on;
title('Magnitude Spectrum Plot')
xlabel('Normalized Frequency (radians)')
ylabel('Magnitude')
%% Prob3
% part(a)
A_z=1.9626^2*[1 2 1]+sqrt(2)*1.9626*[1 0 -1]+[1 -2 1];
A_z=A_z/7.6273;
B_z=[1 -2 1]/7.6273;
order=2;
wc=0.7;
[b0,a0]=butter(order,wc,'high');
% part(b)
[h,w]=freqz(B_z,A_z,200);
hmag=20*log10(abs(h));
figure(1)
plot(w,hmag);
title('Magnitude Plot');
xlabel('Frequency (radians)');
ylabel('Magnitude (dB)');
%% Prob4
% part(a)
% Get the transfer function
b=[0.1756 1];
a=[1 0.1756];
B_z=0.0803*conv(conv(a,a),conv(a,a))-0.1089*conv(conv(b,a),conv(a,a))+0.1666*conv(conv(b,b),conv(a,a))-0.1089*conv(conv(b,b),conv(b,a))+0.0803*conv(conv(b,b),conv(b,b));
A_z=1.0000*conv(conv(a,a),conv(a,a))+1.4655*conv(conv(b,a),conv(a,a))+1.7272*conv(conv(b,b),conv(a,a))+0.9687*conv(conv(b,b),conv(b,a))+0.3187*conv(conv(b,b),conv(b,b));
B_z=B_z/A_z(1);              % The numerator of the transfer function
A_z=A_z/A_z(1);              % The denominator of the transfer function
% part(b)
order=4;
[b2,a2]=ellip(order,1,34,0.7,'high'); % Use ellip to get the transfer function
% part(c)
[h,w]=freqz(B_z,A_z,200);
hmag=20*log10(abs(h));
figure(1)
plot(w,hmag);
title('Magnitude Plot');
xlabel('Frequency (radians)');
ylabel('Magnitude (dB)');
%% Prob5
% part(a)
fs=44056;                              % The sampling frequency
delt=2/fs;
wc1=delt*4000;                         % The pass band edge1
wc2=delt*18000;                        % The pass band edge2
ws1=delt*2000;                         % The stop band edge1
ws2=delt*20000;                        % The stop band edge2
delp=0.15;                             % Pass band ripple
dels=0.01;                             % Stop band ripple
fedge=[ws1 wc1 wc2 ws2];
mval=[0 1 0];
dev=[0.85*dels 0.9*delp 0.85*dels];
[A,Fo,Ao,W]=firpmord(fedge,mval,dev);
b=firpm(A,Fo,Ao,W);
% part(b)
w=pi*(0:0.005:1.0);
h=freqz(b,1,w);
hmag=abs(h);
hphase=angle(h);
tol=0.95*pi;
figure(3)   
subplot(2,1,1)  % Plot the magnitude response of the resulting filter
hmag=unwrap(hmag,tol);
plot(w,hmag)
title('Magnitude Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude')
subplot(2,1,2)  % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w,hphase)
title('Phase Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude (decibels)')
%% part(c)
figure(4)   % Plot the magnitude response of the resulting filter
hmag=unwrap(hmag,tol);
plot(w,hmag)
ylim([0 1.25])
title('Magnitude Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude')
line([0,3.5],[1.19,1.19],'linestyle','--','color','g');
text(0.5,1.19,'1.19','FontWeight','bold','Color','g','horiz','center','vert','bottom')
line([0,3.5],[0.81,0.81],'linestyle','--','color','g');
text(0.4,0.8,'0.81','FontWeight','bold','Color','g','horiz','center','vert','bottom')
line([0,3.5],[0.02,0.02],'linestyle','--','color','m');
text(0.2,0.02,'0.02','FontWeight','bold','Color','m','horiz','center','vert','bottom')
text(3,0.02,'0.02','FontWeight','bold','Color','m','horiz','center','vert','bottom')
%part(c),part(d)
fs=44056;
delt=2/fs;
wc1=delt*4000;
wc2=delt*18000;
ws1=delt*2000;
ws2=delt*20000;
delp=0.15;
dels=0.01;
fedge=[ws1 wc1 wc2 ws2];
mval=[0 1 0];
dev=[0.5*dels 0.45*delp 0.5*dels];        % Modify the weighting parameters
[A,Fo,Ao,W]=firpmord(fedge,mval,dev);
b=firpm(A,Fo,Ao,W);
w=pi*(0:0.005:1.0);
h=freqz(b,1,w);
hmag=abs(h);
hphase=angle(h);
tol=0.95*pi;
figure(5)   % Plot the magnitude response of the resulting filter
hmag=unwrap(hmag,tol);
plot(w,hmag)
ylim([0 1.25])
title('Magnitude Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude')
line([0,3.5],[1.15,1.15],'linestyle','--','color','g');
text(0.5,1.15,'1.15','FontWeight','bold','Color','g','horiz','center','vert','bottom')
line([0,3.5],[0.85,0.85],'linestyle','--','color','g');
text(0.4,0.85,'0.85','FontWeight','bold','Color','g','horiz','center','vert','bottom')
line([0,3.5],[0.01,0.01],'linestyle','--','color','m');
text(0.2,0.02,'0.01','FontWeight','bold','Color','m','horiz','center','vert','bottom')
text(3,0.02,'0.01','FontWeight','bold','Color','m','horiz','center','vert','bottom')
figure(6)   
subplot(2,1,1)  % Plot the magnitude response of the resulting filter
hmag=unwrap(hmag,tol);
plot(w,hmag)
title('Magnitude Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude')
subplot(2,1,2)  % Plot the phase response of the resulting filter
hphase=unwrap(hphase,tol);
plot(w,hphase)
title('Phase Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude (decibels)')
%% part(e)
figure(7)   
hmag=unwrap(hmag,tol);
plot(w,hmag)
ylim([0 1.25])
title('Magnitude Response Plot')
xlabel('Frequency (rad/sample)')
ylabel('Magnitude')
line([0,3.5],[0.92,0.92],'linestyle','--','color','g');
line([0.57,0.57],[0,1.25],'linestyle','--','color','g');
line([2.57,2.57],[0,1.25],'linestyle','--','color','g');
text(0.69,0.02,'0.57','FontWeight','bold','Color','g','horiz','center','vert','bottom')
text(2.69,0.02,'2.57','FontWeight','bold','Color','g','horiz','center','vert','bottom')
line([0,3.5],[0.01,0.01],'linestyle','--','color','m');
line([0.3,0.3],[0,1.25],'linestyle','--','color','m');
line([2.83,2.83],[0,1.25],'linestyle','--','color','m');
text(0.2,0.02,'0.3','FontWeight','bold','Color','m','horiz','center','vert','bottom')
text(2.95,0.02,'2.83','FontWeight','bold','Color','m','horiz','center','vert','bottom')


























