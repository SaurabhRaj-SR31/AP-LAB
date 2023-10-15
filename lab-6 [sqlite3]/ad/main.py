from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database setup
def create_db():
    conn = sqlite3.connect('clinic.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        patient_name TEXT,
        appointment_date TEXT,
        appointment_time TEXT
    )
    ''')
    conn.commit()
    conn.close()

create_db()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Appointments route to list and create appointments
@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        appointment_date = request.form['appointment_date']
        appointment_time = request.form['appointment_time']

        conn = sqlite3.connect('clinic.db')
        c = conn.cursor()

        c.execute("INSERT INTO appointments (patient_name, appointment_date, appointment_time) VALUES (?, ?, ?)",
                  (patient_name, appointment_date, appointment_time))
        conn.commit()
        conn.close()

    conn = sqlite3.connect('clinic.db')
    c = conn.cursor()
    c.execute('SELECT * FROM appointments')
    appointments = c.fetchall()
    conn.close()

    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
