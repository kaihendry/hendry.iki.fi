resume.pdf: resume.html
	prince --no-embed-fonts resume.html

view: resume.pdf
	google-chrome-unstable resume.pdf

clean:
	rm -f resume.pdf
