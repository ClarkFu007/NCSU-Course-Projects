function s=level3_filter(b,x,level,n)
r=conv(b,x);
n1=length(r);
s=zeros(1,n);
n2=3*n1;
s(1,level:3:n2)=r;
end