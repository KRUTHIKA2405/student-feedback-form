document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const dept = document.getElementById('department').value;
    const gender = document.querySelector('input[name="gender"]:checked');
    const comments = document.getElementById('comments').value;

    // Word count check
    const wordCount = comments.trim().split(/\s+/).length;

    if (name === "" || !email.includes("@") || isNaN(mobile) || mobile.length < 10) {
        alert("Please enter valid details.");
    } else if (!gender) {
        alert("Please select a gender.");
    } else if (dept === "") {
        alert("Please select a department.");
    } else if (wordCount < 10) {
        alert("Feedback must be at least 10 words.");
    } else {
        document.getElementById('successMsg').style.display = 'block';
    }
});