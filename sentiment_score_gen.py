import sys
import json
import csv


csv_file = "mycsv.csv"


def scores(afinn, text):
    scores = {}

    with afinn as fx:
        reader = csv.reader(fx, delimiter='\t')
        for row in reader:
           scores[row[0].strip()] = int(row[1].strip())

    with text as fy:
        for line in fy:
           tweet = json.loads(line)
           text = tweet.get('text','').encode('utf-8')
           if text:
              total_sent = sum(scores.get(word,0) for word in text.split())
              #print total_sent
              for word in text.split():
                if not scores.get(word,0):
                        no_score = -0.5
                        final_score = total_sent + no_score
                        sentiment_scores = ( "{} {}".format(word,final_score))
                        #print sentiment_scores
                        for row in sentiment_scores: 
                            out_csv = csv.writer(open(csv_file, 'wb'), delimiter=',', quoting=csv.QUOTE_NONE)      
                            out_csv.writerow(row)
                            out_csv.close()              


def main():
    tweet_text = open(sys.argv[1]) #use output.txt for first argv for initial testing 
    afinn = open(sys.argv[2]) #use AFINN.txt for second argv
    scores(afinn, tweet_text)

if __name__ == '__main__':
    main()
