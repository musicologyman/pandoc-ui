import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Combo

INPUT_FORMATS = ["bibtex (BibTeX bibliography)",
                    "biblatex (BibLaTeX bibliography)",
                    "commonmark (CommonMark Markdown)",
                    "commonmark_x (CommonMark Markdown with extensions)",
                    "creole (Creole 1.0)",
                    "csljson (CSL JSON bibliography)",
                    "csv (CSV table)",
                    "docbook (DocBook)",
                    "docx (Word docx)",
                    "dokuwiki (DokuWiki markup)",
                    "epub (EPUB)",
                    "fb2 (FictionBook2 e-book)",
                    "gfm (GitHub-Flavored Markdown)",
                    "haddock (Haddock markup)",
                    "html (HTML)",
                    "ipynb (Jupyter notebook)",
                    "jats (JATS XML)",
                    "jira (Jira/Confluence wiki markup)",
                    "json (JSON version of native AST)",
                    "latex (LaTeX)",
                    "markdown (Pandoc’s Markdown)",
                    "markdown_mmd (MultiMarkdown)",
                    "markdown_phpextra (PHP Markdown Extra)",
                    "markdown_strict (original unextended Markdown)",
                    "mediawiki (MediaWiki markup)",
                    "man (roff man)",
                    "muse (Muse)",
                    "native (native Haskell)",
                    "odt (ODT)",
                    "opml (OPML)",
                    "org (Emacs Org mode)",
                    "rtf (Rich Text Format)",
                    "rst (reStructuredText)",
                    "t2t (txt2tags)",
                    "textile (Textile)",
                    "tikiwiki (TikiWiki markup)",
                    "twiki (TWiki markup)",
                    "vimwiki (Vimwiki)"]

OUTPUT_FORMATS = ["asciidoc (AsciiDoc)",
                    "asciidoctor (AsciiDoctor)",
                    "beamer (LaTeX beamer slide show)",
                    "bibtex (BibTeX bibliography)",
                    "biblatex (BibLaTeX bibliography)",
                    "commonmark (CommonMark Markdown)",
                    "commonmark_x (CommonMark Markdown with extensions)",
                    "context (ConTeXt)",
                    "csljson (CSL JSON bibliography)",
                    "docbook or docbook4 (DocBook 4)",
                    "docbook5 (DocBook 5)",
                    "docx (Word docx)",
                    "dokuwiki (DokuWiki markup)",
                    "epub (EPUB)", 
                    "epub2 (EPUB v2)",
                    "epub3 (EPUB v3 book)",
                    "fb2 (FictionBook2 e-book)",
                    "gfm (GitHub-Flavored Markdown)",
                    "haddock (Haddock markup)",
                    "html (HTML)", 
                    "html4 (XHTML 1.0 Transitional)",
                    "html5 (HTML, i.e. HTML5/XHTML polyglot markup)",
                    "icml (InDesign ICML)",
                    "ipynb (Jupyter notebook)",
                    "jats_archiving (JATS XML, Archiving and Interchange Tag Set)",
                    "jats_articleauthoring (JATS XML, Article Authoring Tag Set)",
                    "jats_publishing (JATS XML, Journal Publishing Tag Set)",
                    "jats (alias for jats_archiving)",
                    "jira (Jira/Confluence wiki markup)",
                    "json (JSON version of native AST)",
                    "latex (LaTeX)",
                    "man (roff man)",
                    "markdown (Pandoc’s Markdown)",
                    "markdown_mmd (MultiMarkdown)",
                    "markdown_phpextra (PHP Markdown Extra)",
                    "markdown_strict (original unextended Markdown)",
                    "mediawiki (MediaWiki markup)",
                    "ms (roff ms)",
                    "muse (Muse)",
                    "native (native Haskell)",
                    "odt (OpenOffice text document)",
                    "opml (OPML)",
                    "opendocument (OpenDocument)",
                    "org (Emacs Org mode)",
                    "pdf (PDF)",
                    "plain (plain text)",
                    "pptx (PowerPoint slide show)",
                    "rst (reStructuredText)",
                    "rtf (Rich Text Format)",
                    "texinfo (GNU Texinfo)",
                    "textile (Textile)",
                    "slideous (Slideous HTML and JavaScript slide show)",
                    "slidy (Slidy HTML and JavaScript slide show)",
                    "dzslides (DZSlides HTML5 + JavaScript slide show)",
                    "revealjs (reveal.js HTML5 + JavaScript slide show)",
                    "s5 (S5 HTML and JavaScript slide show)",
                    "tei (TEI Simple)",
                    "xwiki (XWiki markup)",
                    "zimwiki (ZimWiki markup)"]

def build_layout():
    return [[sg.Text("Input file:", size=(14, 1)),
             sg.Input(key="-INPUT-FILE-", size=(54, 1)),
             sg.FileBrowse("Browse", key="-FILEBROWSE-", enable_events=True, size=(6, 1))],
            [sg.Text("Output file:", size=(14, 1)),
             sg.Input(key="-OUTPUT-FILE-", size=(54, 1))],
            [sg.Text("Input Format:", size=(14, 1)),
             sg.Combo(INPUT_FORMATS, key="-INPUT-FORMAT-", size=(60, 12))],
            [sg.Text("Output Format:", size=(14, 1)),
             sg.Combo(OUTPUT_FORMATS, key="-OUTPUT-FORMAT-", size=(60,12))],
            [sg.Button("Convert", key="-CONVERT-", disabled=True)]]

def create_window(layout):
    return sg.Window("PANDOC Converter", layout=layout)

def main():

    sg.theme("BlueMono") 
    sg.set_options(font=("Arial", 14))

    window = create_window(build_layout())

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            print("event: {event}\nvalues: {values}", end="\n\n")
        
    window.close()

if __name__ == "__main__":
    main()
