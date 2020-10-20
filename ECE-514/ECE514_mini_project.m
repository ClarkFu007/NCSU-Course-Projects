%% Operate the data
rng(1552,'twister')
BER_true=0.5*erfc(sqrt(0.5));
alpha=1-0.683;
y_half_a=norminv(1-alpha/2);
%Use the known variance of X
lower_confi_boud11_k=zeros(1,100);
upper_confi_boud11_k=zeros(1,100);
lower_confi_boud12_k=zeros(1,100);
upper_confi_boud12_k=zeros(1,100);
lower_confi_boud13_k=zeros(1,100);
upper_confi_boud13_k=zeros(1,100);
trial_11=zeros(1,100);
trial_12=zeros(1,100);
trial_13=zeros(1,100);
M11=zeros(1,100);
M12=zeros(1,100);
M13=zeros(1,100);
for m=1:1:100
X11=randn(1,10)-ones(1,10);
X12=randn(1,100)-ones(1,100);
X13=randn(1,1000)-ones(1,1000);
for i=1:1:10
    if X11(i)>0
        X11(i)=1;
    else
        X11(i)=0;
    end
end
for i=1:1:100
    if X12(i)>0
        X12(i)=1;
    else
        X12(i)=0;
    end
end
for i=1:1:1000
    if X13(i)>0
        X13(i)=1;
    else
        X13(i)=0;
    end
end
M11(m)=mean(X11);                  % The sample mean of X11
M12(m)=mean(X12);                  % The sample mean of X12
M13(m)=mean(X13);                  % The sample mean of X13
V=BER_true-BER_true^2;             % The true variance of X

lower_confi_boud11_k(m)=M11(m)-sqrt(V)*y_half_a/sqrt(10);
upper_confi_boud11_k(m)=M11(m)+sqrt(V)*y_half_a/sqrt(10);
lower_confi_boud12_k(m)=M12(m)-sqrt(V)*y_half_a/sqrt(100);
upper_confi_boud12_k(m)=M12(m)+sqrt(V)*y_half_a/sqrt(100);
lower_confi_boud13_k(m)=M13(m)-sqrt(V)*y_half_a/sqrt(1000);
upper_confi_boud13_k(m)=M13(m)+sqrt(V)*y_half_a/sqrt(1000);
end
for m=1:1:100
    if ((lower_confi_boud11_k(m)<=BER_true)&&(BER_true<=upper_confi_boud11_k(m)))
        trial_11(m)=1;
    end
    if ((lower_confi_boud12_k(m)<=BER_true)&&(BER_true<=upper_confi_boud12_k(m))) 
        trial_12(m)=1;
    end
    if ((lower_confi_boud13_k(m)<=BER_true)&&(BER_true<=upper_confi_boud13_k(m)))
        trial_13(m)=1;
    end
end
mean(trial_11)
mean(trial_12)
mean(trial_13)
% Use the unknown variance of X
lower_confi_boud21_k=zeros(1,100);
upper_confi_boud21_k=zeros(1,100);
lower_confi_boud22_k=zeros(1,100);
upper_confi_boud22_k=zeros(1,100);
lower_confi_boud23_k=zeros(1,100);
upper_confi_boud23_k=zeros(1,100);
trial_21=zeros(1,100);
trial_22=zeros(1,100);
trial_23=zeros(1,100);
M21=zeros(1,100);
M22=zeros(1,100);
M23=zeros(1,100);
for m=1:1:100
X21=randn(1,10)-ones(1,10);
X22=randn(1,100)-ones(1,100);
X23=randn(1,1000)-ones(1,1000);
for i=1:1:10
    if X21(i)>0
        X21(i)=1;
    else
        X21(i)=0;
    end
end
for i=1:1:100
    if X22(i)>0
        X22(i)=1;
    else
        X22(i)=0;
    end
end
for i=1:1:1000
    if X23(i)>0
        X23(i)=1;
    else
        X23(i)=0;
    end
end

M21(m)=mean(X21);                       % The sample mean of X21
M22(m)=mean(X22);                       % The sample mean of X22
M23(m)=mean(X23);                       % The sample mean of X23
V1=(10*M21(m)-10*(M21(m))^2)/9;         % The sample variance of X21
V2=(100*M22(m)-100*(M22(m))^2)/99;      % The sample variance of X22
V3=(1000*M23(m)-1000*(M23(m))^2)/999;   % The sample variance of X23

lower_confi_boud21_k(m)=M21(m)-sqrt(V1)*y_half_a/sqrt(10);
upper_confi_boud21_k(m)=M21(m)+sqrt(V1)*y_half_a/sqrt(10);
lower_confi_boud22_k(m)=M22(m)-sqrt(V2)*y_half_a/sqrt(100);
upper_confi_boud22_k(m)=M22(m)+sqrt(V2)*y_half_a/sqrt(100);
lower_confi_boud23_k(m)=M23(m)-sqrt(V3)*y_half_a/sqrt(1000);
upper_confi_boud23_k(m)=M23(m)+sqrt(V3)*y_half_a/sqrt(1000);
end
for m=1:1:100
    if ((lower_confi_boud21_k(m)<=BER_true)&&(BER_true<=upper_confi_boud21_k(m)))
        trial_21(m)=1;
    end
    if ((lower_confi_boud22_k(m)<=BER_true)&&(BER_true<=upper_confi_boud22_k(m))) 
        trial_22(m)=1;
    end
    if ((lower_confi_boud23_k(m)<=BER_true)&&(BER_true<=upper_confi_boud23_k(m)))
        trial_23(m)=1;
    end
end
mean(trial_21)
mean(trial_22)
mean(trial_23)
%% Use the data to draw figures
%% The sample mean of X with known variance 
figure(1)   % n=10       
X=1:10;
plot(X,M11(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud11_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud11_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([-0.2 0.7])
title({'The plot with known variance when n=10';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')

figure(2)   % n=100
X=1:10;
plot(X,M12(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud12_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud12_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([0.06 0.26])
title({'The plot with known variance when n=100';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')

figure(3)   % n=1000
X=1:10;
plot(X,M13(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud13_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud13_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([0.12 0.20])
title({'The plot with known variance when n=1000';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')
%% The sample mean of X with unknown variance 
figure(4)   % n=10
X=1:10;
plot(X,M21(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud21_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud21_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([-0.2 0.7])
title({'The plot with unknown variance when n=10';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')

figure(5)   % n=100
X=1:10;
plot(X,M22(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud22_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud22_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([0.06 0.26])
title({'The plot with unknown variance when n=100';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')

figure(6)   % n=1000
X=1:10;
plot(X,M23(1:10),'ro','MarkerSize',5,'MarkerFaceColor','r');hold on;
plot(X,lower_confi_boud23_k(1:10),'gv','MarkerSize',5,'MarkerFaceColor','g');hold on;
plot(X,upper_confi_boud23_k(1:10),'g^','MarkerSize',5,'MarkerFaceColor','g');hold on;
xlim([0 11])
ylim([0.12 0.20])
title({'The plot with unknown variance when n=1000';'(The true BER is 0.1587)'})
xlabel('The ith trial')
ylabel('Sample values')
line([0,11],[0.1587,0.1587],'linestyle','--','color','b');
text(5.5,0.16,'0.1587','FontWeight','bold','Color','b','horiz','center','vert','bottom')
