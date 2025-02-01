BIBPATH = ../bib
MDPATH = ../markdown
PLAINTEXTPATH = ../plaintext
DRAFTPATH = ../drafts
DATAPATH = ../data
SCRIPTPATH = scripts
TEXCHAPTERPATH = ../latex/contents/mainmatter
TIMEPREFIX = $(shell /bin/date +"%Y%m%d-%H%M-DRF-")
DOCXOPTIONS = -f markdown -t docx --metadata-file=word.yaml --number-sections --data-dir=./rendering/ --filter pandoc-crossref --filter pandoc-citeproc --bibliography=../bib/all/all.bib --lua-filter ./pagebreak.lua 
TEXOPTIONS = -f markdown -t latex --metadata-file=latex.yaml --wrap=preserve --top-level-division=chapter --number-sections --filter pandoc-crossref --filter pandoc-citeproc --biblatex --bibliography=../bib/all/all.bib --lua-filter ./pagebreak.lua 


docx:	bib md
	echo "docx"
	pandoc ${DOCXOPTIONS} -o ${TIMEPREFIX}introduction.docx ${MDPATH}/01-introduction.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=1 -o ${TIMEPREFIX}requirements.docx ${MDPATH}/02-requirements.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=2 -o ${TIMEPREFIX}sota.docx ${MDPATH}/03-sota.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}solution.docx ${MDPATH}/04-solution.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}awsm-re.docx ${MDPATH}/05-re.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}awsm-rm.docx ${MDPATH}/06-rm.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}awsm-ci.docx ${MDPATH}/07-ci.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}evaluation.docx ${MDPATH}/08-evaluation.fix.md 
	pandoc ${DOCXOPTIONS} --number-offset=3 -o ${TIMEPREFIX}conclusion.docx ${MDPATH}/09-conclusion.fix.md 
	echo "\n"
	rm ${MDPATH}/01-introduction.fix.md
	rm ${MDPATH}/02-requirements.fix.md
	rm ${MDPATH}/03-sota.fix.md
	rm ${MDPATH}/04-solution.fix.md
	rm ${MDPATH}/05-re.fix.md
	rm ${MDPATH}/06-rm.fix.md
	rm ${MDPATH}/07-ci.fix.md
	rm ${MDPATH}/08-evaluation.fix.md
	rm ${MDPATH}/09-conclusion.fix.md

sota-tables:
	python ${SCRIPTPATH}/sota_tables.py ${DATAPATH}/sota.csv ${MDPATH}/03-sota.md

tex:	bib md
	echo "tex"
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/introduction.pandoc.tex ${MDPATH}/01-introduction.fix.md 
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/requirements.pandoc.tex ${MDPATH}/02-requirements.fix.md 
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/sota.pandoc.tex ${MDPATH}/03-sota.fix.md 
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/solution.pandoc.tex ${MDPATH}/04-solution.fix.md
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/re.pandoc.tex ${MDPATH}/05-re.fix.md
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/rm.pandoc.tex ${MDPATH}/06-rm.fix.md
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/ci.pandoc.tex ${MDPATH}/07-ci.fix.md
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/evaluation.pandoc.tex ${MDPATH}/08-evaluation.fix.md
	pandoc ${TEXOPTIONS} -o ${TEXCHAPTERPATH}/conclusion.pandoc.tex ${MDPATH}/09-conclusion.fix.md
	echo "\n"
	echo "\n"
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/introduction.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/requirements.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/sota.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/solution.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/re.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/rm.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/ci.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/evaluation.pandoc.tex
	python3 ${SCRIPTPATH}/fix_latex.py ${TEXCHAPTERPATH}/conclusion.pandoc.tex
	rm ${MDPATH}/01-introduction.fix.md
	rm ${MDPATH}/02-requirements.fix.md
	rm ${MDPATH}/03-sota.fix.md
	rm ${MDPATH}/04-solution.fix.md
	rm ${MDPATH}/05-re.fix.md
	rm ${MDPATH}/06-rm.fix.md
	rm ${MDPATH}/07-ci.fix.md
	rm ${MDPATH}/08-evaluation.fix.md
	rm ${MDPATH}/09-conclusion.fix.md

bib:
	echo "bib"
	rm -f ${BIBPATH}/all/all.bib
	cat ${BIBPATH}/*.bib >> ${BIBPATH}/all/all.bib
#	python ${SCRIPTPATH}/remove_keys.py ${BIBPATH}/all/all.bib
	python3 ${SCRIPTPATH}/fix_bibtex.py ${BIBPATH}/all/all.bib

md:
	echo "md"
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/01-introduction.md ${MDPATH}/01-introduction.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/02-requirements.md ${MDPATH}/02-requirements.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/03-sota.md ${MDPATH}/03-sota.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/04-solution.md ${MDPATH}/04-solution.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/05-re.md ${MDPATH}/05-re.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/06-rm.md ${MDPATH}/06-rm.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/07-ci.md ${MDPATH}/07-ci.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/08-evaluation.md ${MDPATH}/08-evaluation.fix.md
	python ${SCRIPTPATH}/fix_pandoc_md.py ${MDPATH}/09-conclusion.md ${MDPATH}/09-conclusion.fix.md
	python ${SCRIPTPATH}/sota_tables.py ${DATAPATH}/sota.csv ${MDPATH}/03-sota.fix.md
	python ${SCRIPTPATH}/sota_tables.py ${DATAPATH}/sota.csv ${MDPATH}/08-evaluation.fix.md

outline:
	echo "outline"
	pandoc -f docx -t markdown -o ${MDPATH}/${TIMEPREFIX}outline.md --filter pandoc-crossref --filter pandoc-citeproc --bibliography=${BIBPATH}/introduction.bib ${DRAFTPATH}/outline.docx

grammarly:
	pandoc ${MDPATH}/01-introduction.md -t plain -o ${PLAINTEXTPATH}/01-introduction.txt
	pandoc ${MDPATH}/02-requirements.md -t plain -o ${PLAINTEXTPATH}/02-requirements.txt
	pandoc ${MDPATH}/03-sota.md -t plain -o ${PLAINTEXTPATH}/03-sota.txt 
	pandoc ${MDPATH}/04-solution.md -t plain -o ${PLAINTEXTPATH}/04-solution.txt
	pandoc ${MDPATH}/05-re.md -t plain -o ${PLAINTEXTPATH}/05-re.txt
	pandoc ${MDPATH}/06-rm.md -t plain -o ${PLAINTEXTPATH}/06-rm.txt
	pandoc ${MDPATH}/07-ci.md -t plain -o ${PLAINTEXTPATH}/07-ci.txt
	pandoc ${MDPATH}/08-evaluation.md -t plain -o ${PLAINTEXTPATH}/08-evaluation.txt
	pandoc ${MDPATH}/09-conclusion.md -t plain -o ${PLAINTEXTPATH}/09.conclusion.txt

