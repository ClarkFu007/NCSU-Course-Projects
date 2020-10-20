function ba=implement_sos_IIR(K,V)
ba=ones(1,6); % The coefficients [b0,b1,b2,a0,a1,a2]
ba(6)=K(2);
ba(5)=K(1)*(1+ba(6));
ba(3)=V(3);
ba(2)=V(2)+(K(1)*K(2)+K(1))*ba(3);
ba(1)=V(1)+V(2)*K(1)+V(3)*K(2);
return