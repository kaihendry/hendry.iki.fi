# Kai Hendry
# License: GPL (latest version)                                                                                                                                         
NAME=resume
DOCBOOK=$(NAME).xml

all: rtf html ps pdf txt

fo: $(DOCBOOK)
	xmlto fo $(DOCBOOK)

rtf: $(DOCBOOK)
	docbook2rtf $(DOCBOOK)
	ln -s $(NAME).rtf $(NAME).doc || true

html: $(DOCBOOK)
	xmlto html-nochunks $(DOCBOOK)

ps: $(DOCBOOK)
	docbook2ps $(DOCBOOK)

pdf: fo
	fop resume.fo $(NAME).pdf

txt: $(DOCBOOK)
	docbook2txt $(DOCBOOK)
	unix2dos $(NAME).txt

clean :
	rm -f $(NAME).ps $(NAME).pdf $(NAME).txt $(NAME).rtf *.html *.bak *.log

upload :
	scp $(NAME).xml $(NAME).ps $(NAME).pdf $(NAME).txt $(NAME).rtf *.html hendry.iki.fi:/home/hendry/projects/shopping-list
