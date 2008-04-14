# Kai Hendry
# License: GPL (latest version)
NAME=resume
SRC=$(NAME).html

all: pdf

pdf:
	prince --no-embed-fonts --debug -s wiki.css $(SRC)

clean :
	rm -f $(NAME).ps $(NAME).pdf $(NAME).txt $(NAME).rtf *.bak *.log

upload :
	scp $(NAME).pdf *.html hendry.iki.fi:/home/hendry/projects/shopping-list
