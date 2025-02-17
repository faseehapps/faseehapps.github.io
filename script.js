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
