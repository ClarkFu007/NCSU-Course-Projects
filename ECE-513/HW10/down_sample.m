% To get v_n
function v_n=down_sample(x_n,h_b)
v_temp=conv(x_n,h_b);
v_n=v_temp(1,1:2:end);
end
