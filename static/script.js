document.getElementById("surveyForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const answers = [];
    for (let [key, value] of formData.entries()) {
        answers.push({ question: key, answer: value });
    }

    fetch("/assess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answers })
    })
    .then(response => response.json())
    .then(data => {
        const dashboard = document.getElementById("dashboard");
        dashboard.innerHTML = "<h2>Assessment Results:</h2>";
        data.conditions.forEach(item => {
            const div = document.createElement("div");
            div.className = "result-card";
            div.innerHTML = `<strong>${item.condition}</strong><br>
                Risk: ${item.risk}<br>
                Tests: ${item.tests.join(", ")}<br>
                Schedule: ${item.schedule}<br><br>`;
            dashboard.appendChild(div);
        });
    });
});
