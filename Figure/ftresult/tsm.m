
   A =[
 
    15        18         12         2
    12        4         12          18
    17        14         8         8
    5       13        11        5
    ];
 
    A=A(:,1:4);
    A=reshape(A,[4 1 4]);
 
    x={'OLA','WSOLA','PV','FFmpeg'};
    plotBarStackGroups(A,x);
    box on;
    %set(gca,'fontsize',16);
    ylabel('Number');