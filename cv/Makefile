all: index.html resume.pdf

index.html: resume.html index.html.in
	m4 -PEIinc < index.html.in > index.html

resume.pdf: index.html
	prince index.html -o resume.pdf

clean:
	rm -f index.html resume.pdf
