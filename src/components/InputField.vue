<template>
    <label :for="$props.id">{{ $props.placeholder }}</label>
    <div class="input-group input-group-sm mb-2">
        <input v-model="value" type="number" min="0" class="form-control" :id="$props.id" onkeydown="return false">
    </div>
</template>
<script>
export default {
    name:'InputField',
    props: {
        id: String,
        placeholder: String
    },
    data(){
        return{
            value: 0
        }
    },
}
</script>