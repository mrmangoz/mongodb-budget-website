from flask import Flask, request, render_template, flash, make_response, redirect, url_for
import json, datetime
import pymongo
import functions


app = Flask(__name__)
app.secret_key = b'jasf78623ncnoasd--0937h'
totals = {
          'lunch': 300,
          'party': 250,
          'out': 200,
          'week': 750,
          'month': 3000
}
functions.insertCurrentWeek(50, 100, 75)
#client = pymongo.MongoClient()
#db = client.budget
#current_week = db.current_week
post = {
            "date": "2020-10-14",
            "UCT_lunch": "0",
            "party_beers": "0",
            "out_about": "0"
        }
#post_id = current_week.insert_one(post).inserted_id
#print(db.list_collection_names())

#cursor = current_week.find()
#for document in cursor:
    #print(document)

@app.route('/')
def index():
    return redirect('/index')


@app.route('/reset-month')
def reset_month():
    #functions.reset_json("months.json", 'current_month.json', "Months", "Month")
    return render_template('reset-month.html')


@app.route('/reset-week')
def reset_week():
    #functions.reset_json("weeks.json", 'current_week.json', "Weeks", "Days")
    return render_template('reset-week.html')


'''@app.route('/stats')
def statistics():
    current_spendature = 0

    f = open('current_week.json', "r")
    data = f.read()
    json_obj = json.loads(data)
    for day in json_obj["Days"]:
        lunch = float(day["UCT_lunch"])
        party = float(day["party_beers"])
        out = float(day["out_about"])
        current_spendature += lunch + party + out
    left_over = totals["week"] - current_spendature

    return render_template('stats.html', spendature = current_spendature, total_left = left_over)
'''


'''@app.route('/review-json', methods=['GET', 'POST'])
def review_json():
    week_days = ''
    month_days = ''
    week_days_list = functions.statistics_review("current_week.json")
    for day in week_days_list:
        week_days += '\n{}\n{}\n{}\n{}\n'.format(day[0], day[1], day[2], day[3])

    month_days_list = functions.statistics_review("current_month.json")
    for day in month_days_list:
        month_days += '\n{}\n{}\n{}\n{}\n'.format(day[0], day[1], day[2], day[3])

    return render_template('review-json.html', week_days_string=week_days, month_days_string=month_days, week_list=week_days_list, month_list=month_days_list)
'''
@app.route('/index', methods=['GET', 'POST'])
def form():
    #form_values = []
    #running_totals = functions.weekly_spendature()
    UCT_lunch = 0
    party_beers = 0
    out_about = 0
    #current_week_json = functions.load_json_obj("current_week.json")
    #current_month_json = functions.load_json_obj("current_month.json")
    #day = len(current_week_json["Days"]) - 1

    try:
        #print(request.form['UCT_lunch'], "UCT lunch")
        UCT_lunch += float(request.form['UCT_lunch'])
        #current_week_json["Days"][day]["UCT_lunch"] = str(UCT_lunch)
    except:
        pass
    try:
        party_beers += float(request.form['party/beers'])
        #current_week_json["Days"][day]["party_beers"] = str(party_beers)
    except:
        pass
    try:
        out_about += float(request.form['out_about'])
        #current_week_json["Days"][day]["out_about"] = str(out_about)
    except:
        pass
    output_lunch = totals['lunch'] - UCT_lunch #- running_totals[0]
    output_party = totals['party'] - party_beers #- running_totals[1]
    output_out = totals['out'] - out_about #- running_totals[2]
    #functions.write_json(current_week_json, "current_week.json")
    #functions.append_month(current_week_json, current_month_json)
    #print(current_month_json)
    #functions.write_json(current_month_json, "current_month.json")
    #return render_template('index.html', lunch=output_lunch, party=output_party, out=output_out)
    return render_template('index.html')
