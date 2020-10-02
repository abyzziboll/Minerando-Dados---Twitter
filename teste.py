from TwitterSearch import*
import csv
import io
try:

    ts = TwitterSearch(
        consumer_key = 'ZHJdF2y5k3SPavNJ343piIJH7',
        consumer_secret = 'TZP3wOYzSuJMGgzdDhFPXIsRgE6UDWPduwYiQqJ883W9qM1a1b',
        access_token = '1308552426941800453-J3rHkl3MfccZEy3RLTjbhTqpQw9qwP',
        access_token_secret = 'LJImhabi7TVibIKWhc5z1iDGMEwjDsJK0XfqALpD0IerJ'
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