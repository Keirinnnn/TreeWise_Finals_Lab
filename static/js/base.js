console.log("JavaScript Here!");

function toggleMenu() {
    document.getElementById("navbarLinks").classList.toggle("active");
}

// Automatically close the menu when resizing to a large screen
window.addEventListener("resize", function () {
    if (window.innerWidth > 768) {
        document.getElementById("navbarLinks").classList.remove("active");
    }
});

setTimeout(function () {
    var messages = document.getElementById('notification_messages');
    if (messages) {
        const messageItems = messages.querySelectorAll('li');
        messageItems.forEach(function (message) {
            message.classList.add('fade-out');
        });

        setTimeout(function () {
            messages.style.display = 'none';
        }, 800);
    }
}, 3000);

// Video Controls
document.addEventListener("DOMContentLoaded", function () {
    const videoContainer = document.querySelector(".video_container");
    const video = document.querySelector('.vid_comment');

    if (videoContainer && video) {
        const progressBar = document.createElement("input");
        progressBar.type = "range";
        progressBar.min = 0;
        progressBar.max = 100;
        progressBar.value = 0;
        progressBar.step = 0.1;
        progressBar.classList.add("video_progress");

        videoContainer.appendChild(progressBar);

        video.addEventListener("timeupdate", () => {
            progressBar.value = (video.currentTime / video.duration) * 100;
        });

        progressBar.addEventListener("input", () => {
            video.currentTime = (progressBar.value / 100) * video.duration;
        });

        document.addEventListener("keydown", (event) => {
            switch (event.key) {
                case "ArrowRight":
                    video.currentTime += 5;
                    break;
                case "ArrowLeft":
                    video.currentTime -= 5;
                    break;
                case " ":
                    event.preventDefault();
                    video.paused ? video.play() : video.pause();
                    break;
            }
        });
    } else {
        console.log("Video or Video Container not found!");
    }
});
