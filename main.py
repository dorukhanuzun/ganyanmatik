from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FieldList, FormField, Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SekerUzun'
Bootstrap(app)

total = []
total_point = []
points = ["ten_points", "nine_points", "eight_points", "seven_points", "six_points", "five_points", "four_points",
          "three_points", "two_points", "one_point"]


class ClassicForm(Form):
    ten_points = IntegerField("10 puan")
    nine_points = IntegerField("9 puan")
    eight_points = IntegerField("8 puan")
    seven_points = IntegerField("7 puan")
    six_points = IntegerField("6 puan")
    five_points = IntegerField("5 puan")
    four_points = IntegerField("4 puan")
    three_points = IntegerField("3 puan")
    two_points = IntegerField("2 puan")
    one_point = IntegerField("1 puan")


class GanyanForm(FlaskForm):
    column1 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column2 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column3 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column4 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column5 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column6 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column7 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column8 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column9 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column10 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column11 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column12 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column13 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column14 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column15 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column16 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column17 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column18 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column19 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column20 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column21 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column22 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    column23 = FieldList(FormField(ClassicForm), min_entries=1, max_entries=10)
    submit = SubmitField(label="Gonder")


@app.route("/", methods=["POST", "GET"])
def home():
    form = GanyanForm()
    if request.method == "POST":
        column_1 = form.column1.data
        column_2 = form.column2.data
        column_3 = form.column3.data
        column_4 = form.column4.data
        column_5 = form.column5.data
        column_6 = form.column6.data
        column_7 = form.column7.data
        column_8 = form.column8.data
        column_9 = form.column9.data
        column_10 = form.column10.data
        column_11 = form.column11.data
        column_12 = form.column12.data
        column_13 = form.column13.data
        column_14 = form.column14.data
        column_15 = form.column15.data
        column_16 = form.column16.data
        column_17 = form.column17.data
        column_18 = form.column18.data
        column_19 = form.column19.data
        column_20 = form.column20.data
        column_21 = form.column21.data
        column_22 = form.column22.data
        column_23 = form.column23.data
        total.append(column_1)
        total.append(column_2)
        total.append(column_3)
        total.append(column_4)
        total.append(column_5)
        total.append(column_6)
        total.append(column_7)
        total.append(column_8)
        total.append(column_9)
        total.append(column_10)
        total.append(column_11)
        total.append(column_12)
        total.append(column_13)
        total.append(column_14)
        total.append(column_15)
        total.append(column_16)
        total.append(column_17)
        total.append(column_18)
        total.append(column_19)
        total.append(column_20)
        total.append(column_21)
        total.append(column_22)
        total.append(column_23)
        for i in range(23):
            for point in points:
                index = points[::-1].index(point) + 1
                if total[i][0][point] != None:
                    total_point.extend([total[i][0][point]] * index)

        number1 = total_point.count(1)
        number2 = total_point.count(2)
        number3 = total_point.count(3)
        number4 = total_point.count(4)
        number5 = total_point.count(5)
        number6 = total_point.count(6)
        number7 = total_point.count(7)
        number8 = total_point.count(8)
        number9 = total_point.count(9)
        number10 = total_point.count(10)
        number11 = total_point.count(11)
        number12 = total_point.count(12)
        number13 = total_point.count(13)
        number14 = total_point.count(14)
        number15 = total_point.count(15)
        number16 = total_point.count(16)
        number17 = total_point.count(17)
        number18 = total_point.count(18)
        number19 = total_point.count(19)
        number20 = total_point.count(20)
        number21 = total_point.count(21)
        number22 = total_point.count(22)
        number23 = total_point.count(23)

        total_dic = {1: number1, 2: number2, 3: number3, 4: number4, 5: number5, 6: number6, 7: number7, 8: number8,
                         9: number9, 10: number10, 11: number11, 12: number12, 13: number13, 14: number14, 15: number15,
                         16: number16, 17: number17, 18: number18, 19: number19, 20: number20, 21: number21, 22: number22,
                         23: number23}

        sorted_values = sorted(total_dic.items(), key=lambda x: x[1], reverse=True)
        print(sorted_values)
        text = [f"Birinci gelen at : {sorted_values[0][0]} ve puani :{sorted_values[0][1]}\n",
               f"Ikinci gelen at : {sorted_values[1][0]} ve puani :{sorted_values[1][1]}\n",
               f"Ucuncu gelen at: {sorted_values[2][0]} ve puani :{sorted_values[2][1]}\n",
               f"Dorduncu gelen at: {sorted_values[3][0]} ve puani :{sorted_values[3][1]}\n",
               f"Besinci gelen at: {sorted_values[4][0]} ve puani :{sorted_values[4][1]}\n",
               f"Altinci gelen at: {sorted_values[5][0]} ve puani :{sorted_values[5][1]}\n",
               f"Yedinci gelen at: {sorted_values[6][0]} ve puani :{sorted_values[6][1]}\n",
               f"Sekizinci gelen at: {sorted_values[7][0]} ve puani :{sorted_values[7][1]}\n",
               f"Dokuzuncu gelen at: {sorted_values[8][0]} ve puani :{sorted_values[8][1]}\n",
               f"Onuncu gelen at: {sorted_values[9][0]} ve puani :{sorted_values[9][1]}\n"]

        return render_template("result.html", result=text)

    return render_template("index.html", form=form)


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/reset')
def reset():
    global total
    total = []
    global total_point
    total_point = []
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)




# from tkinter import *
#
# window = Tk()
# window.title("Ganyanmatik")
# window.config(padx=40, pady=40, bg="white")
#
# titles = ["AGF", "Puan", "Tabela", "1/2", "Derece", "Kum", "Cim", "Joker", "TF", "S.TF", "MF", "S.MF", "Ort.De",
#           "S.OR.D", "TD", "S.TD", "ORT", "En iyi", "1600-1300"]
#
# result_label = Label(text="Sonuclariniz burada gozukecektir.", fg="black", bg="white", font=("Arial", 20))
# result_label.grid(column=6, row=13, columnspan=10)
#
# for i in range(0, 19):
#     title_label = Label(text=titleas[i], fg="black", bg="white", font=("Arial", 10))
#     title_label.grid(column=i+1, row=0)
#
# total = []
# total_result = []
#
#
# def calculate_result():
#     for entry in ten_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*10)
#
#     for entry in nine_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*9)
#
#     for entry in eight_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*8)
#
#     for entry in seven_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*7)
#
#     for entry in six_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*6)
#
#     for entry in five_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*5)
#
#     for entry in four_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*4)
#
#     for entry in three_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*3)
#
#     for entry in two_points:
#         if entry.get() != "":
#             total.extend([entry.get()]*2)
#
#     for entry in one_point:
#         if entry.get() != "":
#             total.extend([entry.get()]*1)
#
#     number1 = total.count("1")
#     number2 = total.count("2")
#     number3 = total.count("3")
#     number4 = total.count("4")
#     number5 = total.count("5")
#     number6 = total.count("6")
#     number7 = total.count("7")
#     number8 = total.count("8")
#     number9 = total.count("9")
#     number10 = total.count("10")
#     number11 = total.count("11")
#     number12 = total.count("12")
#     number13 = total.count("13")
#     number14 = total.count("14")
#     number15 = total.count("15")
#     number16 = total.count("16")
#     number17 = total.count("17")
#     number18 = total.count("18")
#     number19 = total.count("19")
#     number20 = total.count("20")
#     number21 = total.count("21")
#     number22 = total.count("22")
#     number23 = total.count("23")
#
#     total_dic = {1: number1, 2: number2, 3: number3, 4: number4, 5: number5, 6: number6, 7: number7, 8: number8,
#                  9: number9, 10: number10, 11: number11, 12: number12, 13: number13, 14: number14, 15: number15,
#                  16: number16, 17: number17, 18: number18, 19: number19, 20: number20, 21: number21, 22: number22,
#                  23: number23}
#
#     sorted_values = sorted(total_dic.items(), key=lambda x: x[1], reverse=True)
#     result_label.config(text=f"Birinci gelen at : {sorted_values[0][0]} ve puani :{sorted_values[0][1]}\n"
#                              f"Ikinci gelen at : {sorted_values[1][0]} ve puani :{sorted_values[1][1]}\n"
#                              f"Ucuncu gelen at: {sorted_values[2][0]} ve puani :{sorted_values[2][1]}\n"
#                              f"Dorduncu gelen at: {sorted_values[3][0]} ve puani :{sorted_values[3][1]}\n"
#                              f"Besinci gelen at: {sorted_values[4][0]} ve puani :{sorted_values[4][1]}\n"
#                              f"Altinci gelen at: {sorted_values[5][0]} ve puani :{sorted_values[5][1]}\n"
#                              f"Yedinci gelen at: {sorted_values[6][0]} ve puani :{sorted_values[6][1]}\n"
#                              f"Sekizinci gelen at: {sorted_values[7][0]} ve puani :{sorted_values[7][1]}\n"
#                              f"Dokuzuncu gelen at: {sorted_values[8][0]} ve puani :{sorted_values[8][1]}\n"
#                              f"Onuncu gelen at: {sorted_values[9][0]} ve puani :{sorted_values[9][1]}\n")
#
#
# def reset():
#     for each_field in all_entries:
#         for field in each_field:
#             field.delete(0, END)
#
#
# calculate = Button(window, text="Calculate", pady=10, command=calculate_result)
# calculate.grid(row=11, column=8)
#
# reset = Button(window, text="Reset", pady=10, command=reset)
# reset.grid(row=11, column=11)
#
# ten_points = []
# nine_points = []
# eight_points = []
# seven_points = []
# six_points = []
# five_points = []
# four_points = []
# three_points = []
# two_points = []
# one_point = []
#
# for i in range(1, 24):
#     my_entry10 = Entry(window, width=5)
#     my_entry10.grid(row=1, column=i)
#     ten_points.append(my_entry10)
#
#     my_entry9 = Entry(window, width=5)
#     my_entry9.grid(row=2, column=i)
#     nine_points.append(my_entry9)
#
#     my_entry8 = Entry(window, width=5)
#     my_entry8.grid(row=3, column=i)
#     eight_points.append(my_entry8)
#
#     my_entry7 = Entry(window, width=5)
#     my_entry7.grid(row=4, column=i)
#     seven_points.append(my_entry7)
#
#     my_entry6 = Entry(window, width=5)
#     my_entry6.grid(row=5, column=i)
#     six_points.append(my_entry6)
#
#     my_entry5 = Entry(window, width=5)
#     my_entry5.grid(row=6, column=i)
#     five_points.append(my_entry5)
#
#     my_entry4 = Entry(window, width=5)
#     my_entry4.grid(row=7, column=i)
#     four_points.append(my_entry4)
#
#     my_entry3 = Entry(window, width=5)
#     my_entry3.grid(row=8, column=i)
#     three_points.append(my_entry3)
#
#     my_entry2 = Entry(window, width=5)
#     my_entry2.grid(row=9, column=i)
#     two_points.append(my_entry2)
#
#     my_entry1 = Entry(window, width=5)
#     my_entry1.grid(row=10, column=i)
#     one_point.append(my_entry1)
#
# all_entries = [ten_points, nine_points, eight_points, seven_points, six_points, five_points, four_points, three_points,
#                two_points, one_point]
#
#
# window.mainloop()
#
#
