all: index.html resume.pdf

resume.pdf: index.html
	prince index.html -o resume.pdf

resume.html: resume.md
	markdown resume.md > resume.html

index.html: resume.html index.html.in
	m4 -PEIinc < index.html.in > index.html

clean:
	rm -f index.html resume.pdf
