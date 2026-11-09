import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Stahovani skoncilo chybou: {r.status_code}")
        return []
    hrefs = []
    data = r.text
    odkazy_hrube = data.split("href=")
    for odkazy_ciste in odkazy_hrube[1:]:
        cast = odkazy_ciste.split('"')
        hrefs.append(cast[1])

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")