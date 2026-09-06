(function () {
  var root = document.documentElement;
  var themeButton = document.getElementById("theme-toggle-button");
  var themeIcon = document.getElementById("theme-icon");
  var masthead = document.querySelector(".masthead");

  var setTheme = function (theme) {
    var useTheme = theme;
    if (!useTheme) {
      try {
        useTheme = localStorage.getItem("theme");
      } catch (error) {
        useTheme = null;
      }
    }
    if (!useTheme) {
      useTheme = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
    }

    var isDark = useTheme === "dark";
    if (isDark) {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }

    if (themeIcon) {
      themeIcon.classList.toggle("fa-moon", isDark);
      themeIcon.classList.toggle("fa-sun", !isDark);
    }
    if (themeButton) {
      themeButton.setAttribute("aria-pressed", isDark ? "true" : "false");
      themeButton.setAttribute(
        "aria-label",
        isDark ? "Switch to light theme" : "Switch to dark theme"
      );
    }
  };

  setTheme();

  if (themeButton) {
    themeButton.addEventListener("click", function () {
      var nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      try {
        localStorage.setItem("theme", nextTheme);
      } catch (error) {
        /* Ignore storage failures. */
      }
      setTheme(nextTheme);
    });
  }

  var syncMastheadOffset = function () {
    if (!masthead) {
      return;
    }
    document.body.style.paddingTop = masthead.offsetHeight + "px";
  };

  syncMastheadOffset();
  window.addEventListener("resize", syncMastheadOffset);
})();
