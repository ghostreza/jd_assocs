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
        const setMenuState = (isOpen) => {
            navLinks.classList.toggle('mobile-open', isOpen);
            hamburger.classList.toggle('is-open', isOpen);
            hamburger.setAttribute('aria-expanded', String(isOpen));
            hamburger.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
        };

        hamburger.addEventListener('click', () => {
            setMenuState(!navLinks.classList.contains('mobile-open'));
        });
        navLinks.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => setMenuState(false));
        });
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') setMenuState(false);
        });
    }

    const contactForm = document.querySelector('#contactForm');
    if (contactForm) {
        const subjectInput = contactForm.querySelector('[name="subject"]');
        const querySubject = new URLSearchParams(window.location.search).get('subject');
        if (querySubject && subjectInput && !subjectInput.value) subjectInput.value = querySubject;

        contactForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const formData = new FormData(contactForm);
            const name = formData.get('name');
            const organization = formData.get('organization') || '-';
            const need = formData.get('need');
            const subject = formData.get('subject') || need;
            const message = formData.get('message');
            const body = `Hello J&D Associates,\n\nMy name is ${name}.\nOrganization: ${organization}\nRequirement: ${need}\nProduct / subject: ${subject}\n\n${message}\n\nThank you.`;
            const channel = formData.get('channel');

            if (channel === 'whatsapp') {
                window.open(`https://wa.me/6287775382824?text=${encodeURIComponent(body)}`, '_blank', 'noopener');
            } else {
                window.location.href = `mailto:JD.associates800@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            }
        });
    }

    const mainProductImage = document.querySelector('#productMainImage');
    if (mainProductImage) {
        document.querySelectorAll('.gallery-thumb').forEach((thumbnail) => {
            thumbnail.addEventListener('click', () => {
                mainProductImage.src = thumbnail.dataset.image;
                document.querySelectorAll('.gallery-thumb').forEach((item) => item.classList.remove('is-active'));
                thumbnail.classList.add('is-active');
            });
        });
    }
});