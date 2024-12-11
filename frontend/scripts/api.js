document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/api/predict/", {
        method: "POST",
        body: formData,
    });

    const data = await response.json();
    document.getElementById("result").innerText = `Prediction: ${data.prediction}`;
});
