from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
    data = request.json
    answers = {item['question']: item['answer'] for item in data['answers']}
    age = int(answers.get("age", 0))

    def schedule_text(freq):
        return f"Every {freq} years - next due: Now"

    results = [
        ("Cardiovascular Disease", "Low", ["Blood Pressure", "ECG (optional)"], schedule_text(2)),
        ("Type 2 Diabetes", "Low", ["Fasting Glucose", "HbA1c"], schedule_text(3)),
        ("Lung Disease", "Low", ["Spirometry (if symptoms arise)"], "Not routinely needed"),
        ("Kidney Disease", "Low", ["eGFR (blood test)", "Urine Albumin"], "Every 3-5 years - next due: Now"),
        ("Cholesterol", "Low", ["Lipid Panel"], schedule_text(5)),
        ("Cancer Screening", "Medium", ["PSA Blood Test", "Bowel Screening (FIT Test)"], "Start now, then every 1–2 years - next due: Now"),
        ("Mental Health", "Medium", ["Mental health checkup", "Stress/sleep assessment"], "Annual review recommended"),
        ("Obesity / Metabolic", "Low", ["BMI", "Waist circumference", "Fasting insulin"], "Yearly check or if weight changes"),
        ("Cognitive Health", "Low", ["Cognitive screening", "Memory evaluation"], "Baseline at 50+, then every 2–3 years"),
        ("Bone Health", "Low", ["Bone Density Scan (DEXA)", "Calcium/Vitamin D"], "Start at 50+ or if risk factors emerge"),
        ("Arthritis / Joint Health", "Low", ["Mobility screening", "Inflammatory markers"], "As symptoms or stiffness appear"),
    ]

    response = {
        "conditions": [
            {
                "condition": c,
                "risk": r,
                "tests": t,
                "schedule": s
            }
            for (c, r, t, s) in results
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
