// app.js ကိုပြင်ပါ
const optimize = {
  lazyLoad: () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const video = entry.target;
          video.src = video.dataset.src;
          observer.unobserve(video);
        }
      });
    });
    
    document.querySelectorAll('video[data-src]').forEach(video => {
      observer.observe(video);
    });
  },
  cacheAssets: async () => {
    if ('serviceWorker' in navigator) {
      await navigator.serviceWorker.register('/sw.js');
    }
  }
};
