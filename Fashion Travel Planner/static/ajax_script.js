// ajax code like function
$(document).ready(function () {
    $('.like').click(function () {//on click of the like button
        var tipIdVar = $(this).attr('data-tipid');
        var clickedButton = $(this);

        $.get('/rango/like_tip/',
            { 'tip_id': tipIdVar },//increase the like count
            function (data) {
                clickedButton.closest('li').find('.like_count').html(data);
            }
        );
    });
});

//list checkbox toggle function
function handleCheckboxChange(event) {
    //get item id of the toggle checkbox
    const itemId = event.target.dataset.itemId;
    const isCompleted = event.target.checked;

    fetch(`/rango/update_item/${itemId}/`, {
        //update in database
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify({ completed: isCompleted }),
    })
        .then(response => {
            if (response.ok) {
                console.log('success')
            } else {
                console.error('Failed to update the item status.');
                event.target.checked = !isCompleted;
            }
        })
        .catch(error => {
            console.error('Error occurred while updating the item status.', error);
            event.target.checked = !isCompleted;
        });
}

document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleCheckboxChange);
    });
});