<script setup>
const input_value = ref("");
const return_value = ref("")
const submit = () => {
    const config = useRuntimeConfig();
    const {data} = useFetch("http://192.168.0.29:8000/text", {
        method: "post",
        params: {code : input_value.value},
    });
    console.log(data.value);
    return_value.value = data.value
}
</script>
<template>
    <input type="text" v-model="input_value" placeholder="テキストを入力" />
    <button @click="submit">送信</button>
    <div>
    インプット：{{input_value}}
    <br />
    リターン：{{ return_value }}
    </div>
</template>