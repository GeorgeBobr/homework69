$(document).ready(function() {
    $(".operation-btn").click(function() {
        const operation = $(this).data("operation");
        const numberA = $("#numberA").val();
        const numberB = $("#numberB").val();

        $.ajax({
            url: `/${operation}/`,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ A: numberA, B: numberB }),
            success: function(data) {
                const resultDiv = $("#result");
                resultDiv.empty();

                if ('answer' in data) {
                    resultDiv.css('color', 'green').text(`Result: ${data.answer}`);
                } else if ('error' in data) {
                    resultDiv.css('color', 'red').text(`Error: ${data.error}`);
                }
            },
            error: function() {
                console.error('Error during AJAX request');
            }
        });
    });
});
