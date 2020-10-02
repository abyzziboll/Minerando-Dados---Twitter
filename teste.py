from TwitterSearch import*
import csv
import io
try:

    ts = TwitterSearch(
        consumer_key = 'sua consumer_key',
        consumer_secret = 'sua consumer_secret',
        access_token = 'sua access_token',
        access_token_secret = 'suaaccess_token_secret'
     )
    tso = TwitterSearchOrder()
    tso.set_keywords([':)'])
    tso.set_language('pt')
    tso.set_positive_attitude_filter()
    i=1
    lista = []
    
    with io.open("saida_positiva.csv","w",newline='',encoding="utf-8") as saida:
        escrever = csv.writer(saida)
        for tweet in ts.search_tweets_iterable(tso):
            #print( '@%s tweeted: %s\n' % ( tweet['user']['screen_name'], tweet['text'] ) )
            
            lista.append(tweet['text'])
            print(type(tweet['text']))
            i = i+1
        print(i)
        for j in range(0,(i-1)):
            escrever.writerow([lista[j]])

except TwitterSearchException as e:
    print(e)