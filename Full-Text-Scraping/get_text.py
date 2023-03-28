def get_text(url):
  r1 = r'<p>(.*?)</p>'
  r2 = r'(<a.*?</a>)|</b>|</span>|<strong>|</strong>|(<em>.*?</em>)|(<i>.*?</i>)|(<span.*?</span>)|(<br.*?/>)|(</a>.*?</span>)|(<font.*?</font>)|(<u>.*?</u>)|(<iframe.*?</iframe>)|(<script.*?</script>)|(<noscript.*?</noscript>)'
  request = Request(url, headers = header)
  response = urlopen(request)
  href = response.read()
  soup = BeautifulSoup(href, 'lxml').body
  text_0 = soup.find('article')
  text_1 = re.findall(r1, str(text_0))
  text_2 = re.sub(r2, "", str(text_1))
  response.close()
  return text_2
