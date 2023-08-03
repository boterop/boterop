const SYSTEM_USAGE_URL = "https://api.boterop.io/system-usage";

let interval_sec = 5;

const numbersTillPoint = number => number.toString().split('.')[0].length

const format = bytes => {
    units = ['B', 'KB', 'MB', 'GB', 'TB'];
    currentUnit = 0;
    result = bytes
    while (numbersTillPoint(result) > 3 && currentUnit < units.length-1) {
        currentUnit++;
        result /= 1000
    }
    return `${result.toFixed(1)}${units[currentUnit]}`;
}

const update = () => {
    axios.get(SYSTEM_USAGE_URL)
        .then(({ data }) => {
            cpu_bar.style.width = `${data.CPU.percent}%`;
            swap_bar.style.width = `${data.SWAP.percent}%`;
            memory_bar.style.width = `${data.MEMORY.percent}%`;
            disk_bar.style.width = `${data.DISK.percent}%`;

            cpu_text.textContent = `${data.CPU.percent}%`;
            swap_text.textContent = `${data.SWAP.percent}%`;
            memory_text.textContent = `${data.MEMORY.percent}%`;
            disk_text.textContent = `${data.DISK.percent}%`;

            swap_title.textContent = `${format(data.SWAP.used)}/${format(data.SWAP.total)}`;
            memory_title.textContent = `${format(data.MEMORY.used)}/${format(data.MEMORY.total)}`;
            disk_title.textContent = `${format(data.DISK.used)}/${format(data.DISK.total)}`;
        })
        .catch(function (error) {
            console.error(error);
        });
}

window.onload = function () {
    cpu_bar = document.getElementById("cpu_bar");
    swap_bar = document.getElementById("swap_bar");
    memory_bar = document.getElementById("memory_bar");
    disk_bar = document.getElementById("disk_bar");

    cpu_text = document.getElementById("cpu_text");
    swap_text = document.getElementById("swap_text");
    memory_text = document.getElementById("memory_text");
    disk_text = document.getElementById("disk_text");

    swap_title = document.getElementById("swap_title");
    memory_title = document.getElementById("memory_title");
    disk_title = document.getElementById("disk_title");

    update();
    setInterval(() => update(), interval_sec * 1000);
}