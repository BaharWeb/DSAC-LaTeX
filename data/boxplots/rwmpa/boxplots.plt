#set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
set terminal pdf
set output 'rwmpa-boxplot.pdf'
set border 2 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.5 absolute
set style fill   solid 0.50 border lt -1
unset key
set style increment default
set pointsize 0.5
set style data boxplot
set xtics border in scale 0,0 nomirror norotate  autojustify
set xtics  norangelimit 
set xtics ("Q1" 1.0, "Q2" 2.0, "Q3" 3.0, "Q4" 4.0, "Q5" 5.0, "Q6" 6.0, "Q7" 7.0)
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set xrange [ 0.5 : 7.5 ] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [ 0.5 : 5.5 ] noreverse nowriteback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
set style boxplot medianlinewidth 2.5
set style boxplot outliers pointtype 2
## Last datafile plotted: "silver.dat"
plot for [i=1:7] 'rwmpa.dat' using (i):i lc rgb 'white'
