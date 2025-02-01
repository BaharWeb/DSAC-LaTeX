set terminal pdf
set output 'visual-calibrated.pdf'
set key on bottom right box
set xlabel 'similarity measures'
set ylabel 'empirical similarity'
set xrange [ 0 : 1 ] noreverse writeback
set yrange [ 1 : 5 ] noreverse writeback
f(x) = 0.74 + 3.312*x
g(x) = 1.174 + 2.892*x
plot 'calibrated.dat' using 2:1 pt 2 lc 8 title 'sim E,cal', 'calibrated.dat' using 3:1 pt 1 lc 8 title 'sim H,cal', f(x) title 'sim E,cal', g(x) title 'sim H,cal'		
