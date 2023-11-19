package main

import (
	"flag"
	"html/template"
	"log"
	"os"

	"github.com/mmcdole/gofeed"
)

type feedgen struct {
	Flag struct {
		Link string
	}
	Feed *gofeed.Feed
}

func main() {
	feedgen := &feedgen{}
	// read -link flag
	flag.StringVar(&feedgen.Flag.Link, "link", "", "link to feed")

	flag.Parse()

	fp := gofeed.NewParser()
	url := flag.Arg(0)
	log.Println("parsing", url)
	var err error
	feedgen.Feed, err = fp.ParseURL(url)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("generating links for", feedgen.Feed.Title)

	const tmpl = `
	<h2><a href="{{ .Flag.Link}}">{{ .Feed.Title }}</a></h2>
	<ul>
	{{ range $i, $e := .Feed.Items -}}
	{{ if lt $i 10 }}
		<li><a href="{{ .Link }}">{{ .Title }}</a></li>
	{{- end }}
	{{- end }}
	</ul>`
	t := template.Must(template.New("").Parse(tmpl))
	err = t.Execute(os.Stdout, feedgen)
	if err != nil {
		log.Fatal(err)
	}
}
