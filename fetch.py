import urllib2
import pickle

results = {}
for s in ["M", "W"]:
    i = 1
    while True:
        url = 'https://www.laufen.de/lauf-rangliste?event=BLM&meeting=9999991C957AD40000000015&page=%d&sex=%s' % (i, s)
        response = urllib2.urlopen(url)
        html = response.read()
        print url, len(html)
        results[url] = html
        i = i + 1
        if 'Ihre Suche ergab leider keine Ergebnisse.' in html:
            print "No results"
            break
        
        with open('raw_m_2011.pkl', 'wb') as f:
            pickle.dump(results, f)
    
