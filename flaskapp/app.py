from flask import Flask, render_template, request
from data_process.youtube_take_commend import fetch_video_info
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/comments_show', methods=['POST'])
def submit():
    link1 = request.form['link']
    comAll = fetch_video_info(link1)
    return render_template("index.html", comAll=comAll)
@app.context_processor
def inject_enumerate():
   
    return dict(enumerate=enumerate)
if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)



#from flask import Flask, render_template, request, session
#from data_process.youtube_take_commend import fetch_video_info
#from data_process.emotional_analysis import analysis_sentence
#import json
#
#app = Flask(__name__)
#app.secret_key = '8b8'
#
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#
#def save_link(link):
#    link_to_save = {"link": f"{link}"}
#    with open('save_data_instant/links.json', 'w') as json_file:
#        json.dump(link_to_save, json_file)
#
#
#def read_json_file():
#    with open('save_data_instant/links.json', 'r') as json_file:
#        loaded_data = json.load(json_file)
#    return loaded_data
#
#
#def take_Data():
#    link1 = request.form['link']
#    save_link(link1)
#    comAll = fetch_video_info(link1)
#    return comAll
#
#
#def sentence_analysis(video_comments):
#    result_list = []
#    for comment in video_comments["video_comments"]:
#        analyzed_result = analysis_sentence(comment["comment_text"])
#        result_list.append([comment["comment_text"], analyzed_result])
#    return result_list
#
#
#@app.route('/comments_show', methods=['POST'])
#def submit():
#    comAll = take_Data()
#    return render_template("index.html",
#                           comAll=comAll)
#
#
#@app.route('/analysis', methods=['POST'])
#def analysis():
#    link = read_json_file()
#    print(link["link"])
#    comAll = fetch_video_info(link["link"])
#    processed_data = sentence_analysis(comAll)
#    return render_template("index.html",
#                           processed_data=processed_data)
#
#
#@app.context_processor
#def inject_enumerate():
#    return dict(enumerate=enumerate)
#
#
#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=5000)
#

















