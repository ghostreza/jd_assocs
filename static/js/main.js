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