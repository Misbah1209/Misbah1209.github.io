function scrollToElement(elementSelector, instance = 0) {
    const elements = document.querySelectorAll(elementSelector);
    if (elements.length > instance) {
        elements[instance].scrollIntoView({ behavior: 'smooth' });
    }
}

const link1 = document.getElementById("link1");
const link2 = document.getElementById("link2");
const link3 = document.getElementById("link3");
const link4 = document.getElementById("link4");

link1.addEventListener('click', () => {
    scrollToElement('.header');
});

link2.addEventListener('click', () => {
    scrollToElement('.header', 1);
});

link3.addEventListener('click', () => {
    scrollToElement('.header', 2);
});

link4.addEventListener('click', () => {
    scrollToElement('.column');
});

document.getElementById('openResume').addEventListener('click', function() {
    window.open('static/Misbah Tajuddin Shaikh Resume.pdf', '_blank');
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

function openLink(url) {
  window.open(url, "_blank");
}
