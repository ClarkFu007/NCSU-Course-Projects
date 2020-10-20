function v_n=hard_threshold(v_n,value)
num=length(v_n);
for n=1:1:num
    if abs(v_n(1,n))<value
        v_n(1,n)=0;
    end
end
end