async function predict() {
    const animal = document.getElementById("animalSelect").value;
    const image = document.getElementById("imageUpload").files[0];
    const loader = document.getElementById("loader");
    const resultBox = document.getElementById("result");
    const medicineBox = document.getElementById("medicine");

    resultBox.innerHTML = "";
    medicineBox.innerHTML = "";

    if (!animal || !image) {
        alert("Please select animal and upload an image.");
        return;
    }

    loader.style.display = "block";

    // ---- FIXED REQUEST FIELD NAMES ----
    const formData = new FormData();
    formData.append("animal_type", animal);  // backend expects animal_type
    formData.append("file", image);          // backend expects file
    // -----------------------------------

    try {
        const res = await fetch("http://127.0.0.1:8000/predict/", {
            method: "POST",
            body: formData
        });

        loader.style.display = "none";
        const data = await res.json();
        console.log("Response from backend:", data);

        // Matching backend response keys
        if (data.error) {
            resultBox.innerHTML = `<b style='color:red'>${data.error}</b>`;
            return;
        }

        resultBox.innerHTML = `<b>Disease:</b> ${data.prediction}`;
        medicineBox.innerHTML = `<b>Medicine:</b> ${data.medicine_suggestion}`;

    } catch (err) {
        loader.style.display = "none";
        alert("⚠️ Backend se connection error!");
        console.log(err);
    }
}

