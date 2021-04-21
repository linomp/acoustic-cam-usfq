clc; close all; clear all

% TODO fix hardcoded results file name
load('acMapGtr.mat');
load('underbrink_16.mat')
imgFile = 'gtr.png';

% BF path video
make_vid = 0;
v = VideoWriter('path_3d_2.avi','Motion JPEG AVI');
v.Quality = 100;
v.FrameRate = 10;

% toggle intensities surface on/off
plot_2d = 0;
plot_surf = 1;
plot_mics = 1;
labels_sz = 14;

% intensities surface
xgv = linspace(rg.x_min, rg.x_max, size(spl, 2));
ygv = linspace(rg.y_min, rg.y_max, size(spl, 1));

%spl = spl - max(max(spl)); % normalize map

spl = spl - min(min(spl)); % bring map back to 0 

[rgX, rgY] = meshgrid(xgv, ygv);
grid  

% scaling, maximizing
s = plotPartialSurf(rgX, rgY, spl, plot_surf);
h = get(gca,'DataAspectRatio');
if h(3) == 1
      set(gca,'DataAspectRatio',[1 1 1/max(h(1:2))])
else
      set(gca,'DataAspectRatio',[1 1 h(3)])
end
%alpha(0)
if plot_2d
    cb = colorbar;
    cb.Label.String = 'SPL [dB]'; 
    cb.Label.FontSize = labels_sz;
end
delete(s);

% mic positions
hold on
if plot_mics
    z_offset = 2*max(max(spl))*ones(size(X));
    mics = [X Y z_offset];
    plot3( mics(:,1), mics(:, 2), mics(:, 3), ... 
    'ko', 'linewidth', 2.5,'markerfacecolor','r','markersize',15)
end

% cam image
y = imread(imgFile);
img = imagesc([xgv(1) xgv(end)], [ygv(end) ygv(1)], y)

% orientation tweaks 
if plot_2d
    view(2); axis equal; axis tight; sz = 8;
else
    camorbit(-90,-15,'data',[1 0 0]); camorbit(60,0,'data',[0 1 0]); sz = 1; 
end
xlabel('x [m]', 'fontsize', labels_sz)
ylabel('y [m]', 'fontsize', labels_sz)
zlabel('SPL [dB]', 'fontsize', labels_sz)
%set(gca,'ZTickLabel',[]) % remove z-labels (illustration purposes)

%%
delete(img)

% beamformer path
n = 5;
m = 5;
l = []; 
s = [];
pt = [];

jSteps = 1:n:size(rgX,2);   
jSteps(end+1) = size(rgX,2); 

iSteps = 1:m:size(rgX,1);  
iSteps(end+1) = size(rgX,1); 

if make_vid
    open(v);
end

for j = jSteps(2:end)
    for i = 1%iSteps
        
        delete(pt)
        delete(l)
        for k = 1:size(mics, 1)
            l = [
                    l; plot3([mics(k,1), rgX(i,j)], [mics(k,2), rgY(i,j)], ... 
                    [mics(k,3) - 1e-2, spl(i,j)], 'linewidth', 1.5)
                ];
        end 
        if i == 1 
            xRange = i:i+m; 
        else
            xRange = i-m:i; 
        end 
        yRange = j-n:j; 
        s = plotPartialSurf(rgX(xRange, yRange), rgY(xRange, yRange), ...
                            spl(xRange, yRange), plot_surf);
        pt = plot3(rgX(i,j), rgY(i,j), 1.10*spl(i,j), 'ms', 'markerfacecolor', 'k', 'linewidth', sz, 'markersize', 2.5*sz);
        drawnow
        if make_vid
            frame = getframe(gcf);
            writeVideo(v,frame);
        end
    end  
end

if make_vid
    close(v);
end

