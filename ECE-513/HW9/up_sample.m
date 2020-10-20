function b_new=up_sample(b,L,w)
num=length(b);
num1=L*num;               
b_new=zeros(1,num1);
b_new(1,1:L:num1)=b;     % Pad zeros accordingly
h_new=freqz(b_new,1,w);
hmag_new=abs(h_new);
figure(L)
plot(w/pi,hmag_new);
title('Magnitude Spectrum Plot')
xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude')
end
