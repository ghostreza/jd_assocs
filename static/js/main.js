document.addEventListener('DOMContentLoaded', () => {
    const intro = document.getElementById('siteIntro');
    const heroContent = document.querySelector('.hero-content');
    if (intro) {
        setTimeout(() => {
            heroContent?.classList.add('hero-ready');
            intro.style.display = 'none';
        }, 3950);
    } else {
        heroContent?.classList.add('hero-ready');
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in-up').forEach(el => {
        observer.observe(el);
    });

    const slideshow = document.querySelector('[data-product-slideshow]');
    if (slideshow) {
        const slides = [...slideshow.querySelectorAll('.hero-product-slide')];
        const counter = slideshow.querySelector('.hero-product-counter');
        const progress = slideshow.querySelector('.hero-product-progress i');
        let activeIndex = 0;

        const showSlide = (index) => {
            slides.forEach((slide, slideIndex) => slide.classList.toggle('is-active', slideIndex === index));
            if (counter) counter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
            if (progress) progress.style.transform = `scaleX(${(index + 1) / slides.length})`;
        };

        if (slides.length > 1) {
            showSlide(activeIndex);
            window.setInterval(() => {
                activeIndex = (activeIndex + 1) % slides.length;
                showSlide(activeIndex);
            }, 4800);
        }
    }

    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('mobile-open');
            navLinks.style.display = isOpen ? 'flex' : 'none';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '70px';
            navLinks.style.right = '0';
            navLinks.style.background = 'rgba(5,16,22,0.98)';
            navLinks.style.width = '100%';
            navLinks.style.padding = '20px';
            navLinks.style.borderTop = '1px solid rgba(180,201,214,0.18)';
            navLinks.style.zIndex = '1200';
        });
    }
});