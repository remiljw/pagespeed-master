import requests
 
with open('thespeedurl.txt') as pagespeedurls:
    download_dir = 'pagespeed-results.csv'
    file = open(download_dir, 'w')
    content = pagespeedurls.readlines()
    content = [files.rstrip('\n') for files in content]
 
    columntitle = "URL, First interactive page\n"
    file.write(columntitle)
 
    # This is code in a google pagespeed api uses for loop to insert each url in .txt file
    for files in content:
        # If no  parameter is included, the query by default returns desktop detailed data.
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={files}&strategy=mobile'
        print(f'Requesting http files {x}...')
        r = requests.get(x)
        finalizing = r.json()
       
        try:
            url_id = finalizing['id']
            split = url_id.split('?') # This splits varaible splits the absolute_url from the api key parameter
            url_id = split[0] # This line of code reassigns url_id to the absolute_url
            Id = f'URL ~ {url_id}'
            Id2 = str(url_id)
            url_fcp = finalizing['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            fcp = f'first contentful paint ~ {str(url_fcp)}'
            fcp2 = str(url_fcp)
            url_fi = finalizing['lighthouseResult']['audits']['interactive']['displayValue']
            fi1 = f'First Interactive ~ {str(url_fi)}'
            fi2 = str(url_fi)
        except KeyError:
            print(f'<KeyError> request has one or more key value {files}.')
       
        try:
            row_data = f'{Id2},{fcp2},{fi2}\n'
            file.write(row_data)
        except NameError:
            print(f'<NameError> KeyError found {files}.')
            file.write(f'<KeyError> & <NameError>  nonexistant Key found ~ {files}.' + '\n')
       
        try:
            print(Id)
            print(fcp)
            print(fi1)
        except NameError:
            print(f'<NameError> KeyError found {files}.')
 
    file.close()