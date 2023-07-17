let SYSTEM_USAGE_URL = "http://api.boterop.io/system-usage"

let interval_sec = 5;

const update = () => {
    axios.get(SYSTEM_USAGE_URL)
        .then(({ data }) => {
            cpu_bar.style.width = `${data.CPU.percent}%`;
            swap_bar.style.width = `${data.SWAP.percent}%`;
            memory_bar.style.width = `${data.MEMORY.percent}%`;

            cpu_text.textContent = `${data.CPU.percent}%`;
            swap_text.textContent = `${data.SWAP.percent}%`;
            memory_text.textContent = `${data.MEMORY.percent}%`;
        })
        .catch(function (error) {
            console.error(error);
        });
}

window.onload = function () {
    cpu_bar = document.getElementById("cpu_bar");
    swap_bar = document.getElementById("swap_bar");
    memory_bar = document.getElementById("memory_bar");

    cpu_text = document.getElementById("cpu_text");
    swap_text = document.getElementById("swap_text");
    memory_text = document.getElementById("memory_text");

    update();
    setInterval(() => update(), interval_sec * 1000);
}