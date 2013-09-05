import sys
import json
import csv



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
                        no_score = 0
                        final_score = total_sent + no_score
                        words = ("{}".format(word))
                        sent_score = ("{}".format(final_score))
                        sentiment_scores = ( "{} {}".format(word,final_score))
                        print sentiment_scores

'''
    # open a file to write (mode "w"), and create a CSV writer object
    csvfile = file("output.csv", "w")
    csvwriter = csv.writer(csvfile)

    # add headings to our CSV file
    row = ["words", "sent_score" ]
    csvwriter.writerow(row)

    row = [ words, sent_score]
    csvwriter.writerow(row)

    csvfile.close()                    
'''

def main():
    tweet_text = open(sys.argv[1]) #use output.txt for initial testing 
    afinn = open(sys.argv[2]) #use AFINN.txt for second argv
    scores(afinn, tweet_text)

if __name__ == '__main__':
    main()
