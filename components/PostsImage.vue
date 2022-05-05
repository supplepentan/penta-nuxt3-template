<script setup>
const previewBase64 = ref("initial");
const previewBase64_after = ref("initial");
const fileSelected = (event) => {
      const reader = new FileReader();
      reader.onload = (event) => {
          previewBase64.value = event.target.result;
      };
      reader.readAsDataURL(event.target.files[0]);//データを base64 データurl にエンコードします
    };
const submit = () => {
    const {data} = useFetch("http://192.168.0.29:8000/image", {
        method: "post",
        params: {data: previewBase64.value},
    });
    previewBase64_after.value = data.value
};
</script>

<template>
<div>
インプット：{{previewBase64}}
リターン：{{previewBase64_after}}
</div>
インプット：<img v-bind:src="previewBase64" class="img-fluid" alt="" />
リターン：<img v-bind:src="previewBase64_after" class="img-fluid" alt="" />
<input type="file" v-on:change="fileSelected" />
<button @click="submit">送信</button>
</template>