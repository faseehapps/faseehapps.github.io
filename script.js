function reviewDiv(authorName, reviewText) {
    let review = document.createElement('div');
    review.className = 'review';
    let formattedReview = String(reviewText).replace(/</g, '&lt;');
    formattedReview = formattedReview.split('\n').map(paragraph => `<p>${paragraph}</p>`).join('');
    review.innerHTML = `<p><strong>${authorName}</strong></p>${formattedReview}`;
    return review;
}

// Fetch reviews
async function fetchReviews() {
    let reviewList = document.getElementById('review-list');

    try {
        let response = await fetch("https://faseeh1080.pythonanywhere.com/get-reviews");
        let data = await response.json();
        reviewList.innerHTML = '';

        data.forEach(review => {
            reviewList.appendChild(reviewDiv(review.name, review.review));
        });
    } catch (error) {
        reviewList.innerHTML = '';
        for (let i = 0; i < 10; i++) {
            reviewList.appendChild(reviewDiv("Unavailable", "The server could not process your request at this time. Please try again later or access the page directly from the official website."));
        }
    }
}

fetchReviews();


// Post reviews
document.getElementById('review-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);
    
    try {
        const response = await fetch('https://faseeh1080.pythonanywhere.com/submit-review', {
            method: 'POST',
            body: formData
        });

        console.log(response.ok ? 'Review submitted successfully' : 'Failed to submit the review');

        if (response.ok) {
            fetchReviews();
            // Say thanks
            const thanksDiv = document.createElement('div');
            thanksDiv.className = 'review-thanks';
            thanksDiv.innerHTML = '<div class="review-thanks-icon"></div><p>Thanks</p>';
            const reviewFormDiv = document.getElementById('review-form-div');
            reviewFormDiv.innerHTML = '';
            reviewFormDiv.appendChild(thanksDiv);
        }
    } catch (error) {
        alert('Error submitting review');
    }
});
