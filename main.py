from libgen_api import LibgenSearch



def pesquisaLivro(pesquisa):
    s = LibgenSearch()
    results = s.search_title(pesquisa)
    print(results)

    
if __name__ == "__main__":
    pesquisaLivro("Pride and Prejudice")
