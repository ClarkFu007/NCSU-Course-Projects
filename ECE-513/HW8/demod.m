function yout=demod(yt,Fs,Fc,B)
N=length(yt);                % The length of the signal 
t=(0:N-1)/Fs;
wc=2*pi*Fc;                  % Fc is the carrier frequency
st=yt'.*cos(wc*t);           % Demodulate the signal
order=20;                    % Choosing the number of order is a trade-off between the precision and the cost of the filter
wn=B/2/Fs;                   % The cut-off frequency
w=window(@hamming,order+1);  % I choose the Hamming window to guarantee less distortion in spite of more transition width
b=fir1(order,wn,'low',w);
yout= filter(b,1,st);        % Filter out all signals except the signal found in the baseband
sound(yout,Fs)               % Play the audio
end

