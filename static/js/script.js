// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.querySelector('input[type="file"]');
    const form = document.querySelector('form');
    const resultSection = document.querySelector('.result');

    // Hide result section initially
    if (resultSection) {
        resultSection.style.display = "none";
    }

    // Handle file input change
    fileInput.addEventListener("change", function () {
        const fileName = fileInput.files[0]?.name || "No file selected";
        alert(`Selected file: ${fileName}`);
    });

    // Add loading spinner during form submission
    form.addEventListener("submit", function () {
        const button = form.querySelector("button");
        button.disabled = true;
        button.textContent = "Analyzing...";
    });
});
