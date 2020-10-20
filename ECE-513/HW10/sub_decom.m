function y_n=up_sample(v_n,g_b)
n=length(v_n);
n=2*n;
v_temp=zeros(1,n);
v_temp(1,1:2:end)=v_n;
y_n=conv(v_temp,g_b);
end