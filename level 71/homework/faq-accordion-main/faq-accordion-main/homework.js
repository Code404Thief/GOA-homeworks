document.querySelectorAll(".question").forEach(item => {
    item.addEventListener("click", () => {
        const answer = item.nextElementSibling;
        const toggle = item.querySelector(".toggle");

        if (answer.classList.contains("hidden")) {
            answer.classList.remove("hidden");
            toggle.textContent = "-";
        } else {
            answer.classList.add("hidden");
            toggle.textContent = "+";
        }
    });
});
