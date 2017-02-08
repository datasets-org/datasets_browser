var show_more = function (event) {
    event.preventDefault();
    var elems = event.target.parentNode.parentNode.querySelectorAll("li.hidden");
    elems.forEach(function (entry, i) {
        if (i > 10) {
            return;
        }
        entry.classList.remove("hidden");
    });
};

if (document.querySelector("#changelog_more")) {
    document.querySelector("#changelog_more").addEventListener("click", show_more);
}
if (document.querySelector("#usages_more")) {
    document.querySelector("#usages_more").addEventListener("click", show_more);
}
