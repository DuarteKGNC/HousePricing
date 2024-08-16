<template>
    <input type="text" :id="$props.id" :placeholder="$props.placeholder">
</template>
<script>
export default {
    name:'InputField',
    props: {
        id: String,
        placeholder: String
    }
}
</script>