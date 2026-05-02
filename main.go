package main

import (
	"flag"
	"html/template"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/mmcdole/gofeed"
)

type feedgen struct {
	Flag struct {
		Link string
	}
	Feed *gofeed.Feed
}

type uaTransport struct {
	base http.RoundTripper
}

func (t *uaTransport) RoundTrip(r *http.Request) (*http.Response, error) {
	r = r.Clone(r.Context())
	r.Header.Set("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
	return t.base.RoundTrip(r)
}

func main() {
	feedgen := &feedgen{}
	// read -link flag
	flag.StringVar(&feedgen.Flag.Link, "link", "", "link to feed")

	flag.Parse()

	fp := gofeed.NewParser()
	fp.Client = &http.Client{Transport: &uaTransport{base: http.DefaultTransport}}
	url := flag.Arg(0)
	log.Println("parsing", url)
	var err error
	for i, delay := range []time.Duration{0, 5 * time.Second, 15 * time.Second, 30 * time.Second} {
		if delay > 0 {
			log.Printf("retry %d after %s", i, delay)
			time.Sleep(delay)
		}
		feedgen.Feed, err = fp.ParseURL(url)
		if err == nil {
			break
		}
		log.Printf("attempt %d failed: %v", i+1, err)
	}
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
