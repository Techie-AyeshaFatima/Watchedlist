document.addEventListener('DOMContentLoaded', function() {
    setupRadioButtons();
    checkInitialState();
});

function setupRadioButtons() {
    document.querySelectorAll('input[name="btnradio"]').forEach((radio) => {
        radio.addEventListener('change', handleRadioChange);
    });
}

function handleRadioChange() {
    document.querySelectorAll('.btn-outline-secondary').forEach((label) => {
        label.classList.remove('selected', 'btn-outline-success');
    });
    this.nextElementSibling.classList.add('selected', 'btn-outline-success');
    toggleStars();
}

function checkInitialState() {
    document.querySelectorAll('input[name="btnradio"]').forEach((radio) => {
        if (radio.checked) {
            radio.nextElementSibling.classList.add('selected', 'btn-outline-success');
        }
    });
    toggleStars();
}

function toggleStars() {
    var watchedlist = document.getElementById('btnradio2').checked;
    var droppedlist = document.getElementById('btnradio3').checked;
    var rateDiv = document.getElementById('rate');
    
    if (watchedlist || droppedlist) {
        rateDiv.style.display = 'inline-block';
    } else {
        rateDiv.style.display = 'none';
        resetRatingStars();
    }
}

function resetRatingStars() { 
    var ratingStars = document.querySelectorAll('input[name="rating"]'); 
    ratingStars.forEach((star) => {
        star.checked = false; 
    }); 
}
