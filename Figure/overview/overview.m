[sampledata,FS] = audioread('take_action.wav');
x = 1:1:26000;
y = sampledata(700:1:21700);
plot(y)

set(gca,'fontsize',20);

xlim([0,21000]);
xbounds = xlim();
set(gca, 'xtick', xbounds(1):1:xbounds(2));



set(gca,'xtick',[],'xticklabel',[])
set(gca,'ytick',[],'yticklabel',[])