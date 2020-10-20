% prob1

t;                         % t from hwk3prob1data
xat;                       % xat from hwk3prob1data
figure(1)                  % plot the band pass signal xat
plot(t,xat,'k')
title('Bandpass(Modulated) Signal')
xlabel('Time')
ylabel('Amplitude')

figure(2)                           % sampled sequence xanT
deltaT=1e-6;
Ts=1/4000;                          % obtained from question(b)
tsampstep=Ts/deltaT;
xanT=xat(1:tsampstep:2.5*10^5+1);   % obtain every tsampstep samples from xat
n=0:1:2.5*10^5/250;
plot(n,xanT,'k')                    % plot the xanT sequence
title('xanT Obtained from Sampling xat')
xlabel('n')
ylabel('Amplitude')


n=0:1:2.5*10^5/250;
xanTcos=xanT.*cos(0.5*pi*n);
xanTsin=xanT.*sin(0.5*pi*n);
xIn=xanTcos(1:2:2.5*10^5/250+1);    % extract values when n is even
xQn=-xanTsin(2:2:2.5*10^5/250);     % extract values when n is odd
figure(3)
subplot(2,1,1)                      % plot the discrete sequences xIn
stem(0:length(xIn)-1,xIn)
title('xI(n) Obtained from Sampling xat')
xlabel('n')
ylabel('Amplitude')
subplot(2,1,2)
stem(0:length(xQn)-1,xQn)           % plot the discrete sequences xQn
title('xQ(n) Obtained from Sampling xat')
xlabel('n')
ylabel('Amplitude')

figure(4)
subplot(2,1,1)
stem(0:length(xIn_true)-1,xIn_true)
title('xI(n) Obtained from Sampling xI(t) Directly')
xlabel('n')
ylabel('Amplitude')
subplot(2,1,2)
stem(0:length(xQn_true)-1,xQn_true)
title('xQ(n) Obtained from Sampling xQ(t) Directly')
xlabel('n')
ylabel('Amplitude')

figure(4)
subplot(2,1,1)
stem(0:length(xIn_true)-1,xIn_true-xIn)        % the absolute error between the in-phase component and xIn_true
title('In-phase Component Absolute Error')
xlabel('n')
ylabel('Absolute Error')
subplot(2,1,2)
stem(0:length(xQn_true)-1,xQn_true-xQn)        % the absolute error between the quad-phase component and xQn_true
title('Quad-phase Component Absolute Error')
xlabel('n')
ylabel('Absolute Error')











