# Kai Hendry
# License: GPL (latest version)                                                                                                                                         
NAME=resume
DOCBOOK=$(NAME).xml

all: rtf html ps pdf txt

rtf: $(DOCBOOK)
	docbook2rtf $(DOCBOOK)
	#echo "Making symlink for Word document"
	#ln -s $(NAME).rtf $(NAME).doc

html: $(DOCBOOK)
	docbook2html $(DOCBOOK)

ps: $(DOCBOOK)
	docbook2ps $(DOCBOOK)

pdf: $(DOCBOOK)
	docbook2pdf $(DOCBOOK)

txt: $(DOCBOOK)
	docbook2txt $(DOCBOOK)
	unix2dos $(NAME).txt

clean :
	rm -f $(NAME).ps $(NAME).pdf $(NAME).txt $(NAME).rtf *.html *.bak *.log

upload :
	echo Not used anymore
	scp $(NAME).xml $(NAME).ps $(NAME).pdf $(NAME).txt $(NAME).rtf *.html melkinpaasi.cs.helsinki.fi:public_html/cv
