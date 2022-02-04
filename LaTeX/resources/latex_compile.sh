cd $1

# run it twice as longtable reports a change in row width...
# nasty mistake to find.....

pdflatex -interaction=nonstopmode $2 ;
pdflatex -interaction=nonstopmode $2 ;


if [ $? -eq 0 ]
 then
   rm *.dvi ;\
   rm *.ps ;\
   rm *.bbl ;\
   rm *.aux ;\
   rm *.blg ;\
   rm *.log ;\
   rm *.out ;
fi


#okular $2.pdf ;
