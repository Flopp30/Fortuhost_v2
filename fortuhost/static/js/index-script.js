document.addEventListener('DOMContentLoaded', function () {

    const start = document.getElementById('start');
    const card = document.querySelectorAll('.about__card');
    const btn = document.querySelector('.hero__btn');
    const laptop = document.querySelector('.hero__bg-laptop-color');
    const laptopBlur = document.querySelector('.hero__bg-laptop-blur');
    const btnHdd = document.querySelector('.hero__bg-hdd');
    const btnServer = document.querySelector('.hero__bg-server');
    const descr = document.querySelector('.hero__description');
    const btnCable = document.querySelectorAll('.hero__bg-cable');
    const btnCableBlur = document.querySelectorAll('.hero__bg-cable-blur');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 400) {
            card.forEach(el => el.classList.add('about__card-scroll'));
        } else {
            card.forEach(el => el.classList.remove('about__card-scroll'));
        }

        if (window.pageYOffset > 1190) {
            start.classList.add('start-bg');
        } else {
            start.classList.remove('start-bg');
        }
    }, {passive: true});

    btn.addEventListener('mouseover', () => {
        btn.classList.add('hero__btn--hover');
        laptop.classList.add('hero__bg-laptop-color--active');
        setTimeout(() => {
            laptopBlur.classList.add('hero__bg-laptop-blur--active');
            btnCable.forEach(el => el.classList.add('hero__bg-cable--active'));
            btnCableBlur.forEach(el => el.classList.add('hero__bg-cable-blur--active'));
        }, 600);

        btnHdd.classList.add('hero__bg-hdd--active');
        btnServer.classList.add('hero__bg-server--active');
        descr.classList.add('hero__description--active');

    });
    btn.addEventListener('mouseout', () => {
        btn.classList.remove('hero__btn--hover');
        laptop.classList.remove('hero__bg-laptop-color--active');

        laptopBlur.classList.remove('hero__bg-laptop-blur--active');
        btnHdd.classList.remove('hero__bg-hdd--active');
        btnServer.classList.remove('hero__bg-server--active');
        descr.classList.remove('hero__description--active');
        btnCable.forEach(el => el.classList.remove('hero__bg-cable--active'));
        btnCableBlur.forEach(el => el.classList.remove('hero__bg-cable-blur--active'));
    });

    btn.addEventListener('mousedown', () => btn.classList.add('hero__btn--active'));
    btn.addEventListener('mouseup', () => btn.classList.remove('hero__btn--active'));

    const cards = document.querySelectorAll('.rates__card');
    const blockText = document.querySelectorAll('.rates__card-text');

// cards.forEach(el => el.addEventListener('mouseover', () => blockText.forEach(el => setTimeout(el.classList.add('visible'), 1000))));
// cards.forEach(el => el.addEventListener('mouseout', () => blockText.forEach(el => el.classList.remove('visible'))));

    new JustValidate('.registration__form', {
        colorWrong: '#FF0000',
        borderWrong: "3px solid #FF0000",
        rules: {
            name: {
                required: true,
                minLenght: 2,
                maxLenght: 30,
            },
            surName: {
                required: true,
                minLenght: 2,
                maxLenght: 30,
            },
            mail: {
                required: true,
                email: true
            },
            checkbox: {
                required: true,
            }
        },
        messages: {
            name: "Ошибка. Введите имя",
            surName: "Ошибка. Введите фамилию",
            mail: "Ошибка. Введите email",
        },

    });

});

