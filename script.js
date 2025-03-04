// Fetch reviews
async function fetchReviews() {
    let reviewList = document.getElementById('review-list');

    try {
        let response = await fetch("https://faseeh1080.pythonanywhere.com/get-reviews");
        let data = await response.json();
        reviewList.innerHTML = '';

        data.forEach(review => {
            let div = document.createElement('div');
            div.className = 'review';
            div.innerHTML = `<p><strong>${review.name}</strong><br>${review.review}</p>`;
            reviewList.appendChild(div);
        });
    } catch (error) {
        reviewList.innerHTML = '';
        ['Failed to fetch reviews.', 'Failed to fetch reviews. Process aborted.'].forEach(message => {
            let div = document.createElement('div');
            div.className = 'review';
            div.innerHTML = `<p><strong>Unavailable</strong><br>${message}</p>`;
            reviewList.appendChild(div);
        });
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
