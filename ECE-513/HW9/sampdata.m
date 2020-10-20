% y = sampdata;
%
%   This function returns a sample data set to be used for multirate
%       signal processing problems.
%   The input data is filtered with a low pass filter to make it band
%       limited (cutoff frequency is set at 0.95*pi).

function y = sampdata

ntaps = 65;
f = [0.0 0.9 0.95 1.0];
mag = [ 1.0 1.0 0.7071 0.0];
b = fir2(ntaps, f, mag);
a = 1.0;
len1 = 128 + length(b) -1;
%
%  Generate the input sample sequence.
%
data = zeros(1,len1);
for k=16:48,
    data(1,k) = 5.0;
    data(1,(k+80)) = -5.0;
    end
y = filter(b, a, data);

return
