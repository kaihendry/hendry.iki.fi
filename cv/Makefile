index.html: resume.html index.html.in
	m4 -PEIinc < index.html.in > index.html

resume.html: resume.md
	markdown resume.md > resume.html

resume.pdf: index.html
	prince index.html -o resume.pdf
