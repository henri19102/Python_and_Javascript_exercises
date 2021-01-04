$(document).ready(function () {
    $.getJSON("qJSON.json", function (data) {
        let objects = data
        let questions = []
        let choices = []
        for (let [key, value] of Object.entries(objects)) {
            questions.push(key);
            value.forEach(e => choices.push(e));
        }
        for (let i = 0; i < 3; i++) {
            $(`#p${i}`).append(questions[i])
        }
        for (let i = 0; i < 9; i++) {
            $(`#q${i}`).append(choices[i])
        }
    }
    )
})

$(document).ready(function () {
    $("#sub").click(function () {
        let points = 0;

        for (let i = 0; i < 3; i++) {
            points += Number($(`input[type=radio][name=ans${i}]:checked`).val());
        }
        $(`#anss`).text(`You got ${points} from maximum of 3 points!`)
    });
});




