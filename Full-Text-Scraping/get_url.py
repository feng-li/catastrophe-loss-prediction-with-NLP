def get_url(query, year, month, pages):
    query = query.replace(' ', '+')
    url_0 = f"https://www.google.com/search?q={query}&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{year}%2Ccd_max%3A{month}%2F{year}"
    url_0_set = []
    for n in range(0, pages*10, 10):
        url_0_set.append(url_0 + f"&start={n}")
    
    url_set = []
    title_set = []
    date_set = []
    for n in range(pages):
        time.sleep(5)
        page = requests.Session().get(url_0_set[n], headers = header)
        tree = html.fromstring(page.text)
        
        requests.Session().keep_alive = False
        
        url = tree.xpath('//div[contains(@class,"Z26q7c UK95Uc jGGQ5e")]/div/a/@href')# '//div[contains(@class,"Z26q7c UK95Uc jGGQ5e")]/div/a/@href'
        for i in range(len(url)):
            if "https://translate.google.com" not in url[i]:
                url_set.append(url[i])
        
        title = tree.xpath('//div[@class="yuRUbf"]//a/h3/text()')
        for j in range(len(title)):
            title_set.append(title[j])
        
        date = tree.xpath('//div[contains(@class,"VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc")]//span/span[1]/text()')
        for k in range(len(date)):
            #if "年" not in date[k]:
            #    date[k] = 'None'
            date_set.append(date[k])
    
    flag_len = "not same length"
    if len(url_set) == len(title_set) == len(date_set):
        flag_len = "same length"
        
    page.close()
    
    return url_set, title_set, date_set, flag_len
