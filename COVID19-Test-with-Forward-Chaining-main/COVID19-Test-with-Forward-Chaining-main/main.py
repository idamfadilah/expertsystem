from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    #Get Name
    gender = request.form['gender'] # Mr. / Ms.
    name = request.form['name'] # user name

    #Get Submited answer
    question1 = request.form['question1'] #B
    question2 = request.form['question2'] #C
    question3 = request.form['question3'] #D
    question4 = request.form['question4'] #E
    question5 = request.form['question5'] #F
    question6 = request.form['question6'] #G
    question7 = request.form['question7'] #H
    question8 = request.form['question8'] #I
    question9 = request.form['question9'] #J
    question10 = request.form['question10'] #K
    question11 = request.form['question11'] #L
    question12 = request.form['question12'] #M

    #dari get data form html dimasukkan kedalam array untuk dicek berdasarkan rule
    arr_rule1 = [question1, question2, question3, question4, question5]
    arr_rule2 = [question1, question2, question3, question4, question6, question7, question8]
    arr_rule3 = [question9, question10, question11, question12, question7, question1]
    arr_rule4 = [question1, question5, question7, question10, question12, question11]

    check, advice = main(arr_rule1, arr_rule2, arr_rule3, arr_rule4)

    return render_template('result.html', answer = check, gender = gender, name = name, advice = advice)

def main(arr_rule1, arr_rule2, arr_rule3, arr_rule4): # state_rule1 = sys.argv.pop(0)
    # first_batch
    # Hasil yang diambil sesuai dengan premise-premise yang berada dalam rule1
    question1rule1, question2rule1, question3rule1, question4rule1, question5rule1 = arr_rule1
    testrule1 = question1rule1 + question2rule1 + question3rule1 + question4rule1 + question5rule1

    # second_batch
    # Hasil yang diambil sesuai dengan premise-premise yang berada dalam rule2
    question1rule2, question2rule2, question3rule2, question4rule2, question6rule2, question7rule2, question8rule2 = arr_rule2
    testrule2 = question1rule2 + question2rule2 + question3rule2 + question4rule2 + question6rule2 + question7rule2 + question8rule2

    # third_batch
    # Hasil yang diambil sesuai dengan premise-premise yang berada dalam rule3
    question9rule3, question10rule3, question11rule3, question12rule3, question7rule3, question1rule3 = arr_rule3
    testrule3 = question9rule3 + question10rule3 + question11rule3 + question12rule3 + question7rule3 + question1rule3

    # fourth_batch (ODP)
    # Hasil yang diambil sesuai dengan premise-premise yang berada dalam rule4
    question1rule4, question5rule4, question7rule4, question10rule4, question12rule4, question11rule4 = arr_rule4
    testrule4 = question1rule4 + question5rule4 + question7rule4 + question10rule4 + question12rule4 + question11rule4

    # Membaca rule/knowledge yang ada di txt yang sudah disiapkan berdasarkan jurnal yang diberikan
    knowledge_rule1 = parse("rule1.txt")
    knowledge_rule2 = parse("rule2.txt")
    knowledge_rule3 = parse("rule3.txt")
    knowledge_rule4 = parse("rule4.txt")

    # Hasil input nya dipisah menjadi array berdasarkan ' '(Spasi)
    submitAnswers_rule1 = testrule1.split(' ')  # Menjadi ['-', '-', 'D', 'E', '-']
    submitAnswers_rule2 = testrule2.split(' ')  # Menjadi ['B', 'C', 'D', 'E', '-', 'H', 'I']
    submitAnswers_rule3 = testrule3.split(' ')  # Menjadi ['J', 'K', 'L', '-', '-', '-']
    submitAnswer_rule4 = testrule4.split(' ')   # Menjadi ['B', 'F', 'H', 'K', 'M', 'L']

    '''
        Cara kerja program kami adalah:
        Pengecekan pada rule pertama dahulu, apabila tidak terdiagnosa PDP-19,
        akan dilakukan pengecekan rule kedua.
        
        Apabila tidak terdiagnosa PDP, maka akan dilakukan pengecekan pada rule ketiga.
        
        Apabila tidak terdiagnosa PDP pada rule ketiga maka akan dilakukan pengecekan pada rule keempat(ODP).
        Apabila tidak terdeteksi ODP maka user dinyatakan tidak terkena covid-19(Negative).
    '''

    adviceForPdp = "Please contact your nearest health department for further instruction"
    adviceForOdp = "Please contact your nearest health department for further instruction"
    adviceForNon = "Please continue to follow your health regulation in your area"

    # result_rule# = Membandingkan hasil yang disubmit user dengan rule yang telah buat.
    result_rule1 = fc_five_goals(submitAnswers_rule1, knowledge_rule1)
    if result_rule1:
        return "You are diagnosed with COVID-19.", adviceForPdp
    else:
        result_rule2 = fc_seven_goals(submitAnswers_rule2, knowledge_rule2)
        if result_rule2:
            return "You are diagnosed with COVID-19.", adviceForPdp
        else:
            result_rule3 = fc_six_goals(submitAnswers_rule3, knowledge_rule3)
            if result_rule3:
                return "You are diagnosed with COVID-19.", adviceForPdp
            else:
                result_rule4 = fc_six_goals(submitAnswer_rule4, knowledge_rule4)
                if result_rule4:
                    return "You are labeled to have ODP.", adviceForOdp
                else:
                    return "You are not diagnosed with COVID-19", adviceForNon

def fc_five_goals(submit, knowledge):
    goal = 5   # Nilai counter harus sesuai dengan goals agar menentukan bahwa yang didiagnosa pasien seusai dengan rule covid yang telah dibuat.
    '''
        Cara kerja
        Apabila di rule 'B' dan didiagnosa pasien terdapat 'B'
        Maka akan bernilai true dan counter akan naik 
    '''
    result = False
    for rule in knowledge:
        counter = 0
        for j, premise in enumerate(rule[0]): #enumerate adalah fungsi mendapatkan index pada rule[0]->['B', 'C', 'D', ....]
            if submit[j] == premise:
                counter += 1

        if counter == goal:
            result = True

    return result

def fc_six_goals(submit, knowledge):
    goal = 6 # Nilai counter harus sesuai dengan goals agar menentukan bahwa yang didiagnosa pasien seusai dengan rule covid yang telah dibuat.
    '''
        Cara kerja
        Apabila di rule 'B' dan didiagnosa pasien terdapat 'B'
        Maka akan bernilai true dan counter akan naik 
    '''
    result = False
    for rule in knowledge:
        counter = 0
        for j, premise in enumerate(rule[0]): #enumerate adalah fungsi mendapatkan index pada rule[0]->['B', 'C', 'D', ....]
            if submit[j] == premise:
                counter += 1

        if counter == goal:
            result = True

    return result

def fc_seven_goals(submit, knowledge):
    goal = 7 #Nilai counter harus sesuai dengan goals agar menentukan bahwa yang didiagnosa pasien seusai dengan rule covid yang telah dibuat.
    '''
        Cara kerja
        Apabila di rule 'B' dan didiagnosa pasien terdapat 'B'
        Maka akan bernilai true dan counter akan naik 
    '''
    result = False
    for rule in knowledge:
        counter = 0
        for j, premise in enumerate(rule[0]):#enumerate adalah fungsi mendapatkan index pada rule[0]->['B', 'C', 'D', ....]
            if submit[j] == premise:
                counter += 1

        if counter == goal:
            result = True

    return result


def parse(file):
    current_file = open(file, newline='')# newline='' karena kita ingin melewati setiap baris yang kosong pada file .txt
    kb_rules = []# untuk menyimpan semua rules yang didapatkan dari rule.txt

    for line in current_file:# Membaca knowledge per baris
        if not line.startswith('#') and line != '\n':
            kb_rules.append(split_literals(line.strip())) # hanya membaca knowledge tertenetu

    current_file.close()
    return kb_rules

def split_literals(line):
    rules = []
    literals = line.split(' ')
    hypothesis = []

    while len(literals) > 1:
        hypothesis.append(literals.pop(0)) # Memotong hasil dari knowledge berdasarkan ' ' lalu siap dibandingkan dengan input user

    rules.append(hypothesis)
    rules.append(literals.pop(0))

    return rules

if __name__ == '__main__':
    app.run(debug=True) #debug= True agar dapat rerun setiap ada pergantian