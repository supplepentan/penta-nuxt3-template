<script setup>
import FormData from 'form-data'; //インストールの必要あり: yarn add form-data
const formData = ref(new FormData());
const previewBase64_after = ref("initial");
const fileSelected = (event) => {
      const reader = new FileReader();
      reader.onload = (event) => {
          previewBase64.value = event.target.result;
      };
      reader.readAsDataURL(event.target.files[0]);
    //const formData = new FormData();
    formData.append(event.target.files[0]);
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
<br/>
リターン：{{previewBase64_after}}
<br/>
フォームデータ：{{formData}}
</div>
インプット：<img v-bind:src="previewBase64" class="img-fluid" alt="" />
リターン：<img v-bind:src="previewBase64_after" class="img-fluid" alt="" />
<input type="file" v-on:change="fileSelected" />
<button @click="submit">送信</button>
</template>