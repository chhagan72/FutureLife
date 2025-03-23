document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    let isDown = false;
    let startX;
    let scrollLeft;

    // Auto slide
    let autoSlide = setInterval(() => {
        slider.style.transform = `translateX(-${100}px)`;
        slider.appendChild(slider.firstElementChild);
        slider.style.transition = 'none';
        slider.style.transform = 'translateX(0)';
        setTimeout(() => slider.style.transition = 'transform 0.5s ease-in-out', 50);
    }, 3000); // Adjust timing as needed

    // Mouse click slide
    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.style.transition = 'none';
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
        clearInterval(autoSlide);
    });

    slider.addEventListener('mouseleave', () => {
        isDown = false;
    });

    slider.addEventListener('mouseup', () => {
        isDown = false;
        autoSlide = setInterval(() => {
            slider.style.transform = `translateX(-${100}px)`;
            slider.appendChild(slider.firstElementChild);
            slider.style.transition = 'none';
            slider.style.transform = 'translateX(0)';
            setTimeout(() => slider.style.transition = 'transform 0.5s ease-in-out', 50);
        }, 3000); // Adjust timing as needed
    });

    slider.addEventListener('mousemove', (e) => {
        if(!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 2; // Adjust the multiplier as needed
        slider.scrollLeft = scrollLeft - walk;
    });
});
    



