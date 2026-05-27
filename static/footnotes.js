// Footnote popover: click the superscript ref → show popover with footnote text
// (replaces jump-to-bottom navigation)
(function () {
  'use strict';

  function closePopovers() {
    document.querySelectorAll('.fn-popover').forEach(function (p) { p.remove(); });
  }

  function buildPopoverHtml(footnoteEl) {
    // Clone, then strip the back-reference arrow (↩) link mistune adds
    var clone = footnoteEl.cloneNode(true);
    clone.querySelectorAll('a.footnote-backref').forEach(function (a) { a.remove(); });
    return clone.innerHTML.trim();
  }

  function positionPopover(popover, anchor) {
    var rect = anchor.getBoundingClientRect();
    var top = rect.bottom + window.scrollY + 8;
    var left = rect.left + window.scrollX - 12;
    // Keep within viewport horizontally
    var maxLeft = window.scrollX + window.innerWidth - popover.offsetWidth - 12;
    if (left > maxLeft) left = maxLeft;
    if (left < 8) left = 8;
    popover.style.top = top + 'px';
    popover.style.left = left + 'px';
  }

  function showPopover(anchor) {
    var href = anchor.getAttribute('href');
    if (!href || !href.startsWith('#')) return;
    var target = document.getElementById(href.slice(1));
    if (!target) return;

    closePopovers();
    var popover = document.createElement('div');
    popover.className = 'fn-popover';
    popover.setAttribute('role', 'tooltip');
    popover.innerHTML =
      '<button class="fn-close" aria-label="Close">&times;</button>' +
      buildPopoverHtml(target);
    document.body.appendChild(popover);
    positionPopover(popover, anchor);

    popover.querySelector('.fn-close').addEventListener('click', function (e) {
      e.stopPropagation();
      closePopovers();
    });
  }

  document.addEventListener('click', function (e) {
    var refLink = e.target.closest('sup.footnote-ref > a, a.footnote-ref');
    if (refLink) {
      e.preventDefault();
      showPopover(refLink);
      return;
    }
    // Click outside an open popover → close
    if (!e.target.closest('.fn-popover')) closePopovers();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closePopovers();
  });

  window.addEventListener('scroll', closePopovers, { passive: true });
  window.addEventListener('resize', closePopovers);
})();
