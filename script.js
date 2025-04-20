window.addEventListener("scroll", function () {
  var div = document.getElementById("sticky-header");
  if (window.scrollY > 0) {
    div.classList.add("show-sticky-header");
  } else {
    div.classList.remove("show-sticky-header");
  }
});

function reviewDiv(authorName, reviewText) {
  let review = document.createElement("div");
  review.className = "review";
  let formattedReview = String(reviewText).replace(/</g, "&lt;");
  formattedReview = formattedReview
    .split("\n")
    .map((paragraph) => `<p>${paragraph}</p>`)
    .join("");
  review.innerHTML = `<p><b>${authorName}</b> :</p>${formattedReview}`;
  return review;
}

// Fetch reviews
async function fetchReviews() {
  let reviewList = document.getElementById("review-list");

  try {
    let response = await fetch(
      "https://faseeh1080.pythonanywhere.com/get-reviews"
    );
    let data = await response.json();
    reviewList.innerHTML = "";

    data.forEach((review) => {
      reviewList.appendChild(reviewDiv(review.name, review.review));
    });

    try {
      document.getElementById("submit-btn").disabled = false;
    } catch (error) {}
  } catch (error) {
    reviewList.innerHTML = "";
    for (let i = 0; i < 10; i++) {
      reviewList.appendChild(
        reviewDiv(
          "Server Error",
          "Oops! The server is taking a nap 😴 and couldn’t process your request at this time. Are you visiting directly from the official website? If you're already on the official page, let me know, and I'll wake up the server for you!"
        )
      );
    }
  }
}

fetchReviews(); // Also enables "submit-button" if present.

function validateForm(name, review) {
  if (!name.trim()) {
    alert("Name cannot be empty.");
    return false;
  }

  if (name.length > 100) {
    alert("Name is too long. Please limit it to 100 characters.");
    return false;
  }

  if (!review.trim()) {
    // Explicitly check if suggestion is empty or just spaces
    alert("Suggestion cannot be empty.");
    return false;
  }

  if (review.length < 10) {
    alert("Suggestion is too short. Please provide at least 10 characters.");
    return false;
  }

  if (review.length > 700) {
    alert("Suggestion is too long. Please limit it to 700 characters.");
    return false;
  }

  return true;
}

function sayThanks() {
  const thanksDiv = document.createElement("div");
  thanksDiv.className = "review-thanks";
  thanksDiv.innerHTML = '<div class="review-thanks-icon"></div><p>Thanks</p>';
  const reviewFormDiv = document.getElementById("review-form-div");
  reviewFormDiv.innerHTML = "";
  reviewFormDiv.appendChild(thanksDiv);
}

document
  .getElementById("submit-btn")
  .addEventListener("click", async function () {
    this.disabled = true;

    const name = document.getElementById("name").value;
    const review = document.getElementById("review").value;

    if (!validateForm(name, review)) {
      this.disabled = false;
      return;
    }

    // If validation passes, submit the form
    const formData = new FormData(document.getElementById("review-form"));

    try {
      const response = await fetch(
        "https://faseeh1080.pythonanywhere.com/submit-review",
        {
          method: "POST",
          body: formData,
        }
      );

      if (response.ok) {
        console.log("Review submitted successfully");
        fetchReviews();
        sayThanks();
      } else {
        console.log("Failed to submit the review");
        this.disabled = false;
      }
    } catch (error) {
      this.disabled = false;
      alert("Error submitting review");
    }
  });
