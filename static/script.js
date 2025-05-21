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
        dashboard.innerHTML = "";
        data.conditions.forEach(item => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
                <h3>${item.condition}</h3>
                <p><strong>Risk:</strong> ${item.risk}</p>
                <p><strong>Tests:</strong> ${item.tests.join(", ")}</p>
                <p><strong>Schedule:</strong> ${item.schedule}</p>
            `;
            dashboard.appendChild(card);
        });
    });
});
