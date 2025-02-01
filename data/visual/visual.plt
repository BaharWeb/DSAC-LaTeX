set terminal pdf
set output 'visual-scatter.pdf'
set key on bottom right box
set xlabel 'similarity measures'
set ylabel 'empirical similarity'
set xrange [ 0 : 1 ] noreverse writeback
set yrange [ 1 : 5 ] noreverse writeback
plot 'all.dat' using 11:17 pt 2 lc 8 title 'sim E/H', 'all.dat' using 14:17 pt 1 lc 8 title 'sim R'	
