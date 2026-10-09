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

    document.querySelectorAll('.associates-network-canvas').forEach((networkCanvas) => {
        const networkContext = networkCanvas.getContext('2d');
        const networkPanel = networkCanvas.parentElement;
        const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

        if (networkContext && networkPanel) {
            const particles = [];
            const pointer = { x: null, y: null };
            let panelWidth = 0;
            let panelHeight = 0;
            let animationFrame = 0;
            let panelIsVisible = false;

            const resizeNetwork = () => {
                const bounds = networkPanel.getBoundingClientRect();
                const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
                panelWidth = bounds.width;
                panelHeight = bounds.height;
                networkCanvas.width = Math.round(panelWidth * pixelRatio);
                networkCanvas.height = Math.round(panelHeight * pixelRatio);
                networkContext.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
                particles.length = 0;

                const particleCount = Math.max(38, Math.min(200, Math.round((panelWidth * panelHeight) / 3000)));
                for (let index = 0; index < particleCount; index += 1) {
                    const angle = Math.random() * Math.PI * 2;
                    const speed = 0.12 + Math.random() * 0.22;
                    particles.push({
                        x: Math.random() * panelWidth,
                        y: Math.random() * panelHeight,
                        vx: Math.cos(angle) * speed,
                        vy: Math.sin(angle) * speed,
                        radius: 0.9 + Math.random() * 1.1
                    });
                }
                drawNetwork(false);
            };

            const drawNetwork = (moveParticles) => {
                networkContext.clearRect(0, 0, panelWidth, panelHeight);

                particles.forEach((particle) => {
                    if (moveParticles) {
                        particle.x += particle.vx;
                        particle.y += particle.vy;
                        if (particle.x < 0 || particle.x > panelWidth) particle.vx *= -1;
                        if (particle.y < 0 || particle.y > panelHeight) particle.vy *= -1;
                    }
                });

                for (let firstIndex = 0; firstIndex < particles.length; firstIndex += 1) {
                    const first = particles[firstIndex];
                    for (let secondIndex = firstIndex + 1; secondIndex < particles.length; secondIndex += 1) {
                        const second = particles[secondIndex];
                        const distance = Math.hypot(first.x - second.x, first.y - second.y);
                        if (distance < 88) {
                            networkContext.strokeStyle = `rgba(121, 213, 206, ${(1 - distance / 88) * 0.32})`;
                            networkContext.lineWidth = 0.7;
                            networkContext.beginPath();
                            networkContext.moveTo(first.x, first.y);
                            networkContext.lineTo(second.x, second.y);
                            networkContext.stroke();
                        }
                    }

                    if (pointer.x !== null) {
                        const distance = Math.hypot(first.x - pointer.x, first.y - pointer.y);
                        if (distance < 105) {
                            networkContext.strokeStyle = `rgba(215, 183, 127, ${(1 - distance / 105) * 0.5})`;
                            networkContext.lineWidth = 1;
                            networkContext.beginPath();
                            networkContext.moveTo(first.x, first.y);
                            networkContext.lineTo(pointer.x, pointer.y);
                            networkContext.stroke();
                        }
                    }

                    networkContext.fillStyle = 'rgba(215, 183, 127, 0.78)';
                    networkContext.beginPath();
                    networkContext.arc(first.x, first.y, first.radius, 0, Math.PI * 2);
                    networkContext.fill();
                }
            };

            const animateNetwork = () => {
                animationFrame = 0;
                if (!panelIsVisible || reducedMotion.matches) return;
                drawNetwork(true);
                animationFrame = window.requestAnimationFrame(animateNetwork);
            };

            const visibilityObserver = new IntersectionObserver(([entry]) => {
                panelIsVisible = entry.isIntersecting;
                if (panelIsVisible && !reducedMotion.matches && !animationFrame) {
                    animationFrame = window.requestAnimationFrame(animateNetwork);
                } else if (!panelIsVisible && animationFrame) {
                    window.cancelAnimationFrame(animationFrame);
                    animationFrame = 0;
                }
            });

            networkPanel.addEventListener('pointermove', (event) => {
                const bounds = networkPanel.getBoundingClientRect();
                pointer.x = event.clientX - bounds.left;
                pointer.y = event.clientY - bounds.top;
            });
            networkPanel.addEventListener('pointerleave', () => {
                pointer.x = null;
                pointer.y = null;
            });
            new ResizeObserver(resizeNetwork).observe(networkPanel);
            reducedMotion.addEventListener('change', () => {
                if (reducedMotion.matches && animationFrame) {
                    window.cancelAnimationFrame(animationFrame);
                    animationFrame = 0;
                    drawNetwork(false);
                } else if (!reducedMotion.matches && panelIsVisible && !animationFrame) {
                    animationFrame = window.requestAnimationFrame(animateNetwork);
                }
            });
            visibilityObserver.observe(networkPanel);
        }
    });

    const economyCanvas = document.querySelector('.craft-economy-canvas');
    if (economyCanvas) {
        const context = economyCanvas.getContext('2d');
        const hero = economyCanvas.parentElement;
        const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

        if (context && hero) {
            let width = 0;
            let height = 0;
            let animationFrame = 0;
            let heroIsVisible = false;
            let phase = 0;
            const trend = [0.72, 0.68, 0.73, 0.59, 0.64, 0.51, 0.56, 0.4, 0.46, 0.31, 0.36, 0.22];

            const drawChart = (animate) => {
                context.clearRect(0, 0, width, height);
                const compactLayout = width <= 760;
                const left = width * (compactLayout ? 0.08 : 0.43);
                const right = width * 0.97;
                const top = height * (compactLayout ? 0.72 : 0.12);
                const bottom = height * (compactLayout ? 0.96 : 0.9);
                const chartWidth = right - left;
                const chartHeight = bottom - top;

                context.lineWidth = 1;
                for (let index = 0; index <= 6; index += 1) {
                    const x = left + (chartWidth / 6) * index;
                    context.strokeStyle = 'rgba(121, 213, 206, 0.1)';
                    context.beginPath();
                    context.moveTo(x, top);
                    context.lineTo(x, bottom);
                    context.stroke();
                }
                for (let index = 0; index <= 4; index += 1) {
                    const y = top + (chartHeight / 4) * index;
                    context.strokeStyle = 'rgba(121, 213, 206, 0.1)';
                    context.beginPath();
                    context.moveTo(left, y);
                    context.lineTo(right, y);
                    context.stroke();
                }

                const points = trend.map((value, index) => ({
                    x: left + (chartWidth / (trend.length - 1)) * index,
                    y: top + chartHeight * value
                }));

                points.forEach((point, index) => {
                    const candleWidth = Math.max(3, Math.min(8, chartWidth / 64));
                    const swing = Math.sin(index * 2.1) * chartHeight * 0.045;
                    const openY = point.y + swing;
                    const closeY = point.y - swing * 0.72;
                    const color = closeY < openY ? '201, 162, 89' : '93, 178, 171';
                    context.strokeStyle = `rgba(${color}, 0.46)`;
                    context.fillStyle = `rgba(${color}, 0.2)`;
                    context.beginPath();
                    context.moveTo(point.x, Math.min(openY, closeY) - candleWidth * 1.4);
                    context.lineTo(point.x, Math.max(openY, closeY) + candleWidth * 1.4);
                    context.stroke();
                    context.fillRect(point.x - candleWidth / 2, Math.min(openY, closeY), candleWidth, Math.max(3, Math.abs(closeY - openY)));
                });

                context.beginPath();
                points.forEach((point, index) => {
                    if (index === 0) context.moveTo(point.x, point.y);
                    else context.lineTo(point.x, point.y);
                });
                context.strokeStyle = 'rgba(215, 183, 127, 0.72)';
                context.lineWidth = 1.6;
                context.shadowBlur = 12;
                context.shadowColor = 'rgba(215, 183, 127, 0.48)';
                context.stroke();
                context.shadowBlur = 0;

                const markerPosition = (phase % 1) * (points.length - 1);
                const markerIndex = Math.floor(markerPosition);
                const markerProgress = markerPosition - markerIndex;
                const markerStart = points[markerIndex];
                const markerEnd = points[Math.min(markerIndex + 1, points.length - 1)];
                const markerX = markerStart.x + (markerEnd.x - markerStart.x) * markerProgress;
                const markerY = markerStart.y + (markerEnd.y - markerStart.y) * markerProgress;

                context.beginPath();
                context.arc(markerX, markerY, 3.2, 0, Math.PI * 2);
                context.fillStyle = '#d7b77f';
                context.shadowBlur = 15;
                context.shadowColor = 'rgba(215, 183, 127, 0.8)';
                context.fill();
                context.shadowBlur = 0;

                if (animate) phase = (phase + 0.0016) % 1;
            };

            const resizeChart = () => {
                const bounds = hero.getBoundingClientRect();
                const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
                width = bounds.width;
                height = bounds.height;
                economyCanvas.width = Math.round(width * pixelRatio);
                economyCanvas.height = Math.round(height * pixelRatio);
                context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
                drawChart(false);
            };

            const animateChart = () => {
                animationFrame = 0;
                if (!heroIsVisible || reducedMotion.matches) return;
                drawChart(true);
                animationFrame = window.requestAnimationFrame(animateChart);
            };

            const visibilityObserver = new IntersectionObserver(([entry]) => {
                heroIsVisible = entry.isIntersecting;
                if (heroIsVisible && !reducedMotion.matches && !animationFrame) {
                    animationFrame = window.requestAnimationFrame(animateChart);
                } else if (!heroIsVisible && animationFrame) {
                    window.cancelAnimationFrame(animationFrame);
                    animationFrame = 0;
                }
            });

            new ResizeObserver(resizeChart).observe(hero);
            reducedMotion.addEventListener('change', () => {
                if (reducedMotion.matches && animationFrame) {
                    window.cancelAnimationFrame(animationFrame);
                    animationFrame = 0;
                    drawChart(false);
                } else if (!reducedMotion.matches && heroIsVisible && !animationFrame) {
                    animationFrame = window.requestAnimationFrame(animateChart);
                }
            });
            visibilityObserver.observe(hero);
        }
    }

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