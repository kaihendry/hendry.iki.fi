# License: GPL (latest version)                                                                                                                                         
NAME=cv
DOCBOOK=$(NAME).xml

all: rtf html ps pdf txt

rtf: $(DOCBOOK)
	docbook2rtf $(DOCBOOK)

html: $(DOCBOOK)
	docbook2html $(DOCBOOK)

ps: $(DOCBOOK)
	docbook2ps $(DOCBOOK)

pdf: $(DOCBOOK)
	docbook2pdf $(DOCBOOK)

txt: $(DOCBOOK)
	docbook2txt $(DOCBOOK)

clean :
	rm -f resume.ps resume.pdf resume.txt resume.rtf *.html *.bak *.log
upload :
	scp resume.ps resume.pdf resume.txt resume.rtf *.html melkinpaasi.cs.helsinki.fi:public_html/cv
