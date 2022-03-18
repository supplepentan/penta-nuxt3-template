<script setup lang="ts">
interface Props {
  name: string
  to?: string
}

const props = withDefaults(defineProps<Props>(), {
  name: '',
  to: '/'
})
</script>

<template>
  <div>
    <a :href="to" class="btn btn-light">
      {{ name }}
    </a>
  </div>
</template>