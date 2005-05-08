NAME=panache
DOCBOOK=$(NAME).xml

txt:
	docbook2txt $(DOCBOOK)

rtf:
	docbook2rtf $(DOCBOOK)

clean:
	rm -f $(NAME).txt $(NAME).rtf

all:
	txt rtf
