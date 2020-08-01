clear all;
[sampledata,FS] = audioread('11.wav');
x = 1:1:32768;
y = sampledata(1:1:32768);
plot(y)

set(gca,'fontsize',20);

xlim([0,32768]);
xbounds = xlim();
set(gca, 'xtick', xbounds(1):1:xbounds(2));
set(gca,'fontsize',20);



set(gca,'xtick',[],'xticklabel',[])
set(gca,'ytick',[],'yticklabel',[])