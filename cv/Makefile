# License: GPL (latest version)                                                                                                                                         
# Author: Kai Hendry                                                                                                                                                    
# Email: hendry AT cs.helsinki.fi 

all: rtf html ps pdf txt

rtf: resume.xml
	docbook2rtf resume.xml

html: resume.xml
	docbook2html resume.xml

ps: resume.xml
	docbook2ps resume.xml

pdf: resume.xml
	docbook2pdf resume.xml

txt: resume.xml
	docbook2txt resume.xml

clean :
	rm -f resume.ps resume.pdf resume.txt resume.rtf *.html
upload :
	scp resume.ps resume.pdf resume.txt resume.rtf *.html melkinpaasi:public_html/cv
