from flask import render_template
from app import app, stats
from flask import request
#import MAIN_2
@app.route('/')
@app.route('/index.html')
def index():
    d1 = {'adres':'http://infographer.ru/wp-content/uploads/2011/08/Pie_radar.png'} # первая диаграмма
    d2 = {'adres':'http://morepsd.ru/wp-content/uploads/2013/04/pirog.jpg'} # вторая диаграммам

    return render_template("index.html", title = 'Главная',d1 = d1, d2 = d2)

@app.route('/odin.html')
def odin():
    dsh = {'adres':'http://www.cossa.ru/upload/medialibrary/bee/Dashboard_10_orig.jpg'}  # выдуманный пользователь
    return render_template("odin.html",title='Получить данные',dsh=dsh)

@app.route('/odin_post', methods=['GET','POST'])
def odin_post():
    text=request.form['token']
    f = open('text.txt', 'w')
    for index in text:
        f.write(index)
    f.close()
    return render_template("odin.html", title='Получить данные')
@app.route('/cvet')
def cvet_ind():
    if MAIN_2.timer()==('red'):
        indic1 = {'ind':'Bad_traffic'}
        return render_template('odin.html', title ='lol', indic1='bt')
    else:
        indic2 = {'ind':'Good traffic'}
        return render_template('odin.html', title='lol', indic2='gt')
@app.route('/dva.html')
def dva():
    user = {'user.nickname':'miguel'}
    return render_template("dva.html",title='Показать статистику',user=user)

@app.route('/tri.html')
def tri():
    #user = {'nickname': 'Miguel'}  # выдуманный пользователь
    stats_tv = {'total_vectors': stats.str.get('total_vectors')}
    stats_tr = {'total_results': stats.str.get('total_results')}
    stats_avgul = {'avg_user_level': stats.str.get('avg_user_level')}
    stats_avgfpr = {'avg_false_positive_ratio': stats.str.get('avg_false_positive_ratio')}
    stats_cdr = {'classify_data_ratio' : stats.str.get('classify_data_ratio')}
    stats_avgst = {'avg_spent_time': stats.str.get('avg_spent_time')}
    stats_at_numb = {'attempt_number': stats.str.get('attempt_number')}
    stats_avgfnr = {'avg_false_negative_ratio': stats.str.get('avg_false_negative_ratio')}
    stats_avgaccur = {'avg_accuracy': stats.str.get('avg_accuracy')}
    return render_template("tri.html",
                           title='Показать статистику',
                           stats_tv=stats_tv,
                           stats_tr=stats_tr,
                           stats_avgul=stats_avgul,
                           stats_avgfpr=stats_avgfpr,
                           stats_cdr=stats_cdr,
                           stats_avgst=stats_avgst,
                           stats_at_numb=stats_at_numb,
                           stats_avgfnr=stats_avgfnr,
                           stats_avgaccur=stats_avgaccur
                           )
