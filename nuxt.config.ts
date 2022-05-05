import { defineNuxtConfig } from 'nuxt3';

// https://v3.nuxtjs.org/docs/directory-structure/nuxt.config
export default defineNuxtConfig({
    meta: {
        htmlAttrs: {
            lang: 'ja',
        },
        title: 'さぷりぺんたんの世界 (Penta the World)',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: 'assets/favicon.ico' },
        ]
    },
    modules: []
});
