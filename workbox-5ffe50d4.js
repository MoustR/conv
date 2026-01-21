// Simplified Workbox for local development
const workbox = {
    core: {
        setCacheNameDetails: () => {},
        clientsClaim: () => {},
        skipWaiting: () => {}
    },
    routing: {
        registerRoute: () => {},
        setDefaultHandler: () => {},
        setCatchHandler: () => {}
    },
    strategies: {
        CacheFirst: class {
            constructor() {}
            handle() { return Promise.resolve(new Response()); }
        },
        NetworkFirst: class {
            constructor() {}
            handle() { return Promise.resolve(new Response()); }
        },
        StaleWhileRevalidate: class {
            constructor() {}
            handle() { return Promise.resolve(new Response()); }
        }
    },
    precaching: {
        precacheAndRoute: () => {}
    }
};

self.workbox = workbox;