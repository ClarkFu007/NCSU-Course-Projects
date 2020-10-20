%%
% prob1
xn=[4,-3,2,-1,-5,3,-1,0];
% prob1-a
Xk_a=zeros(1,8);
for k=0:1:7
    X00_k=fft(xn(1))+exp(-1i*pi*k)*fft(xn(5)); % X00_k=X000_k+e^(-j*pi*k)X001_k
    X01_k=fft(xn(3))+exp(-1i*pi*k)*fft(xn(7)); % X01_k=X010_k+e^(-j*pi*k)X011_k
    X10_k=fft(xn(2))+exp(-1i*pi*k)*fft(xn(6)); % X10_k=X100_k+e^(-j*pi*k)X101_k
    X11_k=fft(xn(4))+exp(-1i*pi*k)*fft(xn(8)); % X11_k=X110_k+e^(-j*pi*k)X111_k
    
    X0_k=X00_k+exp(-1i*0.5*pi*k)*X01_k;        % X0_k=X00_k+e^(-j*0.5*pi*k)X01_k
    X1_k=X10_k+exp(-1i*0.5*pi*k)*X11_k;        % X1_k=X10_k+e^(-j*0.5*pi*k)X11_k
    
    Xk_a(k+1)=X0_k+exp(-1i*0.25*pi*k)*X1_k;    % X_k=X0_k+e^(-j*0.25*pi*k)X1_k
end
w=0:7;
figure(1)          % Plot the magnitude spectrum for Xk_a          
plot(w,abs(Xk_a))
title('The magnitude of the resulting spectrum in part(a)')
xlabel('k')
ylabel('Magnitude')
% prob1-b
Xk_b=fft(xn,8);
w=0:7;
figure(2)          % Plot the magnitude spectrum for Xk_b          
plot(w,abs(Xk_b))
title('The magnitude of the resulting spectrum in part(b)')
xlabel('k')
ylabel('Magnitude')
figure(3)          % Plot the difference between Xk_a and Xk_b          
plot(w,abs(Xk_b)-abs(Xk_a))
title('The difference betweent results in part(a) and part(b)')
xlabel('k')
ylabel('Difference')
%%
% prob2
% prob1
xn=[4,-3,2,-1,-5,3,-1,0];
% prob1-a
Xk_a=zeros(1,8);
x00=[xn(1),xn(5)];
x01=[xn(3),xn(7)];
x10=[xn(2),xn(6)];
x11=[xn(4),xn(8)];

X00=fft(x00,2);                            % To calculate 2-point FFT of X00(k)
X01=fft(x01,2);                            % To calculate 2-point FFT of X01(k)
X10=fft(x10,2);                            % To calculate 2-point FFT of X10(k)
X11=fft(x11,2);                            % To calculate 2-point FFT of X11(k)
X00=[X00(1),X00(2),X00(1),X00(2)];         % Utilize the periodicity to get 4-point
X01=[X01(1),X01(2),X01(1),X01(2)];         % Utilize the periodicity to get 4-point
X10=[X10(1),X10(2),X10(1),X10(2)];         % Utilize the periodicity to get 4-point
X11=[X11(1),X11(2),X11(1),X11(2)];         % Utilize the periodicity to get 4-point

X0=zeros(1,8);
X1=zeros(1,8);
for k=0:1:3
 X0(k+1)=X00(k+1)+exp(-1i*0.5*pi*k)*X01(k+1);   % X0_k=X00_k+e^(-j*0.5*pi*k)X01_k
 X1(k+1)=X10(k+1)+exp(-1i*0.5*pi*k)*X11(k+1);   % X1_k=X10_k+e^(-j*0.5*pi*k)X11_k
end
X0=[X0(1),X0(2),X0(3),X0(4),X0(1),X0(2),X0(3),X0(4)]; % Utilize the periodicity to get 8-point
X1=[X1(1),X1(2),X1(3),X1(4),X1(1),X1(2),X1(3),X1(4)]; % Utilize the periodicity to get 8-point
Xk_a=zeros(1,8);
for k=0:1:7
 Xk_a(k+1)=X0(k+1)+exp(-1i*0.25*pi*k)*X1(k+1);    % X_k=X0_k+e^(-j*0.25*pi*k)X1_k
end

w=0:7;
figure(4)          % Plot the magnitude spectrum for Xk_a          
plot(w,abs(Xk_a))
title('The magnitude of the resulting spectrum in part(a)')
xlabel('k')
ylabel('Magnitude')
% prob1-b
Xk_b=fft(xn,8);
w=0:7;
figure(5)          % Plot the magnitude spectrum for Xk_b          
plot(w,abs(Xk_b))
title('The magnitude of the resulting spectrum in part(b)')
xlabel('k')
ylabel('Magnitude')
figure(6)          % Plot the difference between Xk_a and Xk_b          
plot(w,abs(Xk_a)-abs(Xk_b))
title('The difference betweent results in part(a) and part(b)')
xlabel('k')
ylabel('Difference')



















