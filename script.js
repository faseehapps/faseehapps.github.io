const toggleButton = document.getElementById("theme-toggle");

// Function to update the button text
function updateButtonText(theme) {
    toggleButton.textContent = theme === "dark" ? "Light Mode" : "Dark Mode";
}

// Check stored theme preference
const storedTheme = localStorage.getItem("theme") || "light"; // Default to light if no preference
document.documentElement.setAttribute("data-theme", storedTheme);
updateButtonText(storedTheme); // Update button text based on stored theme

toggleButton.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    // Toggle theme and store in localStorage
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme); // Save the preference

    // Update button text
    updateButtonText(newTheme);
});


// Fetch reviews
async function fetchReviews() {
    let reviewList = document.getElementById('review-list');

    try {
        let response = await fetch("https://faseeh1080.pythonanywhere.com/get-reviews");
        let data = await response.json();

        reviewList.innerHTML = ''; 

        data.forEach(review => {
            let div = document.createElement('div');
            div.innerHTML = `<p><strong>${review.name}</strong><br>${review.review}</p>`;
            reviewList.appendChild(div);
        });
    } catch (error) {
        reviewList.innerHTML = "<p>Error fetching reviews";
    }
}

fetchReviews();


// Post reviews
document.getElementById('review-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this);
    const response = await fetch('https://faseeh1080.pythonanywhere.com/submit-review', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        let reviewFormDiv = document.getElementById('review-form-div');
        reviewFormDiv.innerHTML = '<p>Thanks for submitting your review.</p>';
        fetchReviews();
    } else {
        alert('Failed to submit the review.');
    }
});
