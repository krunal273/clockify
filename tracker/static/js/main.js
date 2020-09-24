// @ts-nocheck
// select unknown option for project

const project = document.getElementById("id_project");
// Unknown option selected by default
project[0].removeAttribute("selected");
project.selectedIndex = 1;
project[1].setAttribute("selected", "selected");



// list running activity

const runningActivities = document.querySelectorAll('[data-complete="False"]');
runningActivities.forEach(ele => {

    setInterval(() => {
        const start = ele.getAttribute('data-start'); // read data attribute
        const startTime = new Date(start); // start time
        const currentTime = new Date(); // current time

        let seconds = Math.floor(((currentTime) - startTime) / 1000);
        let minutes = Math.floor(seconds / 60);
        let hours = Math.floor(minutes / 60);
        const days = Math.floor(hours / 24);

        // converting total seconds to actual clock

        hours = hours - (days * 24);
        minutes = minutes - (days * 24 * 60) - (hours * 60);
        seconds = seconds - (days * 24 * 60 * 60) - (hours * 60 * 60) - (minutes * 60);

        document.getElementById("displayTime-" + ele.id).innerText = "Days: " + days + " Hours: " + hours + " Minutes: " + minutes + " Seconds: " + seconds



    }, 1000);



})

// list done activity

const doneActivities = document.querySelectorAll('[data-complete="True"]');
doneActivities.forEach(ele => {
    const start = ele.getAttribute('data-start'); // read data attribute
    const end = ele.getAttribute('data-end'); // read data attribute
    const startTime = new Date(start); // start time
    const endTime = new Date(end); // current time

    let seconds = Math.floor(((endTime) - startTime) / 1000);
    let minutes = Math.floor(seconds / 60);
    let hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    // converting total seconds to actual clock

    hours = hours - (days * 24);
    minutes = minutes - (days * 24 * 60) - (hours * 60);
    seconds = seconds - (days * 24 * 60 * 60) - (hours * 60 * 60) - (minutes * 60);

    document.getElementById("displayTime-" + ele.id).innerText = "Days: " + days + " Hours: " + hours + " Minutes: " + minutes + " Seconds: " + seconds

})