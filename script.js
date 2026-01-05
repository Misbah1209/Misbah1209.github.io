function scrollToElement(elementSelector) {
    const element = document.querySelector(elementSelector);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

const link1 = document.getElementById("link1");
const link2 = document.getElementById("link2");
const link3 = document.getElementById("link3");
const link4 = document.getElementById("link4");
const link5 = document.getElementById("link5");

link1.addEventListener('click', () => {
    scrollToElement('#skills');  // Scroll to Skills section
});

link2.addEventListener('click', () => {
    scrollToElement('#experience');  // Scroll to Experience section
});

link3.addEventListener('click', () => {
    scrollToElement('#education');  // Scroll to Education section
});

link4.addEventListener('click', () => {
    scrollToElement('#projects');  // Scroll to Projects section
});

link5.addEventListener('click', () => {
    scrollToElement('#contactme');  // Scroll to Contact Me section
});


document.getElementById('openResume').addEventListener('click', function() {
    window.open('static/Resume.pdf', '_blank');
});

document.getElementById('openResume').addEventListener('click', function() {
    window.open('static/SLA.pdf', '_blank');
});

const cardsContainer = document.querySelector(".cards");
const prevButton = document.querySelector(".prev-btn");
const nextButton = document.querySelector(".next-btn");
const cardWidth = 250; 
const cardsVisible = 2; 
const totalCards = document.querySelectorAll(".cards .card").length;
const maxScroll = Math.max(0, totalCards - cardsVisible);

let scrollPosition = 0;

nextButton.addEventListener("click", () => {
  if (scrollPosition < maxScroll) {
    scrollPosition++;
    cardsContainer.style.transform = `translateX(-${scrollPosition * (cardWidth)}px)`;
  }
});

prevButton.addEventListener("click", () => {
  if (scrollPosition > 0) {
    scrollPosition--;
    cardsContainer.style.transform = `translateX(-${scrollPosition * (cardWidth)}px)`;
  }
});

function setupPopup(triggerId, popupId) {
    const trigger = document.getElementById(triggerId);
    const popup = document.getElementById(popupId);
    const closeBtn = popup.querySelector(".close");

    trigger.onclick = function () {
        popup.style.display = "block";
        setTimeout(() => {
            popup.classList.add("show");
        }, 10);
    };

    closeBtn.onclick = function () {
        popup.classList.remove("show");
        setTimeout(() => {
            popup.style.display = "none";
        }, 400);
    };

    window.addEventListener("click", function (event) {
        if (event.target === popup) {
            popup.classList.remove("show");
            setTimeout(() => {
                popup.style.display = "none";
            }, 400);
        }
    });
}

setupPopup("popupTrigger1", "popup1");
setupPopup("popupTrigger2", "popup2");
setupPopup("popupTrigger3", "popup3");

function openLink(url) {
  window.open(url, "_blank");

}
