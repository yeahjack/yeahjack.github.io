(function () {
  'use strict';
  var root = document.querySelector('.academic-home--refined');
  if (!root) return;

  var hover = root.querySelector('#preview-figure-hover');
  var hoverImage = hover.querySelector('img');
  var dialog = root.querySelector('#preview-figure-dialog');
  var dialogImage = dialog.querySelector('img');
  var closeButton = dialog.querySelector('.preview-figure-dialog__close');
  var title = dialog.querySelector('#preview-figure-title');
  var paperLink = dialog.querySelector('.preview-figure-dialog__paper');
  var mouseHover = window.matchMedia('(hover: hover) and (pointer: fine)');
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var pendingHover = null;
  var activeTrigger = null;
  var dialogRequest = 0;
  var hoverTimer = null;
  var themeTimer = null;

  function hideHover() {
    clearTimeout(hoverTimer);
    pendingHover = null;
    hover.hidden = true;
  }

  function positionHover(trigger, image) {
    if (pendingHover !== trigger || dialog.open) return;
    var ratio = image.naturalWidth / image.naturalHeight;
    var contentWidth = Math.min(500, window.innerWidth - 64, (window.innerHeight - 130) * ratio, 340 * ratio);
    var width = contentWidth + 18;
    var height = contentWidth / ratio + 18;
    var rect = trigger.getBoundingClientRect();
    var left = rect.right + 18;
    if (left + width > window.innerWidth - 24) left = rect.left - width - 18;
    left = Math.max(24, Math.min(left, window.innerWidth - width - 24));
    var top = Math.max(80, Math.min(rect.top + (rect.height - height) / 2, window.innerHeight - height - 24));
    hoverImage.src = image.currentSrc || image.src;
    hover.style.width = width + 'px';
    hover.style.height = height + 'px';
    hover.style.left = left + 'px';
    hover.style.top = top + 'px';
    hover.hidden = false;
  }

  function showHover(trigger) {
    var image = new Image();
    image.src = trigger.dataset.previewImage;
    image.decode().then(function () { positionHover(trigger, image); }).catch(hideHover);
  }

  function fitDialog() {
    if (!activeTrigger) return;
    var sourceWidth = Number(activeTrigger.dataset.previewWidth);
    var sourceHeight = Number(activeTrigger.dataset.previewHeight);
    if (!sourceWidth || !sourceHeight) return;
    var sharpWidth = Math.floor(sourceWidth / Math.max(1, window.devicePixelRatio));
    dialogImage.style.maxWidth = 'min(100%, ' + sharpWidth + 'px)';
    var contentWidth = Math.min(sharpWidth, window.innerHeight * 0.65 * sourceWidth / sourceHeight);
    dialog.style.width = Math.min(1060, window.innerWidth - (window.innerWidth <= 760 ? 16 : 48), contentWidth + 64) + 'px';
  }
  dialogImage.addEventListener('load', fitDialog);

  root.querySelectorAll('.preview-figure-trigger').forEach(function (trigger) {
    trigger.addEventListener('pointerenter', function (event) {
      if (!mouseHover.matches || event.pointerType !== 'mouse') return;
      hideHover();
      pendingHover = trigger;
      hoverTimer = setTimeout(function () { showHover(trigger); }, 150);
    });
    trigger.addEventListener('pointerleave', hideHover);
    trigger.addEventListener('click', function (event) {
      hideHover();
      var image = trigger.querySelector('img');
      activeTrigger = trigger;
      var request = ++dialogRequest;
      dialog.style.width = '';
      dialogImage.style.maxWidth = '100%';
      dialogImage.src = image.currentSrc || image.src;
      dialogImage.alt = image.alt;
      title.textContent = trigger.dataset.paperTitle;
      var paperUrl = trigger.dataset.paperUrl;
      paperLink.parentElement.hidden = !paperUrl;
      dialog.classList.toggle('preview-figure-dialog--no-paper', !paperUrl);
      if (paperUrl) paperLink.href = paperUrl;
      else paperLink.removeAttribute('href');
      dialog.classList.toggle('is-keyboard-open', event.detail === 0);
      dialog.showModal();
      fitDialog();
      var original = new Image();
      original.src = trigger.dataset.previewImage;
      original.decode().then(function () {
        if (dialog.open && request === dialogRequest) dialogImage.src = original.src;
      }).catch(function () { /* Keep the already visible thumbnail if the original cannot load. */ });
    });
  });

  closeButton.addEventListener('click', function () { dialog.close(); });
  dialog.addEventListener('click', function (event) {
    if (event.target !== dialog) return;
    var rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  dialog.addEventListener('close', function () {
    dialogRequest++;
    if (activeTrigger) activeTrigger.focus({ preventScroll: true });
  });
  window.addEventListener('scroll', hideHover, { passive: true });
  window.addEventListener('resize', function () {
    hideHover();
    if (dialog.open) fitDialog();
  }, { passive: true });

  var themeButton = document.getElementById('theme-toggle-button');
  if (themeButton) {
    themeButton.addEventListener('pointerenter', function () {
      if (!reducedMotion.matches) document.body.classList.add('is-theme-switching');
    });
    themeButton.addEventListener('pointerleave', function () {
      clearTimeout(themeTimer);
      themeTimer = setTimeout(function () { document.body.classList.remove('is-theme-switching'); }, 180);
    });
    themeButton.addEventListener('click', function (event) {
      clearTimeout(themeTimer);
      if (event.detail === 0 || reducedMotion.matches) document.body.classList.remove('is-theme-switching');
      themeTimer = setTimeout(function () { document.body.classList.remove('is-theme-switching'); }, 200);
    }, true);
  }
}());
