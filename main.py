from libgen_api import LibgenSearch



def pesquisaLivro(pesquisa,filtros):
    s = LibgenSearch()
    if filtros:
        results = s.search_title_filtered(pesquisa,filtros,exact_match=True)
    else:
        results = s.search_title(pesquisa)
    input("print, download?"))
    urlretrieve(url, filename)


if __name__ == "__main__":
    filtros={

    }
    pesquisa = input("Nome do Livro:")
    ano = input("Qual ano?")
    ext = input("Extensão:")
    if ano:
        filtros["Year"] = ano
    if ext:
        filtros["Extension"] = ext
    print(filtros)
    
    pesquisaLivro(pesquisa,filtros)
