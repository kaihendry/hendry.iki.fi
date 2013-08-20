resume.pdf: resume.html
	prince --no-embed-fonts --debug -s wiki.css resume.html

clean:
	rm -f resume.pdf

upload: resume.html resume.pdf
	scp resume.pdf resume.html hendry.iki.fi:/home/hendry/projects/shopping-list
