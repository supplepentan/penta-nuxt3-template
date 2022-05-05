<script>
import PostsFormAxios from "./components/PostsFormAxios.vue";
import PostsText from "./components/PostsText.vue";
export default {
    head() {
        return {
            script: [
                {
                    src: "./assets/js/bootstrap.bundle.min.js"
                }
            ],
            link: [
                {
                    rel: "stylesheet",
                    href: "./assets/css/bootstrap.min.css"
                }
            ]
        };
    },
    components: { PostsText, PostsFormAxios }
}
</script>

<template>
  <div class="container-fluid">
    <PostsForm />
    <Header />
    <NuxtPage />
    <Footer /> 
  </div>
</template>

<style>
</style>