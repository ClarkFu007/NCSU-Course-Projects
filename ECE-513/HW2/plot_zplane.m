% Read in the unstable filter
b1=[0.8581 4.2134 9.5802 9.5802 4.2134 0.8581];
a1=[1.0000 3.0937 5.5700 5.2578 2.0294 0.1642];
zplane(b1,a1) % pole/zero plot of the unstable filter
% Compute the frequency response using the Matlab function freqz
n=0:199;
w=n*pi/199;
h=freqz(b1,a1,w);
hmag=abs(h);
hphase=angle(h);
% Plot the results
figure(2) % Magnitude
plot(w,hmag)
title('Frequency Response Plot')
xlabel('Normalized Frequency (radians/sample)')
ylabel('Magnitude')
print -dps iirfreq.ps
figure(3) % Phase
plot(w,hphase)
title('Phase Response Plot')
xlabel('Normalized Frequency (radians/sample)')
ylabel('Phase')
print -dps iirphase.ps
% Read in the stable filter
b2=[0.3588 1.7617 4.0056 4.0056 1.7617 0.3588];
a2=[1.0000 2.2817 2.2179 1.2507 0.3782 0.0287];
zplane(b2,a2) % pole/zero plot of the stable filter
% Compute the frequency response using the Matlab function freqz
n=0:199;
w=n*pi/199;
h=freqz(b2,a2,w);
hmag=abs(h);
hphase=angle(h);
% Plot the results
figure(5) % Magnitude
plot(w,hmag)
title('Frequency Response Plot')
xlabel('Normalized Frequency (radians/sample)')
ylabel('Magnitude')
print -dps iirfreq.ps
figure(6) % Phase
plot(w,hphase)
title('Phase Response Plot')
xlabel('Normalized Frequency (radians/sample)')
ylabel('Phase')
print -dps iirphase.ps
