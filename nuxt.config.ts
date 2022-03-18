import { defineNuxtConfig } from 'nuxt3'

// https://v3.nuxtjs.org/docs/directory-structure/nuxt.config
export default defineNuxtConfig({
    meta: {                      // !!Nuxt3からheadになったので注意！！！
        htmlAttrs: {
            lang: 'ja',
            'data-theme': "cupcake"  // テーマを選択
        },
        title: 'さぷりぺんたんの世界',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: 'assets/favicon.ico' },
        ]
    },
})
