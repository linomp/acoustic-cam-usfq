function s = plotPartialSurf(x, y, z, plot_surf)
    
    s = surf(x,y,z);
    s.LineStyle= 'none';
    s.EdgeColor = 'none';
    s.FaceColor = 'interp';
    s.FaceAlpha = 0.6;
    colormap jet
    if(~plot_surf)
        s.FaceAlpha = 0;
    end 

end