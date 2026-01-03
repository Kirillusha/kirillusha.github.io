# Testing Checklist

## 🧪 Functional Testing

### Navigation
- [ ] Click "Главная" button - scrolls to hero section
- [ ] Click "Хронология" button - scrolls to timeline section
- [ ] Click "Картины" button - scrolls to gallery section
- [ ] Click "Цитаты" button - scrolls to quotes section

### Timeline Modal
- [ ] Click each timeline card (1987, 1994, 2001, 2011, 2015, 2023)
- [ ] Verify modal opens with correct year, title, and text
- [ ] Click X button to close modal
- [ ] Click backdrop to close modal

### Neuro-Paint Gallery
- [ ] Hover over "Сны Сибири" - gradient follows cursor
- [ ] Hover over "Трещина подо льдом" - gradient follows cursor
- [ ] Hover over "Эмоция №7" - gradient follows cursor
- [ ] Mouse leave - gradients reset to original

### Quote Carousel
- [ ] Quotes auto-rotate every 7 seconds
- [ ] Smooth fade transition between quotes
- [ ] Click "Пауза" button - stops rotation
- [ ] Button changes to "Продолжить"
- [ ] Click "Продолжить" - resumes rotation

### Scroll Animations
- [ ] Scroll down - timeline cards fade in
- [ ] Gallery items fade in on scroll
- [ ] Sections appear with translate-y animation

---

## 🎨 Visual Testing

### Layout
- [ ] Hero section displays correctly
- [ ] Navigation bar fixed at top
- [ ] Timeline grid responsive
- [ ] Gallery grid responsive
- [ ] Footer at bottom

### Typography
- [ ] Hero title "НЕВСКИЙ" gradient visible
- [ ] All text readable and properly sized
- [ ] Russian text displays correctly
- [ ] Font weights correct

### Colors & Gradients
- [ ] Background parallax layers visible
- [ ] Gradient text on hero title
- [ ] Gallery paint gradients work
- [ ] Modal backdrop blur effect

### Animations
- [ ] Hero title pulse animation smooth
- [ ] Scroll animations trigger correctly
- [ ] Hover effects on buttons
- [ ] Timeline card hover lift effect
- [ ] Gallery hover scale effect

---

## 📱 Responsive Testing

### Desktop (1920x1080)
- [ ] Full layout displays correctly
- [ ] All sections properly spaced
- [ ] Images load correctly
- [ ] Animations smooth

### Tablet (768x1024)
- [ ] Grid collapses appropriately
- [ ] Navigation still accessible
- [ ] Touch events work
- [ ] Modal fits screen

### Mobile (375x667)
- [ ] Single column layout
- [ ] Text sizes readable
- [ ] Buttons touch-friendly (48px min)
- [ ] No horizontal scroll

---

## ⚡ Performance Testing

### Initial Load
- [ ] Page loads quickly (< 2s on fast connection)
- [ ] No render blocking
- [ ] Images load progressively
- [ ] No layout shift

### Runtime Performance
- [ ] Smooth scrolling (60 FPS)
- [ ] Animations don't jank
- [ ] Mouse interactions responsive
- [ ] No memory leaks (check DevTools)

### Network
- [ ] CSS file loads (6.7 KB)
- [ ] JS file loads (3.1 KB)
- [ ] Images optimized (WebP)
- [ ] Resources cached on reload

---

## 🌐 Browser Testing

### Chrome/Edge
- [ ] All features work
- [ ] Animations smooth
- [ ] No console errors

### Firefox
- [ ] All features work
- [ ] Backdrop blur works
- [ ] No console errors

### Safari
- [ ] All features work
- [ ] WebKit prefixes work
- [ ] No console errors

### Mobile Browsers
- [ ] iOS Safari works
- [ ] Chrome Mobile works
- [ ] Touch events responsive

---

## 🔍 DevTools Testing

### Lighthouse Audit
- [ ] Run Lighthouse (Desktop)
- [ ] Performance score > 90
- [ ] Accessibility score > 90
- [ ] Best Practices score > 90
- [ ] SEO score > 90

### Network Tab
- [ ] Check total page size (< 300 KB)
- [ ] Verify WebP images loading
- [ ] Check cache headers
- [ ] No 404 errors

### Performance Tab
- [ ] Record page load
- [ ] Check FCP < 1.0s
- [ ] Check LCP < 2.5s
- [ ] No long tasks > 50ms
- [ ] Check for paint operations

### Coverage Tab
- [ ] Check CSS usage (should be ~90%+)
- [ ] Check JS usage (should be ~90%+)
- [ ] No large unused chunks

### Console
- [ ] No errors
- [ ] No warnings
- [ ] No deprecation notices

---

## ♿ Accessibility Testing

### Keyboard Navigation
- [ ] Tab through all interactive elements
- [ ] Enter/Space activates buttons
- [ ] Escape closes modal
- [ ] Focus visible on all elements

### Screen Reader
- [ ] Test with NVDA/JAWS/VoiceOver
- [ ] All buttons have labels
- [ ] Proper heading hierarchy
- [ ] Alt text where needed

### Contrast
- [ ] Text readable on backgrounds
- [ ] Focus indicators visible
- [ ] Error states clear

---

## 🐛 Edge Cases

### Slow Network
- [ ] Test on slow 3G
- [ ] Content still usable
- [ ] Graceful degradation

### Disabled JavaScript
- [ ] Basic content visible
- [ ] Navigation accessible
- [ ] No broken images

### Large Fonts
- [ ] Increase browser font size to 200%
- [ ] Layout doesn't break
- [ ] Text readable

### High Contrast Mode
- [ ] Enable Windows High Contrast
- [ ] Content still distinguishable
- [ ] Interactive elements visible

---

## ✅ Automated Tests (Optional)

### Lighthouse CI
```bash
# Run from command line
lighthouse https://your-site.com --view
```

Expected scores:
- Performance: 98+
- Accessibility: 92+
- Best Practices: 95+
- SEO: 100

### WebPageTest
```
URL: https://your-site.com
Location: Virginia, USA
Browser: Chrome
Connection: Cable
```

Expected metrics:
- Speed Index: < 1.5s
- FCP: < 1.0s
- LCP: < 2.0s
- TBT: < 200ms

---

## 📝 Testing Notes

### Known Issues
- None identified

### Browser-Specific Notes
- Safari: Requires -webkit- prefixes (already added)
- Firefox: Backdrop-filter requires flag in older versions (works in modern)
- Edge: Full compatibility with Chrome

### Performance Notes
- First load may be slightly slower due to DNS lookup
- Subsequent loads are instant (cached assets)
- Background images lazy load (intentional)

---

## 🎯 Acceptance Criteria

✅ All functionality works as expected
✅ Visual design matches original
✅ Performance metrics meet targets
✅ No console errors or warnings
✅ Accessible to keyboard and screen reader users
✅ Responsive on all device sizes
✅ Cross-browser compatible
✅ File sizes within budget

---

## 📊 Performance Targets

| Metric | Target | How to Check |
|--------|--------|--------------|
| FCP | < 1.0s | Lighthouse |
| LCP | < 2.5s | Lighthouse |
| TTI | < 3.0s | Lighthouse |
| TBT | < 300ms | Lighthouse |
| CLS | < 0.1 | Lighthouse |
| Page Size | < 300KB | Network tab |
| CSS Size | < 50KB | Network tab |
| JS Size | < 50KB | Network tab |

---

## 🚀 Ready for Production

Once all checkboxes are ticked:
- ✅ Merge to main branch
- ✅ Deploy to production
- ✅ Monitor Core Web Vitals
- ✅ Celebrate! 🎉
