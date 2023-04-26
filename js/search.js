let element = document.getElementById("pos");

let parent = element.parentNode;

// задаем новые значения координат позиционирования
element.style.position = "absolute";
element.style.top = ((parent.offsetHeight - element.offsetHeight) / 2) + "px";
element.style.left = ((parent.offsetWidth - element.offsetWidth) / 2) + "px";
