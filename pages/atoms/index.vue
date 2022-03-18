<script setup lang="ts">
interface Menus {
  name: string
  to: string
}[]

const menus = reactive<Menus>([
  { name: 'ホーム', to: '/home' },
  { name: 'マイページ', to: '/mypage' },
  { name: '設定', to: '/setting' },
  { name: 'アバウト', to: '/about'}
])
</script>

<template>
  <div>
    <p>単発で呼び出し</p>
    <AtomsTheButton name="ホーム" to="/home" />
    <p>ループで呼び出し</p>
    <div v-for="(v, k) in menus" :key="k">
      <AtomsTheButton :name="v.name" :to="v.to" />
    </div>
  </div>
</template>