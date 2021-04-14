import urllib
import urllib.request
import urllib.error


def url_esta_ativa(url):
    try:
        urllib.request.urlopen(url)
        return 'pode ser acessado'
    except urllib.error.URLError:
        return 'não pode ser acessado'


resultado = url_esta_ativa('http://pudim.com.br/')
print(f'O Site pudim.com.br {resultado}')