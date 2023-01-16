const name = document.getElementById('name');
const details = document.getElementsByClassName('content-item');

const sound = new Audio('/static/food-details/click.wav');
sound.volume = 0.1;


const handleClick = () => {
    sound.play();
}

name.addEventListener('click', handleClick);
for (const detail of details) {
    detail.addEventListener('click', handleClick);
}
