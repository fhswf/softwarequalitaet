Array.from(document.getElementsByTagName('input')).forEach(element => {
    element.addEventListener('change', updateUI);
    element.addEventListener('input', updateUI);
});

function updateUI() {
    // Logik zur Aktualisierung des UI hier
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const bmi = calculateBMI(weight, height);
    console.log("weight: %s, height: %s, bmi: %s", weight, height, bmi);
    document.getElementById('bmi').innerText = bmi;
}

function calculateBMI(weight, height) {
    // Logik zur Berechnung des BMI hier
    height = height / 100;
    return weight / (height * height);
}

updateUI();