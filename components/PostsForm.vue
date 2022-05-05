<script setup>
import FormData from 'form-data'; //インストールの必要あり: yarn add form-data
const previewBase64 = ref();
const previewBase64_after = ref("initial");
const uploadfile = ref();
const file = ref([]);
const fileSelected = (event) => {
      const reader = new FileReader();
      reader.onload = (event) => {
          previewBase64.value = event.target.result;
      };
      //reader.readAsDataURL(event.target.files[0]);
      //formData.append("img", event.target.files[0]);
      //formData.value.append("img", reader.readAsDataURL(event.target.files[0]));
      //uploadfile.value = reader.readAsDataURL(event.target.files[0]);
      file.value = event.target.files[0]
      console.log("ここ①", file.value)
      };
const submit = () => {
    console.log("ここ②", file.value);
    const formData = new FormData();
    formData.append("img", file.value);
    const {data} = fetch("http://192.168.0.29:8000/image", {
        method: "post",
        body: formData,
    });
    previewBase64_after.value = data.value
};
</script>

<template>
<div>
インプット：{{previewBase64}}
<br/>
アップロードファイル： {{file}}
<br/>
リターン：{{previewBase64_after}}
<br/>
フォームデータ：{{formData}}
</div>
インプット：<img v-bind:src="previewBase64" class="img-fluid" alt="" />
リターン：<img v-bind:src="previewBase64_after" class="img-fluid" alt="" />
<div>
<input type="file" v-on:change="fileSelected" name="file"/>
<button @click="submit">送信</button>
</div>
</template>