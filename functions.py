import pymongo, datetime

client = pymongo.MongoClient()
db = client.budget
current_week = db.current_week


def insertCurrentWeek(lunch,party_beers,out_about):
    todays_date = datetime.datetime.today()
    print(todays_date)
    current_week.insert({
                         "date" : todays_date,
                         "UCT_lunch" : lunch,
                         "party_beers" : party_beers,
                         "out_about" : out_about
    })
