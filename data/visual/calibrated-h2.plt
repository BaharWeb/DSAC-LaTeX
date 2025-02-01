set terminal pdf
set output 'visual-calibrated-h2.pdf'
set key on bottom right box
set xlabel 'similarity measure'
set ylabel 'empirical similarity'
set xrange [ 0 : 1 ] noreverse writeback
set yrange [ 1 : 5 ] noreverse writeback
g(x) = 1.174 + 2.892*x
plot 'calibrated.dat' using 3:1 pt 1 lc 8 title 'sim H,cal', g(x) lc 8 title 'linear model' 	
