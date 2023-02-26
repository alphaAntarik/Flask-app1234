from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open('careerlast.pkl', 'rb'))

app = Flask(__name__)


@app.route('/home')

def predict():
        Database_Fundamentals = int(request.args.get('Database Fundamentals'))
        Computer_Architecture = int(request.args.get('Computer Architecture'))
        Distributed_Computing_Systems = int(request.args.get('Distributed Computing Systems'))
        Cyber_Security = int(request.args.get('Cyber Security'))
        Networking = int(request.args.get('Networking'))
        Development = int(request.args.get('Development'))
        Programming_Skills = int(request.args.get('Programming Skills'))
        Project_Management = int(request.args.get('Project Management'))
        Computer_Forensics_Fundamentals = int(request.args.get('Computer Forensics Fundamentals'))
        Technical_Communication = int(request.args.get('Technical Communication'))
        AI_ML = int(request.args.get('AI ML'))
        Software_Engineering = int(request.args.get('Software Engineering'))
        Business_Analysis = int(request.args.get('Business Analysis'))
        Communication_skills = int(request.args.get('Communication skills'))
        Data_Science = int(request.args.get('Data Science'))
        Troubleshooting_skills = int(request.args.get('Troubleshooting skills'))
        Graphics_Designing = int(request.args.get('Graphics Designing'))

        input_query = np.array([[Database_Fundamentals, Computer_Architecture, Distributed_Computing_Systems,
                                 Cyber_Security, Networking, Development, Programming_Skills, Project_Management,
                                 Computer_Forensics_Fundamentals, Technical_Communication, AI_ML, Software_Engineering,
                                 Business_Analysis,
                                 Communication_skills, Data_Science, Troubleshooting_skills, Graphics_Designing]])

        result = model.predict(input_query)[0]

        return jsonify({'placement': result})


# @app.route('/predict', methods=['POST'])
# def predict():
#
#     Database_Fundamentals = "Professional"
#     Computer_Architecture = "Not Interested"
#     Distributed_Computing_Systems = "Not Interested"
#     Cyber_Security = "Not Interested"
#     Networking = "Not Interested"
#     Development = "Not Interested"
#     Programming_Skills = "Not Interested"
#     Project_Management = "Not Interested"
#     Computer_Forensics_Fundamentals = "Not Interested"
#     Technical_Communication = "Not Interested"
#     AI_ML = "Not Interested"
#     Software_Engineering = "Not Interested"
#     Business_Analysis = "Not Interested"
#     Communication_skills = "Not Interested"
#     Data_Science = "Not Interested"
#     Troubleshooting_skills = "Not Interested"
#     Graphics_Designing = "Not Interested"
#
#     input_query = np.array([[Database_Fundamentals, Computer_Architecture, Distributed_Computing_Systems,
#                              Cyber_Security, Networking, Development, Programming_Skills, Project_Management,
#                              Computer_Forensics_Fundamentals, Technical_Communication, AI_ML, Software_Engineering,
#                              Business_Analysis,
#                              Communication_skills, Data_Science, Troubleshooting_skills, Graphics_Designing]])
#
#     result = model.predict(input_query)[0]
#
#     return jsonify({'placement': result})
#

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
